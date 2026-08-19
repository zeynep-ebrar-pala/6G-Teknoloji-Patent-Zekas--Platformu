"""
Modül 3 literatür sayımı — Türkiye ve Avrupa, başlık 6G, 2020–2026.
IEEE / Springer / Elsevier: DOI öneki. Scholar ve WoS: API yok.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd
import streamlit as st

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "tr_eu_6g.json"
TREND_YEARS = list(range(2020, 2027))

TOPIC_QUERIES: Dict[str, str] = {
    "ISAC": "ISAC",
    "RIS": "RIS",
    "NTN": "NTN",
    "AI-RAN": "O-RAN",
    "THz": "THz",
    "Ambient IoT": "ambient IoT",
}

PUBLISHER_PREFIXES: Dict[str, str] = {
    "ieee": "10.1109",
    "springer": "10.1007",
    "elsevier": "10.1016",
}

EU_AFFIL: Dict[str, str] = {
    "DE": "Germany",
    "FR": "France",
    "IT": "Italy",
    "ES": "Spain",
    "GB": "United Kingdom",
    "FI": "Finland",
    "SE": "Sweden",
    "NL": "Netherlands",
    "BE": "Belgium",
    "AT": "Austria",
    "CH": "Switzerland",
    "NO": "Norway",
    "DK": "Denmark",
    "PL": "Poland",
    "PT": "Portugal",
    "GR": "Greece",
    "IE": "Ireland",
    "CZ": "Czech Republic",
    "HU": "Hungary",
    "RO": "Romania",
    "BG": "Bulgaria",
    "HR": "Croatia",
    "SK": "Slovakia",
    "SI": "Slovenia",
    "LT": "Lithuania",
    "LV": "Latvia",
    "EE": "Estonia",
    "LU": "Luxembourg",
    "MT": "Malta",
    "CY": "Cyprus",
    "IS": "Iceland",
}

TREND_EU = ("DE", "FR", "IT", "ES", "GB", "FI", "GR", "CZ")


def _load_disk() -> Dict[str, Any]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _ordered_years(years: Dict[str, Any]) -> Dict[str, int]:
    out: Dict[str, int] = {}
    for year in TREND_YEARS:
        key = str(year)
        try:
            out[key] = int(years.get(key) or 0)
        except (TypeError, ValueError):
            out[key] = 0
    return out


def snapshot_meta() -> Dict[str, str]:
    cache = _load_disk()
    return {"fetched_at": str(cache.get("fetched_at") or "")}


@st.cache_data(ttl=21600, show_spinner=False)
def literature_bundle(region: str = "both", topic: Optional[str] = None) -> Dict[str, Any]:
    """Türkiye / Avrupa / ikisi. Konu TR konu önbelleğindedir; ülke çubukları 6G başlıktır."""
    cache = _load_disk()
    region = region if region in ("tr", "eu", "both") else "both"
    tpc = (topic or "").strip() or None
    if tpc and tpc not in TOPIC_QUERIES:
        tpc = None

    tr = cache.get("TR") if isinstance(cache.get("TR"), dict) else {}
    eu_map = cache.get("EU_countries") if isinstance(cache.get("EU_countries"), dict) else {}

    tr_total = tr.get("total") if isinstance(tr.get("total"), int) else None
    tr_years = _ordered_years(tr.get("years") or {})
    publishers = tr.get("publishers") if isinstance(tr.get("publishers"), dict) else {}
    topics = tr.get("topics") if isinstance(tr.get("topics"), dict) else {}
    tr_cited = tr.get("top_cited") if isinstance(tr.get("top_cited"), list) else []
    eu_cited = cache.get("EU_top_cited") if isinstance(cache.get("EU_top_cited"), list) else []
    affiliations = tr.get("affiliations") if isinstance(tr.get("affiliations"), dict) else {}

    countries: List[Dict[str, Any]] = []
    if isinstance(tr_total, int):
        countries.append({"cc": "TR", "count": tr_total})
    for cc, row in eu_map.items():
        if isinstance(row, dict) and isinstance(row.get("total"), int):
            countries.append({"cc": cc, "count": int(row["total"])})
    countries.sort(key=lambda r: r["count"], reverse=True)

    year_series: Dict[str, Dict[str, int]] = {"TR": tr_years}
    for cc in TREND_EU:
        row = eu_map.get(cc) or {}
        if isinstance(row, dict) and isinstance(row.get("years"), dict):
            year_series[cc] = _ordered_years(row["years"])

    inst = [
        {"name": name, "count": int(n)}
        for name, n in list(affiliations.items())[:10]
        if isinstance(n, int)
    ]

    topic_counts = {k: int(v) for k, v in topics.items() if isinstance(v, int)}
    if tpc:
        topic_counts = {tpc: topic_counts[tpc]} if tpc in topic_counts else {}

    if region == "tr":
        cited = list(tr_cited)
        year_counts = tr_years
        country_rows = [r for r in countries if r["cc"] == "TR"]
        inst_rows = inst
        pub = {k: publishers.get(k) for k in PUBLISHER_PREFIXES}
        total = tr_total
    elif region == "eu":
        cited = list(eu_cited)
        year_counts = {}
        country_rows = [r for r in countries if r["cc"] != "TR"]
        inst_rows = []
        pub = {"ieee": None, "springer": None, "elsevier": None}
        total = None
        if not tpc:
            topic_counts = {}
    else:
        by_doi: Dict[str, Dict[str, Any]] = {}
        for paper in list(tr_cited) + list(eu_cited):
            doi = str(paper.get("doi") or "").lower()
            if not doi:
                continue
            prev = by_doi.get(doi)
            if prev is None or int(paper.get("citations") or 0) > int(prev.get("citations") or 0):
                by_doi[doi] = paper
        cited = sorted(by_doi.values(), key=lambda p: -int(p.get("citations") or 0))[:10]
        year_counts = tr_years
        country_rows = countries
        inst_rows = inst
        pub = {k: publishers.get(k) for k in PUBLISHER_PREFIXES}
        total = tr_total

    return {
        "region": region,
        "topic": tpc,
        "total_tr": tr_total,
        "total": total,
        "year_counts": year_counts,
        "year_series": year_series,
        "countries": country_rows,
        "institutions": inst_rows,
        "topics": topic_counts,
        "publishers": pub,
        "cited": cited,
        "source": (
            "IEEE / Springer / Elsevier: DOI öneki + bağlılık ülkesi, başlık 6G, "
            "2020–2026 dergi ve bildiri. Scholar ve WoS sayım API’si yok."
        ),
        **snapshot_meta(),
    }


def country_year_df(region: str = "both") -> Optional[pd.DataFrame]:
    bundle = literature_bundle(region, None)
    series: Dict[str, Dict[str, int]] = bundle.get("year_series") or {}
    if region == "tr":
        keep = ["TR"]
    elif region == "eu":
        keep = [cc for cc in TREND_EU if cc in series]
    else:
        keep = ["TR"] + [cc for cc in TREND_EU if cc in series]
    if not keep:
        return None
    data: Dict[str, List[int]] = {"Years": list(TREND_YEARS)}
    for cc in keep:
        years = series.get(cc) or {}
        data[cc] = [int(years.get(str(y), 0) or 0) for y in TREND_YEARS]
    return pd.DataFrame(data)
