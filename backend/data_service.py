"""
Türk Telekom 6G Platform - Backend Data Service Layer
Statik sözlük önbelleğe alınmaz: beginner ve uzman derinlik metinleri anında birleşir.
"""

from data.beginner_copy import BEGINNER_COPY
from data.expert_depth import EXPERT_DEPTH
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


def _with_layers(tech: dict | None) -> dict | None:
    if not tech:
        return tech
    extra = BEGINNER_COPY.get(tech.get("id"), {})
    depth = EXPERT_DEPTH.get(tech.get("id"), {})
    out = dict(tech)
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
    foundation = {k: extra.get(k) for k in FOUNDATION_KEYS if extra.get(k) is not None}
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
            item = dict(uc) if isinstance(uc, dict) else {"title": f"Senaryo #{idx+1}", "description": str(uc)}
            if idx < len(extras) and isinstance(extras[idx], dict):
                item["how"] = extras[idx].get("how", "")
                item["when_not"] = extras[idx].get("when_not", "")
            merged_uc.append(item)
        out["use_cases"] = merged_uc
    return out


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
            extra = BEGINNER_COPY.get(t_id, {})
            depth = EXPERT_DEPTH.get(t_id, {})
            content_str = (
                f"{data['title']} {data['acronym']} {data['executive_summary']} "
                f"{use_case_text} {extra.get('card', '')} {extra.get('what', '')} "
                f"{depth.get('comparison', {}).get('title', '')}"
            ).lower()
            if query_lower in content_str or any(
                query_lower in part for part in t_id.split("_")
            ):
                results[t_id] = _with_layers(data)
        return results
