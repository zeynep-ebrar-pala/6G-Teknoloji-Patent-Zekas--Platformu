"""
Akademik yayın analitik servisi — DOI doğrulamalı set her zaman gösterilir.
OpenAlex canlı sayım varsa eklenir; yoksa disk önbelleği (uydurma yok).
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
    fetch_works_by_dois,
    snapshot_meta,
)
from data.academic import ACADEMIC_DATA_SOURCE, ACADEMIC_SOURCES, MOST_CITED_PAPERS


def _papers_raw() -> List[Dict[str, Any]]:
    return load_validated_papers(MOST_CITED_PAPERS)


@st.cache_data(ttl=21600)
def _enriched_papers() -> List[Dict[str, Any]]:
    papers = _papers_raw()
    dois = tuple(p["doi"] for p in papers)
    live_map = fetch_works_by_dois(dois)
    enriched: List[Dict[str, Any]] = []
    for paper in papers:
        merged = dict(paper)
        live = live_map.get(paper["doi"].lower())
        merged["citations"] = None
        merged["citations_live"] = False
        if live:
            merged["citations"] = live.get("citations")
            merged["citations_live"] = True
            if live.get("source_url"):
                merged["source_url"] = live["source_url"]
            if live.get("title"):
                merged["title"] = live["title"]
            merged["institutions"] = live.get("institutions") or []
            merged["countries"] = live.get("countries") or []
        enriched.append(merged)
    return sorted(enriched, key=lambda p: (-int(p.get("year") or 0), -(p.get("citations") or 0)))


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
    meta = snapshot_meta()
    return {
        "total_latest_year": total_latest,
        "latest_year": latest_year,
        "top_topic": top_topic[0],
        "top_topic_count": top_topic[1],
        "top_paper_citations": top_paper_citations,
        "verified_paper_count": len(papers),
        "source": ACADEMIC_DATA_SOURCE,
        "trends_available": trends is not None,
        "snapshot_at": meta.get("fetched_at") or "",
        "openalex_url": meta.get("source_url") or "https://openalex.org/works",
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
    def get_verified_year_counts() -> Dict[str, int]:
        counts = Counter(str(int(p["year"])) for p in _enriched_papers())
        return dict(sorted(counts.items(), key=lambda x: int(x[0])))

    @staticmethod
    def get_verified_topic_counts() -> Dict[str, int]:
        return dict(Counter(p.get("topic") or "Diğer" for p in _enriched_papers()))

    @staticmethod
    def get_verified_institutions() -> List[Dict[str, Any]]:
        counter: Counter = Counter()
        for p in _enriched_papers():
            for inst in p.get("institutions") or []:
                counter[inst] += 1
        return [{"name": n, "count": c} for n, c in counter.most_common(10)]

    @staticmethod
    def get_verified_countries() -> List[Dict[str, Any]]:
        counter: Counter = Counter()
        for p in _enriched_papers():
            for cc in p.get("countries") or []:
                counter[cc] += 1
        return [{"name": n, "count": c} for n, c in counter.most_common(10)]

    @staticmethod
    def get_most_cited_papers() -> List[Dict[str, Any]]:
        return _enriched_papers()

    @staticmethod
    def get_top_institutions() -> Optional[List[Dict[str, Any]]]:
        return fetch_top_institutions()

    @staticmethod
    def get_top_countries() -> Optional[List[Dict[str, Any]]]:
        return fetch_top_countries()
