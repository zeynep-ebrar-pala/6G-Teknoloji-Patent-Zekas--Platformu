"""
Modül 3 — Türkiye ve Avrupa 6G yayın analitiği.
Kilitli örnek liste çizilmez. Springer sayısı uydurulmaz.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import pandas as pd

from backend.literature_client import (
    country_year_df,
    literature_bundle,
    snapshot_meta,
)
from backend.publisher_apis import key_fingerprint
from backend.springer_live import load_live
from data.academic import ACADEMIC_SOURCES, academic_data_source


def _norm_topic(topic: Optional[str]) -> Optional[str]:
    if not topic or topic in ("all", "Tümü", "All"):
        return None
    return topic


def _live_fp() -> str:
    from backend.openalex_inst import load_live as oa_live

    return f"{load_live().get('fetched_at') or ''}|{oa_live().get('fetched_at') or ''}"


class AcademicService:
    """Şartname Modül 3 servis katmanı."""

    @staticmethod
    def get_sources() -> List[str]:
        return ACADEMIC_SOURCES

    @staticmethod
    def get_data_source() -> str:
        return academic_data_source()

    @staticmethod
    def get_bundle(region: str = "both", topic: Optional[str] = None) -> Dict[str, Any]:
        return literature_bundle(region, _norm_topic(topic), key_fingerprint(), "sp4", _live_fp())

    @staticmethod
    def get_summary(topic: Optional[str] = None) -> Dict[str, Any]:
        bundle = literature_bundle("both", _norm_topic(topic), key_fingerprint(), "sp4", _live_fp())
        meta = snapshot_meta()
        years = bundle.get("year_counts") or {}
        peak_year, peak_n = "—", None
        if years:
            peak_year = max(years, key=lambda y: years[y])
            peak_n = years[peak_year]
        topics = bundle.get("topics") or {}
        top_topic, top_n = "—", None
        if topics:
            top_topic = max(topics, key=topics.get)
            top_n = topics[top_topic]
        return {
            "literature_total": bundle.get("total"),
            "peak_year": peak_year,
            "peak_n": peak_n,
            "top_topic": top_topic,
            "top_topic_count": top_n,
            "verified_paper_count": len(bundle.get("cited") or []),
            "source": academic_data_source(),
            "snapshot_at": meta.get("fetched_at") or bundle.get("fetched_at") or "",
        }

    @staticmethod
    def get_tech_publication_trends_df(topic: Optional[str] = None) -> Optional[pd.DataFrame]:
        return country_year_df("tr", _norm_topic(topic))

    @staticmethod
    def get_topic_yearly_df(topic: str) -> Optional[pd.DataFrame]:
        """Springer Nature Meta year facet. Overlay yoksa None — Crossref yedek yok."""
        from backend.springer_live import ensure_prefetch, live_topic_row
        from backend.years import trend_years

        name = _norm_topic(topic)
        if not name:
            return None
        ensure_prefetch()
        row = live_topic_row(name)
        years = row.get("years") if isinstance(row.get("years"), dict) else {}
        axis = [y for y in trend_years() if isinstance(years.get(str(y)), int)]
        if not axis:
            return None
        return pd.DataFrame({"Years": axis, name: [int(years[str(y)]) for y in axis]})

    @staticmethod
    def get_most_cited_papers(topic: Optional[str] = None) -> List[Dict[str, Any]]:
        return list(
            literature_bundle("both", _norm_topic(topic), key_fingerprint(), "sp4", _live_fp()).get("cited") or []
        )

    @staticmethod
    def get_trend_df(region: str = "both", topic: Optional[str] = None) -> Optional[pd.DataFrame]:
        return country_year_df(region, _norm_topic(topic))
