"""
Akademik yayın analitik servisi — OpenAlex canlı veri + DOI doğrulamalı makale seti.
Atıf sayıları yalnızca OpenAlex cited_by_count; API yoksa None (uydurma yok).
"""

from __future__ import annotations

from collections import Counter
from typing import Any, Dict, List, Optional

import pandas as pd
import streamlit as st

from backend.data_validator import load_validated_papers
from backend.openalex_client import (
    TREND_YEARS,
    fetch_publication_trends,
    fetch_top_countries,
    fetch_top_institutions,
    fetch_topic_yearly_series,
    fetch_work_by_doi,
)
from data.academic import ACADEMIC_DATA_SOURCE, ACADEMIC_SOURCES, MOST_CITED_PAPERS


def _papers_raw() -> List[Dict[str, Any]]:
    return load_validated_papers(MOST_CITED_PAPERS)


@st.cache_data(ttl=3600)
def _enriched_papers() -> List[Dict[str, Any]]:
    """DOI doğrulamalı makaleleri OpenAlex ile zenginleştirir."""
    enriched: List[Dict[str, Any]] = []
    for paper in _papers_raw():
        live = fetch_work_by_doi(paper["doi"])
        merged = dict(paper)
        merged["citations"] = None
        merged["citations_live"] = False
        if live:
            merged["citations"] = live.get("citations")
            merged["citations_live"] = True
            if live.get("source_url"):
                merged["source_url"] = live["source_url"]
            if live.get("title"):
                merged["title"] = live["title"]
        enriched.append(merged)
    return sorted(enriched, key=lambda p: p.get("citations") or 0, reverse=True)


def _compute_summary() -> Dict[str, Any]:
    papers = _enriched_papers()
    trends = fetch_publication_trends()
    total_latest = None
    top_topic = ("—", 0)
    latest_year = TREND_YEARS[-1] if TREND_YEARS else None
    if trends and "Years" in trends:
        latest_idx = len(trends["Years"]) - 1
        latest_year = trends["Years"][latest_idx]
        topic_counts = {
            t: trends[t][latest_idx]
            for t in trends
            if t != "Years" and trends[t]
        }
        if topic_counts:
            total_latest = sum(topic_counts.values())
            top_topic = max(topic_counts.items(), key=lambda x: x[1])

    live_cited = [p for p in papers if p.get("citations_live") and isinstance(p.get("citations"), int)]
    top_paper_citations = max((p["citations"] for p in live_cited), default=None)
    return {
        "total_latest_year": total_latest,
        "latest_year": latest_year,
        "top_topic": top_topic[0],
        "top_topic_count": top_topic[1],
        "top_paper_citations": top_paper_citations,
        "verified_paper_count": len(papers),
        "source": ACADEMIC_DATA_SOURCE,
        "trends_available": trends is not None,
    }


class AcademicService:
    """Akademik literatür servis katmanı."""

    @staticmethod
    def get_sources() -> List[str]:
        return ACADEMIC_SOURCES

    @staticmethod
    def get_data_source() -> str:
        return ACADEMIC_DATA_SOURCE

    @staticmethod
    def get_summary() -> Dict[str, Any]:
        return _compute_summary()

    @staticmethod
    def get_tech_publication_trends_df() -> Optional[pd.DataFrame]:
        trends = fetch_publication_trends()
        if not trends:
            return None
        return pd.DataFrame(trends)

    @staticmethod
    def get_topic_yearly_df(topic: str) -> Optional[pd.DataFrame]:
        series = fetch_topic_yearly_series(topic)
        if not series:
            return None
        return pd.DataFrame(series)

    @staticmethod
    def get_database_distribution() -> Dict[str, int]:
        return dict(Counter(p.get("source", "Diğer") for p in _enriched_papers()))

    @staticmethod
    def get_most_cited_papers() -> List[Dict[str, Any]]:
        return _enriched_papers()

    @staticmethod
    def get_top_institutions() -> Optional[List[Dict[str, Any]]]:
        return fetch_top_institutions()

    @staticmethod
    def get_top_countries() -> Optional[List[Dict[str, Any]]]:
        return fetch_top_countries()
