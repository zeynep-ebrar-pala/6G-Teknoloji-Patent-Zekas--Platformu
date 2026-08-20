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
from backend.tt_europe_service import TTEuropeService
from data.glossary import glossary_plain_corpus
from i18n.core import format_int, t

def _is_beginner(view_mode: str) -> bool:
    text = str(view_mode or "beginner")
    if text in ("beginner", "expert"):
        return text == "beginner"
    if "Uzman" in text or "Expert" in text:
        return False
    return True


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
        layers = DataService.teaching_layers(tech["id"])
        chunks.append(
            {
                "id": f"tech:{tech['id']}:temel",
                "title": f"{tech['acronym']} — {tech['title']} Temel (TRL {tech['trl']})",
                "text": " ".join(
                    [
                        tech.get("title", ""),
                        tech.get("acronym", ""),
                        layers["beginner"],
                        _strip_html(tech.get("beginner_card", "")),
                        _strip_html(tech.get("beginner_principle", "")),
                        _strip_html(tech.get("beginner_arch", "")),
                    ]
                ),
            }
        )
        chunks.append(
            {
                "id": f"tech:{tech['id']}:uzman",
                "title": f"{tech['acronym']} — {tech['title']} Uzman (TRL {tech['trl']})",
                "text": " ".join(
                    [
                        tech.get("title", ""),
                        tech.get("acronym", ""),
                        layers["expert"],
                        layers["formulas"],
                        layers["comparison"],
                        _strip_html(tech.get("working_principle", "")),
                        _strip_html(tech.get("system_architecture", "")),
                        " ".join(tech.get("advantages", [])),
                        " ".join(tech.get("disadvantages", [])),
                    ]
                ),
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
    tt_sum = TTEuropeService.summary()
    pos = TTEuropeService.europe_position()
    leaders = pos.get("europe_pub_leaders") or []
    lead_txt = "; ".join(f"{r['name_en']} {r['lead']} {r['n']}" for r in leaders[:8]) or "none"
    chunks.append(
        {
            "id": "tt_eu:overview",
            "title": t("tt_eu.what_title"),
            "text": " ".join(
                [
                    _strip_html(t("tt_eu.what_body")),
                    _strip_html(t("tt_eu.role_body")),
                    _strip_html(t("tt_eu.expert_body")),
                    f"Google Patents Netsia {tt_sum['patent_n']} papers {tt_sum['paper_n']}",
                    (
                        f"Türk Telekom Europe position: Türkiye publication rank {pos['tr_pub_rank']} "
                        f"({pos['tr_pub_n']} DOI), patent rank {pos['tr_pat_rank']} ({pos['tr_pat_n']} Netsia Google Patents). "
                        f"Non-TR countries with TT papers {pos['pub_outside_tr']}. "
                        f"In-country publication leaders: {lead_txt}. "
                        "Countries are separate leagues; no invented pan-Europe rank."
                    ),
                    "Netsia Inc Türk Telekom grubu operatör toptan TTI",
                ]
            ),
        }
    )
    for pat in TTEuropeService.get_patents():
        chunks.append(
            {
                "id": f"tt_eu:patent:{pat['publication_number']}",
                "title": f"{pat['publication_number']} — {pat['title']}",
                "text": f"{pat['title']} {pat.get('assignee','')} Netsia Türk Telekom {pat.get('domain','')} {pat.get('abstract','')}",
            }
        )
    for paper in TTEuropeService.get_papers():
        chunks.append(
            {
                "id": f"tt_eu:paper:{paper.get('doi','')}",
                "title": paper["title"],
                "text": (
                    f"{paper['title']} {paper.get('authors','')} {paper.get('journal','')} "
                    f"Türk Telekom Ar-Ge Türkiye DOI {paper.get('doi','')} {paper.get('note','')}"
                ),
            }
        )
    for row in TTEuropeService.get_touchpoints():
        chunks.append(
            {
                "id": f"tt_eu:touch:{row['country']}",
                "title": f"{row['country_name_tr']} — {row['title_tr']}",
                "text": f"{row['title_tr']} {row['title_en']} {row['detail_tr']} {row['detail_en']} {row['url']}",
            }
        )
    return chunks


def _retrieve(question: str, k: int = 6, view_mode: str = "") -> List[Dict[str, str]]:
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
    q_upper = question.upper()
    selected = []
    for idx, score in ranked:
        cid = str(chunks[idx].get("id", ""))
        title = str(chunks[idx].get("title", "")).upper()
        if cid.startswith("tech:") or cid == "glossary":
            score += 0.18
        if cid.endswith(":temel") and _is_beginner(view_mode):
            score += 0.14
        if cid.endswith(":uzman") and not _is_beginner(view_mode):
            score += 0.14
        if any(tok in q_upper and tok in title for tok in ("RIS", "ISAC", "NTN", "THZ", "MIMO", "IOT", "AI-RAN", "AIRAN")):
            score += 0.22
        selected.append((score, chunks[idx]))
    selected.sort(key=lambda x: x[0], reverse=True)
    out = []
    for score, ch in selected[:k]:
        if score <= 0:
            continue
        item = dict(ch)
        item["score"] = f"{score:.3f}"
        out.append(item)
    return out or chunks[: min(k, len(chunks))]


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
        limit = 2000 if str(ch.get("id", "")).startswith("tech:") else 1200
        lines.append(ch["text"][:limit])
        lines.append("")
    return "\n".join(lines)


def _system_preamble() -> str:
    return t("ai.system")


GROQ_CHAT_MODELS = (
    "openai/gpt-oss-120b",
    "qwen/qwen3.6-27b",
    "openai/gpt-oss-20b",
)
GEMINI_CHAT_MODELS = (
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-flash-latest",
)


def _message_text(response) -> str:
    msg = response.choices[0].message
    text = getattr(msg, "content", None) or ""
    if not text:
        text = getattr(msg, "reasoning", None) or ""
    return str(text)


def _answer_with_groq(question: str, api_key: str, context: str) -> str:
    from groq import Groq

    client = Groq(api_key=api_key)
    messages = [
        {"role": "system", "content": _system_preamble() + "\n\n" + context},
        {"role": "user", "content": question},
    ]
    last_exc: Exception | None = None
    for model in GROQ_CHAT_MODELS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.2,
                max_tokens=1800,
            )
            text = _message_text(response)
            if text.strip():
                return text
        except Exception as exc:
            last_exc = exc
    if last_exc:
        raise last_exc
    return ""


def _answer_with_gemini(question: str, api_key: str, context: str) -> str:
    from google import genai

    client = genai.Client(api_key=api_key)
    prompt = (
        f"{_system_preamble()}\n\n{context}\n\n{t('ai.user_wrap', question=question)}"
    )
    last_exc: Exception | None = None
    for model in GEMINI_CHAT_MODELS:
        try:
            response = client.models.generate_content(model=model, contents=prompt)
            text = getattr(response, "text", None) or ""
            if str(text).strip():
                return str(text)
        except Exception as exc:
            last_exc = exc
    if last_exc:
        raise last_exc
    return ""


def _fallback_from_chunks(question: str, chunks: List[Dict[str, str]]) -> str:
    if not chunks:
        return t("ai.fallback_none")
    preferred = [c for c in chunks if str(c.get("id", "")).startswith("tech:") or c.get("id") == "glossary"]
    ordered = preferred + [c for c in chunks if c not in preferred]
    parts = [f"### {ordered[0]['title']}\n\n{ordered[0]['text'][:900]}"]
    extras = [c for c in ordered[1:] if not str(c.get("id", "")).startswith("patent:")][:3]
    if extras:
        parts.append(f"\n\n{t('ai.related')}\n" + "\n".join(f"- {c['title']}" for c in extras))
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

        chunks = _retrieve(question, view_mode=view_mode or "")
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
            except Exception:
                return {"response": _fallback_from_chunks(question, chunks), "type": "fallback"}

        return {"response": _fallback_from_chunks(question, chunks), "type": "fallback"}
