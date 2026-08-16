"""
Türk Telekom 6G Platform - Backend Data Service Layer
Statik sözlük önbelleğe alınmaz: beginner metinleri güncellenince kartlarda None kalmasın.
"""

from data.beginner_copy import BEGINNER_COPY
from data.technologies import TECHNOLOGIES


def _with_beginner(tech: dict | None) -> dict | None:
    if not tech:
        return tech
    extra = BEGINNER_COPY.get(tech.get("id"), {})
    out = dict(tech)
    card = extra.get("card")
    if card:
        out["beginner_card"] = card
        out["beginner_one_liner"] = card
    if extra.get("kicker"):
        out["beginner_kicker"] = extra["kicker"]
    if extra.get("teach_html"):
        out["beginner_teach"] = extra["teach_html"]
    if extra.get("principle_html"):
        out["beginner_principle"] = extra["principle_html"]
    if extra.get("arch_html"):
        out["beginner_arch"] = extra["arch_html"]
    return out


class DataService:
    """Backend Data Access Service for 6G Knowledge Base."""

    @staticmethod
    def get_all_technologies() -> dict:
        """Returns all 7 6G technologies with beginner teaching copy merged."""
        return {t_id: _with_beginner(data) for t_id, data in TECHNOLOGIES.items()}

    @staticmethod
    def get_technology_by_id(tech_id: str) -> dict:
        """Retrieves a specific technology by its unique ID."""
        return _with_beginner(TECHNOLOGIES.get(tech_id))

    @staticmethod
    def filter_technologies_by_trl(min_trl: int, max_trl: int) -> dict:
        """Filters technologies within a specific TRL range."""
        return {
            t_id: _with_beginner(data)
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
            content_str = (
                f"{data['title']} {data['acronym']} {data['executive_summary']} "
                f"{use_case_text} {extra.get('card', '')}"
            ).lower()
            if query_lower in content_str or any(
                query_lower in part for part in t_id.split("_")
            ):
                results[t_id] = _with_beginner(data)
        return results
