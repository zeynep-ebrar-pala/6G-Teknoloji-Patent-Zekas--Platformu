"""
Türk Telekom 6G AI Assistant Service
sklearn TF-IDF yerel geri getirme + Groq / Gemini.
LLM bağlamı kısa tutulur (Groq TPM limiti); yerel yanıt Dual-Depth + donanım yapılandırır.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Optional, Sequence

from backend.academic_service import AcademicService
from backend.data_service import DataService
from backend.patent_service import PatentService
from backend.tt_europe_service import TTEuropeService
from data.glossary import GLOSSARY, localized_entry
from i18n.core import format_int, t

_TECH_HINTS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("ai_ran", ("AI-RAN", "AIRAN", "AI RAN", "YAPAY ZEKA TABANLI")),
    ("cell_free", ("CELL-FREE", "CELL FREE", "HUCRESIZ", "CF MIMO", "CF-MIMO")),
    ("ambient_iot", ("AMBIENT", "PILSIZ", "PİLSİZ", "ORTAM ENERJI", "ORTAM ENERJİ")),
    ("isac", ("ISAC",)),
    ("ris", ("RIS",)),
    ("ntn", ("NTN",)),
    ("thz", ("THZ", "TERAHERTZ")),
)

_CTX_BUDGET = 5200
_CTX_BUDGET_RETRY = 3200


def _is_beginner(view_mode: str) -> bool:
    text = str(view_mode or "beginner")
    if text in ("beginner", "expert"):
        return text == "beginner"
    if "Uzman" in text or "Expert" in text:
        return False
    return True


def _strip_html(text: str) -> str:
    cleaned = re.sub(r"<[^>]+>", " ", text or "")
    cleaned = re.sub(r"\$\$[^$]+\$\$", " ", cleaned)
    cleaned = re.sub(r"\$[^$]+\$", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()


def _list_bits(items: Any, *, titles_only: bool = False) -> str:
    bits: List[str] = []
    for item in items or []:
        if isinstance(item, dict):
            if titles_only:
                bits.append(str(item.get("title") or ""))
            else:
                bits.append(
                    " ".join(
                        str(item.get(k) or "")
                        for k in ("title", "description", "how", "when_not", "text")
                    )
                )
        else:
            bits.append(_strip_html(str(item)))
    return " · ".join(b for b in bits if b.strip())


def _fold(text: str) -> str:
    table = {
        ord("İ"): "I",
        ord("I"): "I",
        ord("ı"): "I",
        ord("Ş"): "S",
        ord("ş"): "S",
        ord("Ğ"): "G",
        ord("ğ"): "G",
        ord("Ü"): "U",
        ord("ü"): "U",
        ord("Ö"): "O",
        ord("ö"): "O",
        ord("Ç"): "C",
        ord("ç"): "C",
    }
    return (text or "").translate(table).upper().replace("-", " ")


def _mentioned_tech_ids(question: str) -> List[str]:
    folded = _fold(question)
    hits: List[tuple[int, str]] = []
    for tech_id, aliases in _TECH_HINTS:
        best = -1
        for alias in aliases:
            pos = folded.find(_fold(alias))
            if pos >= 0 and (best < 0 or pos < best):
                best = pos
        if best >= 0:
            hits.append((best, tech_id))
    hits.sort(key=lambda x: x[0])
    return [tid for _, tid in hits]


def _is_compare(question: str) -> bool:
    folded = _fold(question)
    return any(tok in folded for tok in ("FARK", "VS", "KARSILASTIR", "KARŞILAŞTIR", "BETWEEN", "VERSUS"))


def _is_patent_q(question: str) -> bool:
    folded = _fold(question)
    return any(
        tok in folded
        for tok in ("PATENT", "LENS", "USPTO", "EPO", "FIRMA", "FİRMA", "ASSIGNEE", "GRANT")
    )


def _glossary_line(abbr: str) -> str:
    item = GLOSSARY.get(abbr) or next(
        (v for v in GLOSSARY.values() if v.get("abbr") == abbr), None
    )
    if not item:
        return abbr
    loc = localized_entry(abbr) or localized_entry(item["abbr"]) or item
    return (
        f"{item['abbr']} ({item['en']} — {item['tr']}): "
        f"{loc.get('definition', '')} {loc.get('why', '')}"
    ).strip()


def _tech_structured(tech_id: str, beginner: bool, *, compact: bool = False) -> str:
    """Dual-Depth + donanım blokları; LLM ve yerel yanıt aynı kaynaktan."""
    tech = DataService.get_technology_by_id(tech_id)
    if not tech:
        return ""
    layers = DataService.teaching_layers(tech_id)
    foundation = layers["beginner"] if beginner else (layers["beginner"] + " " + layers["expert"])
    hw_cap = 900 if compact else 1600
    use_cap = 600 if compact else 1100
    parts = [
        f"## {tech['acronym']} — {tech['title']} (TRL {tech['trl']})",
        _glossary_line(tech["acronym"]),
        "",
        f"### {t('ai.sec_what')}",
        _strip_html(tech.get("executive_summary", ""))[: (700 if compact else 1200)],
        _strip_html(foundation)[: (900 if compact else 1600)],
        "",
        f"### {t('ai.sec_how_hw')}",
        _strip_html(tech.get("beginner_principle", ""))[:700],
        _strip_html(tech.get("working_principle", ""))[:hw_cap],
        _strip_html(tech.get("system_architecture", ""))[:hw_cap],
        "",
        f"### {t('ai.sec_use')}",
        _list_bits(tech.get("use_cases"))[:use_cap],
        _list_bits(tech.get("tt_scenarios"))[: (500 if compact else 900)],
        "",
        f"### {t('ai.sec_limit')}",
        " · ".join(tech.get("disadvantages") or []),
        str(tech.get("trl_desc") or ""),
    ]
    if not beginner:
        parts.extend(
            [
                "",
                f"### {t('ai.sec_expert')}",
                _strip_html(layers.get("formulas", ""))[:900],
                _strip_html(layers.get("comparison", ""))[:700],
                " · ".join(tech.get("advantages") or [])[:500],
            ]
        )
    return "\n".join(p for p in parts if str(p).strip())


def _patent_structured(*, compact: bool = False) -> str:
    summary = PatentService.get_summary()
    tops = PatentService.get_top_patents()[: 6 if compact else 10]
    company_bits = []
    counts = summary.get("company_counts") or {}
    for name, n in sorted(counts.items(), key=lambda x: (-int(x[1]), str(x[0])))[:8]:
        company_bits.append(f"{name}: {format_int(int(n))}")
    topic_bits = []
    for name, n in (summary.get("topic_counts") or {}).items():
        if int(n) > 0:
            topic_bits.append(f"{name}: {format_int(int(n))}")
    lines = [
        f"## {t('ai.sec_patents')}",
        t(
            "ai.patent_summary_body",
            total=format_int(int(summary.get("total") or 0)),
            source=str(summary.get("source") or "Lens.org"),
            leader=str(summary.get("leader_company") or "—"),
            leader_n=format_int(int(summary.get("leader_count") or 0)),
            top_domain=str(summary.get("top_domain") or "—"),
            top_domain_n=format_int(int(summary.get("top_domain_count") or 0)),
        ),
        "",
        t("ai.patent_by_company") + " " + "; ".join(company_bits),
        t("ai.patent_by_topic") + " " + "; ".join(topic_bits),
        "",
        t("ai.patent_examples"),
    ]
    for pat in tops:
        lines.append(
            f"- {pat.get('publication_number')} — {pat.get('title')} "
            f"({pat.get('assignee')}, {pat.get('domain')}, {pat.get('year')})"
        )
    return "\n".join(lines)


def _glossary_chunks() -> List[Dict[str, str]]:
    chunks: List[Dict[str, str]] = []
    from i18n.core import get_lang

    lang = get_lang()
    for key, item in GLOSSARY.items():
        loc = localized_entry(key) or item
        if lang == "en":
            text = f"{item['abbr']} ({item['en']}): {loc['definition']} {loc['why']}"
        else:
            text = (
                f"{item['abbr']} ({item['en']} — {item['tr']}): "
                f"{loc['definition']} {loc['why']}"
            )
        chunks.append({"id": f"glossary:{item['abbr']}", "title": item["abbr"], "text": text})
    return chunks


def _tech_chunks() -> List[Dict[str, str]]:
    chunks: List[Dict[str, str]] = []
    for tech in DataService.get_all_technologies().values():
        for beginner, suffix in ((True, "temel"), (False, "uzman")):
            chunks.append(
                {
                    "id": f"tech:{tech['id']}:{suffix}",
                    "title": f"{tech['acronym']} — {tech['title']} ({suffix})",
                    "text": _tech_structured(tech["id"], beginner, compact=True),
                }
            )
    return chunks


def _corpus() -> List[Dict[str, str]]:
    chunks: List[Dict[str, str]] = []
    chunks.extend(_glossary_chunks())
    chunks.extend(_tech_chunks())
    chunks.append(
        {
            "id": "patent:overview",
            "title": t("ai.sec_patents"),
            "text": _patent_structured(compact=True),
        }
    )
    for pat in PatentService.get_top_patents():
        chunks.append(
            {
                "id": f"patent:{pat['publication_number']}",
                "title": f"{pat['publication_number']} — {pat['title']}",
                "text": (
                    f"{pat['title']} {pat.get('assignee','')} {pat.get('domain','')} "
                    f"{pat.get('year','')} {pat.get('abstract','')}"
                ),
            }
        )
    for paper in AcademicService.get_most_cited_papers():
        cite = paper.get("citations")
        cite_txt = t("ai.cite_n", n=format_int(cite)) if isinstance(cite, int) else t("ai.cite_na")
        chunks.append(
            {
                "id": f"paper:{paper.get('doi','')}",
                "title": paper["title"],
                "text": (
                    f"{paper['title']} {paper.get('authors','')} {paper.get('journal','')} "
                    f"{paper.get('year','')} {cite_txt} DOI {paper.get('doi','')} "
                    f"{paper.get('abstract') or paper.get('note') or ''}"
                ),
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
                    f"Google Patents Netsia {tt_sum['patent_n']} papers {tt_sum['paper_n']}",
                    (
                        f"Türk Telekom Europe position: {pos['tr_pub_n']} locked DOI papers in Türkiye; "
                        f"{pos['tr_pat_n']} Netsia grants at USPTO in this sample. "
                        f"Non-TR countries with TT papers {pos['pub_outside_tr']}. "
                        f"In-country publication leaders: {lead_txt}."
                    ),
                ]
            ),
        }
    )
    return chunks


def _retrieve(question: str, k: int = 8, view_mode: str = "") -> List[Dict[str, str]]:
    chunks = _corpus()
    if not chunks:
        return []
    mentioned = _mentioned_tech_ids(question)
    patent_q = _is_patent_q(question)
    want = k + (2 if _is_compare(question) else 0) + (2 if patent_q else 0)
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
    except ImportError:
        q = question.lower()
        scored = []
        for ch in chunks:
            hay = (ch["title"] + " " + ch["text"]).lower()
            score = sum(1 for w in q.split() if len(w) > 2 and w.lower() in hay)
            scored.append((score, ch))
        scored.sort(key=lambda x: x[0], reverse=True)
        picked = [c for s, c in scored[:want] if s > 0] or chunks[:want]
        return _merge_forced(picked, chunks, mentioned, view_mode, want, patent_q)

    docs = [c["title"] + " " + c["text"] for c in chunks]
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True)
    matrix = vectorizer.fit_transform(docs + [question])
    sims = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
    ranked = sorted(enumerate(sims), key=lambda x: x[1], reverse=True)
    q_upper = _fold(question)
    selected: List[tuple[float, Dict[str, str]]] = []
    beginner = _is_beginner(view_mode)
    for idx, score in ranked:
        cid = str(chunks[idx].get("id", ""))
        title = _fold(chunks[idx].get("title", ""))
        if cid.startswith("tech:") or cid.startswith("glossary:"):
            score += 0.12
        if cid.startswith("patent:") and patent_q:
            score += 0.45
        if cid == "patent:overview" and patent_q:
            score += 0.6
        if cid.endswith(":temel") and beginner:
            score += 0.12
        if cid.endswith(":uzman") and not beginner:
            score += 0.12
        for tok in ("RIS", "ISAC", "NTN", "THZ", "MIMO", "IOT", "AI RAN", "AIRAN", "TRL"):
            if tok in q_upper and tok in title:
                score += 0.28
                break
        selected.append((float(score), chunks[idx]))
    selected.sort(key=lambda x: x[0], reverse=True)
    picked: List[Dict[str, str]] = []
    for score, ch in selected[:want]:
        if score <= 0:
            continue
        item = dict(ch)
        item["score"] = f"{score:.3f}"
        picked.append(item)
    if not picked:
        picked = [dict(c) for c in chunks[: min(want, len(chunks))]]
    return _merge_forced(picked, chunks, mentioned, view_mode, want, patent_q)


def _merge_forced(
    picked: List[Dict[str, str]],
    chunks: List[Dict[str, str]],
    tech_ids: Sequence[str],
    view_mode: str,
    limit: int,
    patent_q: bool = False,
) -> List[Dict[str, str]]:
    beginner = _is_beginner(view_mode)
    suffix = "temel" if beginner else "uzman"
    other = "uzman" if beginner else "temel"
    by_id = {str(c.get("id")): c for c in chunks}
    seen = {str(c.get("id")) for c in picked}
    extra: List[Dict[str, str]] = []
    if patent_q:
        row = by_id.get("patent:overview")
        if row and "patent:overview" not in seen:
            extra.append(dict(row))
            seen.add("patent:overview")
    for tid in tech_ids:
        for end in (suffix, other):
            cid = f"tech:{tid}:{end}"
            row = by_id.get(cid)
            if row and cid not in seen:
                extra.append(dict(row))
                seen.add(cid)
    return (extra + picked)[: max(limit, len(extra) + min(3, len(picked)))]


def _build_answer_body(question: str, view_mode: str = "", *, compact: bool = False) -> tuple[str, List[str]]:
    """Yapılı Dual-Depth yanıt gövdesi + kaynak başlıkları."""
    beginner = _is_beginner(view_mode)
    tech_ids = _mentioned_tech_ids(question)
    sources: List[str] = []
    blocks: List[str] = []

    if _is_patent_q(question) and not tech_ids:
        blocks.append(_patent_structured(compact=compact))
        sources.append(t("ai.sec_patents"))
        for pat in PatentService.get_top_patents()[:5]:
            sources.append(f"{pat.get('publication_number')} — {pat.get('title')}")
        return "\n\n".join(blocks), _uniq(sources)

    if tech_ids:
        for tid in tech_ids:
            body = _tech_structured(tid, beginner, compact=compact)
            if body:
                blocks.append(body)
                tech = DataService.get_technology_by_id(tid)
                if tech:
                    sources.append(f"{tech['acronym']} — {tech['title']}")
        if _is_compare(question) and len(tech_ids) >= 2:
            blocks.append(f"\n### {t('ai.sec_compare')}\n{t('ai.compare_hint')}")
        return "\n\n".join(blocks), _uniq(sources)

    chunks = _retrieve(question, view_mode=view_mode)
    for ch in chunks[:4]:
        cid = str(ch.get("id", ""))
        if cid.startswith("tech:"):
            parts = cid.split(":")
            if len(parts) >= 2:
                body = _tech_structured(parts[1], beginner, compact=True)
                if body:
                    blocks.append(body)
                    sources.append(ch["title"])
                    continue
        if cid == "patent:overview" or (cid.startswith("patent:") and _is_patent_q(question)):
            blocks.append(_patent_structured(compact=True))
            sources.append(t("ai.sec_patents"))
            continue
        blocks.append(f"### {ch['title']}\n\n{ch['text'][: (900 if compact else 1400)]}")
        sources.append(ch["title"])
    if not blocks:
        return t("ai.fallback_none"), []
    return "\n\n".join(blocks), _uniq(sources)


def _uniq(items: Sequence[str]) -> List[str]:
    out: List[str] = []
    seen: set[str] = set()
    for item in items:
        text = str(item or "").strip()
        if text and text not in seen:
            seen.add(text)
            out.append(text)
    return out[:8]


def _format_context(question: str, view_mode: str = "", budget: int = _CTX_BUDGET) -> tuple[str, List[str]]:
    depth = t("ai.depth_beginner") if _is_beginner(view_mode) else t("ai.depth_expert")
    body, sources = _build_answer_body(question, view_mode, compact=True)
    header = "\n".join(
        [
            t("ai.ctx_header"),
            t("ai.pedagogy"),
            depth,
            t("ai.ctx_rule"),
            t("ai.complete_rule"),
            "",
        ]
    )
    if len(header) + len(body) > budget:
        body = body[: max(800, budget - len(header) - 40)]
    return header + body, sources


def _system_preamble() -> str:
    return t("ai.system") + "\n" + t("ai.complete_rule")


GROQ_CHAT_MODELS = (
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "openai/gpt-oss-120b",
    "qwen/qwen3.6-27b",
    "openai/gpt-oss-20b",
)
GEMINI_CHAT_MODELS = (
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-flash-latest",
    "gemini-2.5-pro",
)


def _history_messages(history: Optional[Sequence[Dict[str, Any]]]) -> List[Dict[str, str]]:
    out: List[Dict[str, str]] = []
    for msg in list(history or [])[-4:]:
        role = str(msg.get("role") or "")
        content = str(msg.get("content") or "").strip()
        if role not in ("user", "assistant") or not content:
            continue
        if role == "assistant" and len(out) == 0:
            continue
        out.append({"role": role, "content": content[:1200]})
    return out[-4:]


def _message_text(response) -> str:
    msg = response.choices[0].message
    text = getattr(msg, "content", None) or ""
    if not text:
        text = getattr(msg, "reasoning", None) or ""
    return str(text)


def _too_large(exc: Exception) -> bool:
    text = str(exc).lower()
    return "413" in text or "too large" in text or "tokens per minute" in text or "request too large" in text


def _answer_with_groq(
    question: str,
    api_key: str,
    context: str,
    history: Optional[Sequence[Dict[str, Any]]] = None,
) -> str:
    from groq import Groq

    client = Groq(api_key=api_key)
    messages: List[Dict[str, str]] = [
        {"role": "system", "content": _system_preamble() + "\n\n" + context},
        *_history_messages(history),
        {"role": "user", "content": question},
    ]
    last_exc: Exception | None = None
    for model in GROQ_CHAT_MODELS:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.2,
                max_tokens=2048,
            )
            text = _message_text(response)
            if text.strip():
                return text
        except Exception as exc:
            last_exc = exc
            if _too_large(exc):
                continue
    if last_exc:
        raise last_exc
    return ""


def _answer_with_gemini(
    question: str,
    api_key: str,
    context: str,
    history: Optional[Sequence[Dict[str, Any]]] = None,
) -> str:
    from google import genai

    client = genai.Client(api_key=api_key)
    prior = "\n".join(f"{m['role']}: {m['content']}" for m in _history_messages(history))
    prompt = (
        f"{_system_preamble()}\n\n{context}\n\n"
        f"{prior}\n\n{t('ai.user_wrap', question=question)}"
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


def _fallback_from_question(question: str, view_mode: str = "") -> tuple[str, List[str]]:
    body, sources = _build_answer_body(question, view_mode, compact=False)
    note = f"\n\n{t('ai.tfidf_note')}"
    return body + note, sources


class AIAssistantService:
    """Groq/Gemini destekli, TF-IDF geri getirmeli 6G asistan servisi."""

    @classmethod
    def answer_question(
        cls,
        question: str,
        provider: Optional[str] = None,
        api_key: Optional[str] = None,
        view_mode: Optional[str] = None,
        history: Optional[Sequence[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        if not (question or "").strip():
            return {"response": t("ai.empty_q"), "type": "error", "sources": []}

        mode = view_mode or ""
        local, sources = _fallback_from_question(question, mode)
        provider = (provider or "groq").lower()
        key = (api_key or "").strip()

        if key and provider in ("groq", "gemini"):
            try:
                context, ctx_sources = _format_context(question, mode, budget=_CTX_BUDGET)
                sources = _uniq(list(ctx_sources) + list(sources))
                if provider == "gemini":
                    text = _answer_with_gemini(question, key, context, history)
                else:
                    try:
                        text = _answer_with_groq(question, key, context, history)
                    except Exception as exc:
                        if _too_large(exc):
                            context, ctx_sources = _format_context(
                                question, mode, budget=_CTX_BUDGET_RETRY
                            )
                            sources = _uniq(list(ctx_sources) + list(sources))
                            text = _answer_with_groq(question, key, context, None)
                        else:
                            raise
                if len(text.strip()) >= 280:
                    return {"response": text.strip(), "type": "llm", "sources": sources}
                if text.strip():
                    return {
                        "response": text.strip() + "\n\n" + local,
                        "type": "llm",
                        "sources": sources,
                    }
            except Exception as exc:
                note = t("ai.llm_fail", exc=str(exc)[:180])
                return {"response": f"{local}\n\n{note}", "type": "fallback", "sources": sources}

        return {"response": local, "type": "fallback", "sources": sources}
