"""
Türk Telekom 6G Platform - Backend Data Service Layer
Statik sözlük önbelleğe alınmaz: beginner ve uzman derinlik metinleri anında birleşir.
"""

from data.technologies import TECHNOLOGIES

FOUNDATION_KEYS = (
    "what",
    "why_needed",
    "problem",
    "how_steps",
    "mental_model",
    "analogy",
    "analogy_technical_map",
    "when_used",
    "when_not",
    "not_to_confuse",
    "real_world",
    "tt_impact",
)


def _lang() -> str:
    try:
        from i18n.core import get_lang

        return get_lang()
    except Exception:
        return "tr"


def _expert_copy() -> dict:
    if _lang() == "en":
        from data.expert_copy_en import EXPERT_COPY

        return EXPERT_COPY
    from data.expert_copy import EXPERT_COPY

    return EXPERT_COPY


def _is_expert_view() -> bool:
    try:
        import streamlit as st

        mode = st.session_state.get("view_mode", "beginner")
        if mode == "expert":
            return True
        if mode == "beginner":
            return False
        text = str(mode)
        return "Uzman" in text or "Expert" in text
    except Exception:
        return False


def _beginner_copy() -> dict:
    if _lang() == "en":
        from data.beginner_copy_en import BEGINNER_COPY

        return BEGINNER_COPY
    from data.beginner_copy import BEGINNER_COPY

    return BEGINNER_COPY


def _expert_depth() -> dict:
    if _lang() == "en":
        from data.expert_depth_en import EXPERT_DEPTH

        return EXPERT_DEPTH
    from data.expert_depth import EXPERT_DEPTH

    return EXPERT_DEPTH


BEGINNER_SURFACE_KEYS = (
    "use_cases",
    "advantages",
    "disadvantages",
    "global_research",
    "tt_scenarios",
    "highlights",
    "trl_desc",
)


def _beginner_surfaces() -> dict:
    from data.beginner_surfaces import BEGINNER_SURFACES

    return BEGINNER_SURFACES


def _with_layers(tech: dict | None) -> dict | None:
    if not tech:
        return tech
    extra = _beginner_copy().get(tech.get("id"), {})
    expert_extra = _expert_copy().get(tech.get("id"), {}) if _is_expert_view() else {}
    depth = _expert_depth().get(tech.get("id"), {})
    out = dict(tech)
    if _lang() == "en":
        from data.tech_overlay_en import TECH_OVERLAY_EN

        out.update(TECH_OVERLAY_EN.get(tech.get("id"), {}))
    card = extra.get("card")
    if card:
        out["beginner_card"] = card
        out["beginner_one_liner"] = card
    if extra.get("kicker"):
        out["beginner_kicker"] = extra["kicker"]
    if extra.get("principle_html"):
        out["beginner_principle"] = extra["principle_html"]
    if extra.get("arch_html"):
        out["beginner_arch"] = extra["arch_html"]
    if not _is_expert_view() and _lang() == "tr":
        surfaces = _beginner_surfaces().get(tech.get("id"), {})
        for key in BEGINNER_SURFACE_KEYS:
            if surfaces.get(key) is not None:
                out[key] = surfaces[key]
    foundation_src = {k: extra.get(k) for k in FOUNDATION_KEYS if extra.get(k) is not None}
    if expert_extra:
        for k in FOUNDATION_KEYS:
            if expert_extra.get(k) is not None:
                foundation_src[k] = expert_extra[k]
    foundation = {k: foundation_src.get(k) for k in FOUNDATION_KEYS if foundation_src.get(k) is not None}
    if foundation:
        out["foundation"] = foundation
    if depth.get("formulas"):
        out["formulas"] = depth["formulas"]
    if depth.get("comparison"):
        out["comparison"] = depth["comparison"]
    if depth.get("adv_why"):
        out["adv_why"] = depth["adv_why"]
    if depth.get("dis_why"):
        out["dis_why"] = depth["dis_why"]
    if depth.get("global_why"):
        out["global_why"] = depth["global_why"]
    if depth.get("tt_why"):
        out["tt_why"] = depth["tt_why"]
    extras = depth.get("use_case_depth") or []
    if extras:
        merged_uc = []
        for idx, uc in enumerate(out.get("use_cases") or []):
            item = dict(uc) if isinstance(uc, dict) else {"title": f"#{idx+1}", "description": str(uc)}
            if idx < len(extras) and isinstance(extras[idx], dict):
                item["how"] = extras[idx].get("how", "")
                item["when_not"] = extras[idx].get("when_not", "")
            merged_uc.append(item)
        out["use_cases"] = merged_uc
    return out


