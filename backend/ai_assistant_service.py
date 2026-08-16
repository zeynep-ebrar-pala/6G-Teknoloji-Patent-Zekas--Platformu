"""
Türk Telekom 6G AI Assistant Service
sklearn TF-IDF yerel geri getirme + Groq / Gemini.
LLM yalnızca getirilen doğrulanmış parçaları kullanır.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional

from backend.academic_service import AcademicService
from backend.data_service import DataService
from backend.patent_service import PatentService


def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text or "").replace("\n", " ").strip()


def _corpus() -> List[Dict[str, str]]:
    """Modül 1–3 doğrulanmış metin parçaları."""
    chunks: List[Dict[str, str]] = []
    for tech in DataService.get_all_technologies().values():
        body = " ".join(
            [
                tech.get("title", ""),
                tech.get("acronym", ""),
                _strip_html(tech.get("executive_summary", "")),
                _strip_html(tech.get("working_principle", "")),
                _strip_html(tech.get("system_architecture", "")),
                " ".join(tech.get("advantages", [])),
                " ".join(tech.get("disadvantages", [])),
            ]
        )
        chunks.append(
            {
                "id": f"tech:{tech['id']}",
                "title": f"{tech['acronym']} — {tech['title']} (TRL {tech['trl']})",
                "text": body,
            }
        )
    for pat in PatentService.get_top_patents():
        chunks.append(
            {
                "id": f"patent:{pat['publication_number']}",
                "title": f"{pat['publication_number']} — {pat['title']}",
                "text": f"{pat['title']} {pat.get('assignee','')} {pat.get('domain','')} {pat.get('abstract','')}",
            }
        )
    for paper in AcademicService.get_most_cited_papers():
        cite = paper.get("citations")
        cite_txt = f"{cite} atıf" if isinstance(cite, int) else "atıf sayısı OpenAlex'ten alınamadı"
        chunks.append(
            {
                "id": f"paper:{paper.get('doi','')}",
                "title": paper["title"],
                "text": f"{paper['title']} {paper.get('authors','')} {paper.get('journal','')} {cite_txt} DOI {paper.get('doi','')}",
            }
        )
    return chunks


def _retrieve(question: str, k: int = 6) -> List[Dict[str, str]]:
    chunks = _corpus()
    if not chunks:
        return []
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
    except ImportError:
        q = question.lower()
        scored = []
        for ch in chunks:
            hay = (ch["title"] + " " + ch["text"]).lower()
            score = sum(1 for w in q.split() if len(w) > 3 and w in hay)
            scored.append((score, ch))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [c for s, c in scored[:k] if s > 0] or chunks[:k]

    docs = [c["title"] + " " + c["text"] for c in chunks]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(docs + [question])
    sims = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
    ranked = sorted(enumerate(sims), key=lambda x: x[1], reverse=True)
    selected = []
    for idx, score in ranked[:k]:
        if score <= 0:
            continue
        item = dict(chunks[idx])
        item["score"] = f"{score:.3f}"
        selected.append(item)
    return selected or chunks[: min(k, len(chunks))]


def _format_context(chunks: List[Dict[str, str]]) -> str:
    lines = [
        "=== DOĞRULANMIŞ 6G VERİ BAĞLAMI (TF-IDF ile seçilmiş parçalar) ===",
        "KURAL: Bu bağlamda olmayan sayı, patent ID veya makale uydurma.",
        "Emin değilsen 'Platform verisinde bu bilgi yok' de.",
        "",
    ]
    for ch in chunks:
        lines.append(f"[{ch['id']}] {ch['title']}")
        lines.append(ch["text"][:900])
        lines.append("")
    return "\n".join(lines)


def _answer_with_groq(question: str, api_key: str, context: str) -> str:
    from groq import Groq

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "Türk Telekom 6G Ar-Ge asistanısın. Yalnızca verilen bağlamı kullan. "
                    "Tahmin veya uydurma yapma.\n\n" + context
                ),
            },
            {"role": "user", "content": question},
        ],
        temperature=0.2,
        max_tokens=900,
    )
    return response.choices[0].message.content or ""


def _answer_with_gemini(question: str, api_key: str, context: str) -> str:
    from google import genai

    client = genai.Client(api_key=api_key)
    prompt = (
        "Türk Telekom 6G Ar-Ge asistanısın. Yalnızca aşağıdaki doğrulanmış bağlamı kullan; "
        "bilgi yoksa uydurma.\n\n"
        f"{context}\n\nKullanıcı sorusu: {question}"
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text or ""


def _fallback_from_chunks(question: str, chunks: List[Dict[str, str]]) -> str:
    if not chunks:
        return (
            "### 6G Asistan (veri tabanlı mod)\n\n"
            "Sorunuz platform veri kümesinde eşleşmedi. "
            "6G Teknolojileri, Patent Zekası veya Yayın Trendleri sayfalarındaki "
            "doğrulanmış kaynakları inceleyin."
        )
    parts = [f"### {chunks[0]['title']}\n\n{chunks[0]['text'][:700]}"]
    if len(chunks) > 1:
        extras = "\n".join(f"- {c['title']}" for c in chunks[1:4])
        parts.append(f"\n\n**İlgili doğrulanmış kayıtlar:**\n{extras}")
    parts.append("\n\n*Yanıt TF-IDF ile seçilen platform kayıtlarındandır; sayı uydurulmaz.*")
    return "".join(parts)


class AIAssistantService:
    """Groq/Gemini destekli, TF-IDF geri getirmeli 6G asistan servisi."""

    @classmethod
    def answer_question(
        cls,
        question: str,
        provider: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        if not (question or "").strip():
            return {"response": "Lütfen bir soru yazın.", "type": "error"}

        chunks = _retrieve(question)
        context = _format_context(chunks)
        provider = (provider or "groq").lower()
        key = (api_key or "").strip()

        if key and provider in ("groq", "gemini"):
            try:
                if provider == "gemini":
                    text = _answer_with_gemini(question, key, context)
                else:
                    text = _answer_with_groq(question, key, context)
                if text.strip():
                    return {"response": text, "type": "llm"}
            except Exception as exc:
                fallback = _fallback_from_chunks(question, chunks)
                return {
                    "response": f"{fallback}\n\n---\n*LLM yanıtı alınamadı: {exc}*",
                    "type": "fallback",
                }

        return {"response": _fallback_from_chunks(question, chunks), "type": "fallback"}
