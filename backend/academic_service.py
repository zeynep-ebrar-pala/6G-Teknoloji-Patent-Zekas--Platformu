"""
Modül 3 — Türkiye ve Avrupa 6G yayın analitiği.
Kilitli örnek liste çizilmez. Scholar/WoS sayısı uydurulmaz.
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
from backend.wos_topic_cache import load_wos_topics
from data.academic import ACADEMIC_DATA_SOURCE, ACADEMIC_SOURCES


def _norm_topic(topic: Optional[str]) -> Optional[str]:
    if not topic or topic in ("all", "Tümü", "All"):
        return None
    return topic


def _wos_fp() -> str:
    return str(load_wos_topics().get("fetched_at") or "")


class AcademicService:
    """Şartname Modül 3 servis katmanı."""

    @staticmethod
    def get_sources() -> List[str]:
        return ACADEMIC_SOURCES

    @staticmethod
    def get_data_source() -> str:
        return ACADEMIC_DATA_SOURCE

    @staticmethod
    def get_bundle(region: str = "both", topic: Optional[str] = None) -> Dict[str, Any]:
        from backend.wos_live import ensure_prefetch, load_live

        ensure_prefetch()
        live_at = str(load_live().get("fetched_at") or "")
        return literature_bundle(region, _norm_topic(topic), key_fingerprint(), _wos_fp(), "cc3", live_at)

    @staticmethod
    def get_summary(topic: Optional[str] = None) -> Dict[str, Any]:
        from backend.wos_live import ensure_prefetch, load_live

        ensure_prefetch()
        live_at = str(load_live().get("fetched_at") or "")
        bundle = literature_bundle("both", _norm_topic(topic), key_fingerprint(), _wos_fp(), "cc3", live_at)
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
            "literature_total": bundle.get("total_tr"),
            "peak_year": peak_year,
            "peak_n": peak_n,
            "top_topic": top_topic,
            "top_topic_count": top_n,
            "verified_paper_count": len(bundle.get("cited") or []),
            "source": ACADEMIC_DATA_SOURCE,
            "snapshot_at": meta.get("fetched_at") or "",
        }

    @staticmethod
    def get_tech_publication_trends_df(topic: Optional[str] = None) -> Optional[pd.DataFrame]:
        return country_year_df("tr", _norm_topic(topic))

    @staticmethod
    def get_topic_yearly_df(topic: str) -> Optional[pd.DataFrame]:
        df = country_year_df("tr", _norm_topic(topic))
        if df is None or df.empty:
            return None
        if "TR" in df.columns:
            return df.rename(columns={"TR": topic or "6G"})
        return df

    @staticmethod
    def get_most_cited_papers(topic: Optional[str] = None) -> List[Dict[str, Any]]:
        from backend.wos_live import load_live

        live_at = str(load_live().get("fetched_at") or "")
        return list(
            literature_bundle("both", _norm_topic(topic), key_fingerprint(), _wos_fp(), "cc3", live_at).get("cited")
            or []
        )

    @staticmethod
    def get_trend_df(region: str = "both", topic: Optional[str] = None) -> Optional[pd.DataFrame]:
        return country_year_df(region, _norm_topic(topic))