def _plain_foundation(block: dict) -> str:
    bits: list[str] = []
    for key in FOUNDATION_KEYS:
        val = block.get(key)
        if isinstance(val, list):
            bits.extend(str(item) for item in val if item)
        elif val:
            bits.append(str(val))
    return " ".join(bits)


class DataService:
    """Backend Data Access Service for 6G Knowledge Base."""

    @staticmethod
    def get_all_technologies() -> dict:
        """Returns all 7 6G technologies with teaching + expert depth merged."""
        return {t_id: _with_layers(data) for t_id, data in TECHNOLOGIES.items()}

    @staticmethod
    def get_technology_by_id(tech_id: str) -> dict:
        """Retrieves a specific technology by its unique ID."""
        return _with_layers(TECHNOLOGIES.get(tech_id))

    @staticmethod
    def teaching_layers(tech_id: str) -> dict:
        """Temel ve uzman düz metin — UI ve AI aynı kaynaktan aktarır."""
        extra = _beginner_copy().get(tech_id, {})
        expert = _expert_copy().get(tech_id, {})
        depth = _expert_depth().get(tech_id, {})
        cmp_ = depth.get("comparison") or {}
        formula_bits = []
        for frm in depth.get("formulas") or []:
            formula_bits.append(
                f"{frm.get('name', '')} {frm.get('tells_us', '')} {frm.get('why_this_form', '')} "
                f"{frm.get('when_valid', '')} {frm.get('assumptions', '')}"
            )
        cmp_text = " ".join(
            [str(cmp_.get("title", ""))]
            + [str(h) for h in (cmp_.get("headers") or [])]
            + [" ".join(str(c) for c in row) for row in (cmp_.get("rows") or [])]
        )
        return {
            "beginner": _plain_foundation(extra),
            "expert": _plain_foundation(expert),
            "beginner_block": dict(extra) if extra else {},
            "expert_block": dict(expert) if expert else {},
            "formulas": " ".join(formula_bits),
            "comparison": cmp_text,
        }

    @staticmethod
    def filter_technologies_by_trl(min_trl: int, max_trl: int) -> dict:
        """Filters technologies within a specific TRL range."""
        return {
            t_id: _with_layers(data)
            for t_id, data in TECHNOLOGIES.items()
            if min_trl <= data.get("trl", 0) <= max_trl
        }

    @staticmethod
    def search_technologies(query: str) -> dict:
        """Searches technologies by keyword across titles, summaries, and use cases."""
        query_lower = query.lower()
        results = {}
        for t_id, data in TECHNOLOGIES.items():
            use_case_text = " ".join(
                uc.get("title", "") + " " + uc.get("description", "")
                if isinstance(uc, dict) else str(uc)
                for uc in data.get("use_cases", [])
            )
            extra = _beginner_copy().get(t_id, {})
            expert = _expert_copy().get(t_id, {})
            depth = _expert_depth().get(t_id, {})
            content_str = (
                f"{data['title']} {data['acronym']} {data['executive_summary']} "
                f"{use_case_text} {extra.get('card', '')} {extra.get('what', '')} "
                f"{expert.get('what', '')} {expert.get('mental_model', '')} "
                f"{depth.get('comparison', {}).get('title', '')}"
            ).lower()
            if query_lower in content_str or any(
                query_lower in part for part in t_id.split("_")
            ):
                results[t_id] = _with_layers(data)
        return results
