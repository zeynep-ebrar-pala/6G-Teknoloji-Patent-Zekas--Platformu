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
from data.glossary import glossary_plain_corpus
from i18n.core import format_int, t

def _is_beginner(view_mode: str) -> bool:
    if view_mode in ("beginner", "expert"):
        return view_mode == "beginner"
    return "Temel" in str(view_mode or "")


def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text or "").replace("\n", " ").strip()


def _corpus() -> List[Dict[str, str]]:
    """Modül 1–3 doğrulanmış metin parçaları + sözlük + formül açıklaması."""
    chunks: List[Dict[str, str]] = []
    chunks.append(
        {
            "id": "glossary",
            "title": t("ai.glossary_title"),
            "text": glossary_plain_corpus(),
        }
    )
    for tech in DataService.get_all_technologies().values():
        fnd = tech.get("foundation") or {}
        formula_bits = []
        for frm in tech.get("formulas") or []:
            formula_bits.append(
                f"{frm.get('name','')} {frm.get('tells_us','')} {frm.get('why_this_form','')} "
                f"{frm.get('when_valid','')} {frm.get('assumptions','')}"
            )
        cmp_ = tech.get("comparison") or {}
        body = " ".join(
            [
                tech.get("title", ""),
                tech.get("acronym", ""),
                _strip_html(tech.get("executive_summary", "")),
                _strip_html(tech.get("beginner_card", "")),
                str(fnd.get("what", "")),
                str(fnd.get("why_needed", "")),
                str(fnd.get("problem", "")),
                str(fnd.get("mental_model", "")),
                str(fnd.get("analogy_technical_map", "")),
                str(fnd.get("when_used", "")),
                str(fnd.get("when_not", "")),
                str(fnd.get("not_to_confuse", "")),
                str(fnd.get("real_world", "")),
                str(fnd.get("tt_impact", "")),
                _strip_html(tech.get("beginner_principle", "")),
                _strip_html(tech.get("beginner_arch", "")),
                _strip_html(tech.get("working_principle", "")),
                _strip_html(tech.get("system_architecture", "")),
                " ".join(tech.get("advantages", [])),
                " ".join(tech.get("disadvantages", [])),
                " ".join(formula_bits),
                str(cmp_.get("title", "")),
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
        cite_txt = t("ai.cite_n", n=format_int(cite)) if isinstance(cite, int) else t("ai.cite_na")
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


def _format_context(chunks: List[Dict[str, str]], view_mode: str = "") -> str:
    depth = t("ai.depth_beginner") if _is_beginner(view_mode) else t("ai.depth_expert")
    lines = [
        t("ai.ctx_header"),
        t("ai.pedagogy"),
        depth,
        t("ai.ctx_rule"),
        "",
    ]
    for ch in chunks:
        lines.append(f"[{ch['id']}] {ch['title']}")
        lines.append(ch["text"][:1400])
        lines.append("")
    return "\n".join(lines)


def _system_preamble() -> str:
    return t("ai.system")


def _answer_with_groq(question: str, api_key: str, context: str) -> str:
    from groq import Groq

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": _system_preamble() + "\n\n" + context,
            },
            {"role": "user", "content": question},
        ],
        temperature=0.2,
        max_tokens=1800,
    )
    return response.choices[0].message.content or ""


def _answer_with_gemini(question: str, api_key: str, context: str) -> str:
    from google import genai

    client = genai.Client(api_key=api_key)
    prompt = (
        f"{_system_preamble()}\n\n{context}\n\n{t('ai.user_wrap', question=question)}"
    )
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text or ""


def _fallback_from_chunks(question: str, chunks: List[Dict[str, str]]) -> str:
    if not chunks:
        return t("ai.fallback_none")
    parts = [f"### {chunks[0]['title']}\n\n{chunks[0]['text'][:700]}"]
    if len(chunks) > 1:
        extras = "\n".join(f"- {c['title']}" for c in chunks[1:4])
        parts.append(f"\n\n{t('ai.related')}\n{extras}")
    parts.append(f"\n\n{t('ai.tfidf_note')}")
    return "".join(parts)


class AIAssistantService:
    """Groq/Gemini destekli, TF-IDF geri getirmeli 6G asistan servisi."""

    @classmethod
    def answer_question(
        cls,
        question: str,
        provider: Optional[str] = None,
        api_key: Optional[str] = None,
        view_mode: Optional[str] = None,
    ) -> Dict[str, Any]:
        if not (question or "").strip():
            return {"response": t("ai.empty_q"), "type": "error"}

        chunks = _retrieve(question)
        context = _format_context(chunks, view_mode or "")
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
                    "response": f"{fallback}\n\n---\n{t('ai.llm_fail', exc=exc)}",
                    "type": "fallback",
                }

        return {"response": _fallback_from_chunks(question, chunks), "type": "fallback"}
