"""
WoS (Web of Science — Web of Science) Core Collection konu önbelleği.

Kaynak: oturum açık Analyze Results + Times Cited. Starter API değildir.
Konu serileri toplanmaz (aynı makale birden fazla TS sorgusunda çıkar).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "wos_topics.json"
TREND_YEARS = list(range(2020, 2027))
TOPIC_ORDER = ("ISAC", "RIS", "NTN", "AI-RAN", "THz", "Ambient IoT")

# WoS Analyze Results ülke adı → ISO 3166-1 alpha-2.
# ENGLAND, WoS’ta UK’nin İngiltere dilimidir; İskoçya ayrı satır olabilir.
WOS_COUNTRY_CC = {
    "PEOPLES R CHINA": "CN",
    "USA": "US",
    "ENGLAND": "GB",
    "GERMANY": "DE",
    "SOUTH KOREA": "KR",
    "CANADA": "CA",
    "AUSTRALIA": "AU",
    "SINGAPORE": "SG",
    "SWEDEN": "SE",
    "INDIA": "IN",
    "ITALY": "IT",
    "JAPAN": "JP",
    "SPAIN": "ES",
    "SAUDI ARABIA": "SA",
    "FRANCE": "FR",
    "FINLAND": "FI",
    "GREECE": "GR",
    "EGYPT": "EG",
}


def _ordered_years(years: Dict[str, Any]) -> Dict[str, int]:
    out: Dict[str, int] = {}
    for year in TREND_YEARS:
        key = str(year)
        try:
            out[key] = int(years.get(key) or 0)
        except (TypeError, ValueError):
            out[key] = 0
    return out


def load_wos_topics() -> Dict[str, Any]:
    if not CACHE_PATH.exists():
        return {}
    try:
        data = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def _institutions(row: Dict[str, Any]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for item in row.get("institutions") or []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name") or "").strip()
        try:
            count = int(item.get("count"))
        except (TypeError, ValueError):
            continue
        if name and count >= 0:
            out.append({"name": name, "count": count})
    return out


def _countries(row: Dict[str, Any]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for item in row.get("countries") or []:
        if not isinstance(item, dict):
            continue
        raw = str(item.get("name") or "").strip().upper()
        cc = WOS_COUNTRY_CC.get(raw)
        if not cc:
            continue
        try:
            count = int(item.get("count"))
        except (TypeError, ValueError):
            continue
        out.append({"cc": cc, "count": count})
    return out


def _cited(row: Dict[str, Any], topic: str) -> List[Dict[str, Any]]:
    from backend.data_validator import load_validated_papers

    raw: List[Dict[str, Any]] = []
    for paper in row.get("cited") or []:
        if not isinstance(paper, dict):
            continue
        doi = str(paper.get("doi") or "").strip().lower()
        doi = doi.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
        if not doi.startswith("10."):
            continue
        url = f"https://doi.org/{doi}"
        raw.append(
            {
                "title": paper.get("title") or "",
                "authors": paper.get("authors") or "",
                "journal": paper.get("journal") or "",
                "year": paper.get("year"),
                "doi": doi,
                "citations": paper.get("citations"),
                "source": "Web of Science Core Collection",
                "source_url": url,
                "url": url,
                "topic": topic,
                "wos_ut": str(paper.get("wos_ut") or "").strip(),
            }
        )
    validated = load_validated_papers(raw)
    ut_by_doi = {p["doi"]: p.get("wos_ut") or "" for p in raw}
    for item in validated:
        item["wos_ut"] = ut_by_doi.get(item["doi"], "")
    return validated


def _merge_cited(topics: Dict[str, Any]) -> List[Dict[str, Any]]:
    by_doi: Dict[str, Dict[str, Any]] = {}
    for name in TOPIC_ORDER:
        row = topics.get(name)
        if not isinstance(row, dict):
            continue
        for paper in _cited(row, name):
            doi = str(paper.get("doi") or "").lower()
            if not doi:
                continue
            prev = by_doi.get(doi)
            if prev is None or int(paper.get("citations") or 0) > int(prev.get("citations") or 0):
                by_doi[doi] = paper
    return sorted(by_doi.values(), key=lambda p: -int(p.get("citations") or 0))[:10]


def wos_overlay(topic: Optional[str]) -> Optional[Dict[str, Any]]:
    """Grafik katmanı. Yoksa None — sayı uydurulmaz."""
    cache = load_wos_topics()
    topics = cache.get("topics") if isinstance(cache.get("topics"), dict) else {}
    if not topics:
        return None

    totals: Dict[str, int] = {}
    series: Dict[str, Dict[str, int]] = {}
    for name in TOPIC_ORDER:
        row = topics.get(name)
        if not isinstance(row, dict):
            continue
        if isinstance(row.get("total"), int):
            totals[name] = int(row["total"])
        series[name] = _ordered_years(row.get("years") or {})

    if not totals:
        return None

    meta = {
        "chart_source": "wos",
        "wos_fetched_at": str(cache.get("fetched_at") or ""),
        "wos_filter": str(cache.get("filter") or ""),
    }
    tpc = (topic or "").strip() or None
    if tpc and tpc in topics and isinstance(topics[tpc], dict):
        row = topics[tpc]
        return {
            **meta,
            "wos_total": int(row["total"]) if isinstance(row.get("total"), int) else None,
            "wos_query": str(row.get("query") or ""),
            "topics": {tpc: totals[tpc]} if tpc in totals else {},
            "year_counts": series.get(tpc) or {},
            "year_series": {tpc: series[tpc]} if tpc in series else {},
            "institutions": _institutions(row),
            "countries": _countries(row),
            "cited": _cited(row, tpc),
        }

    return {
        **meta,
        "wos_total": None,
        "wos_query": str(cache.get("filter") or ""),
        "topics": totals,
        "year_counts": {},
        "year_series": series,
        "institutions": [],
        "countries": [],
        "cited": _merge_cited(topics),
    }
