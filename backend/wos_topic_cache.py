"""
WoS (Web of Science — Web of Science) Core Collection konu önbelleği.

Kaynak: oturum açık Analyze Results + Times Cited. Starter API değildir.
Konu serileri toplanmaz (aynı makale birden fazla TS sorgusunda çıkar).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from backend.wos_live import TOPIC_ORDER, live_topic_row, load_live

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "wos_topics.json"
TREND_YEARS = list(range(2020, 2027))
LAST5_YEARS = list(range(2022, 2027))

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
    "TURKEY": "TR",
    "TURKIYE": "TR",
    "TÜRKIYE": "TR",
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
    out.sort(key=lambda r: (-int(r["count"]), str(r["name"])))
    return out


def _countries(row: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Analyze Results ilk 10. Eşleşmeyen ad atılmaz — sıra kaymasın."""
    out: List[Dict[str, Any]] = []
    for item in row.get("countries") or []:
        if not isinstance(item, dict):
            continue
        raw_name = str(item.get("name") or "").strip()
        if not raw_name:
            continue
        cc = WOS_COUNTRY_CC.get(raw_name.upper()) or ""
        try:
            count = int(item.get("count"))
        except (TypeError, ValueError):
            continue
        out.append({"cc": cc, "name": raw_name, "count": count})
    out.sort(key=lambda r: (-int(r["count"]), str(r.get("cc") or r.get("name") or "")))
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


def _merge_topic_row(name: str, cache_row: Dict[str, Any], live_row: Dict[str, Any]) -> Dict[str, Any]:
    row = dict(cache_row or {})
    if isinstance(live_row.get("total"), int):
        row["total"] = int(live_row["total"])
        row["query"] = str(live_row.get("query") or row.get("query") or "")
    live_years = live_row.get("years") if isinstance(live_row.get("years"), dict) else {}
    if live_years:
        row["years"] = live_years
    if live_row.get("cited"):
        row["cited"] = live_row["cited"]
    if live_row.get("countries"):
        row["countries"] = live_row["countries"]
    if live_row.get("institutions") and not _institutions(row):
        row["institutions"] = live_row["institutions"]
    if live_row.get("institutions") and name == "Cell-Free":
        row["institutions"] = live_row["institutions"]
    for key in ("turkey_count", "turkey_rank", "roster"):
        if live_row.get(key) is not None:
            row[key] = live_row[key]
    return row


def wos_overlay(topic: Optional[str]) -> Optional[Dict[str, Any]]:
    """Grafik katmanı. Canlı Starter varsa o; yoksa Analyze önbelleği. Sayı uydurulmaz."""
    cache = load_wos_topics()
    live_blob = load_live()
    cache_topics = cache.get("topics") if isinstance(cache.get("topics"), dict) else {}
    topics: Dict[str, Any] = {}
    for name in TOPIC_ORDER:
        base = cache_topics.get(name) if isinstance(cache_topics.get(name), dict) else {}
        live_row = live_topic_row(name)
        merged = _merge_topic_row(name, base, live_row)
        if merged.get("total") is not None or merged.get("years") or merged.get("countries") or merged.get("cited"):
            topics[name] = merged
    if not topics:
        return None

    totals: Dict[str, int] = {}
    series: Dict[str, Dict[str, int]] = {}
    turkey: Dict[str, Dict[str, Any]] = {}
    for name in TOPIC_ORDER:
        row = topics.get(name)
        if not isinstance(row, dict):
            continue
        if isinstance(row.get("total"), int):
            totals[name] = int(row["total"])
        series[name] = _ordered_years(row.get("years") or {})
        turkey[name] = {
            "count": row.get("turkey_count") if isinstance(row.get("turkey_count"), int) else None,
            "rank": row.get("turkey_rank") if isinstance(row.get("turkey_rank"), int) else None,
            "roster": row.get("roster") if isinstance(row.get("roster"), int) else None,
        }

    if not totals:
        return None

    fetched = str(live_blob.get("fetched_at") or cache.get("fetched_at") or "")
    meta = {
        "chart_source": "wos",
        "wos_fetched_at": fetched,
        "wos_filter": str(cache.get("filter") or "TS=(6G) AND konu AND PY=2020-2026"),
        "turkey_by_topic": turkey,
    }
    by_inst: Dict[str, List[Dict[str, Any]]] = {}
    by_cc: Dict[str, List[Dict[str, Any]]] = {}
    for name in TOPIC_ORDER:
        row = topics.get(name)
        if not isinstance(row, dict):
            continue
        inst = _institutions(row)
        cc = _countries(row)
        if inst:
            by_inst[name] = inst
        if cc:
            by_cc[name] = cc

    tpc = (topic or "").strip() or None
    if tpc:
        row = topics.get(tpc) if isinstance(topics.get(tpc), dict) else {}
        return {
            **meta,
            "wos_total": int(row["total"]) if isinstance(row.get("total"), int) else None,
            "wos_query": str(row.get("query") or ""),
            "topics": {tpc: totals[tpc]} if tpc in totals else {},
            "year_counts": series.get(tpc) or {},
            "year_series": {tpc: series[tpc]} if tpc in series else {},
            "institutions": _institutions(row) if row else [],
            "countries": _countries(row) if row else [],
            "institutions_by_topic": {tpc: by_inst[tpc]} if tpc in by_inst else {},
            "countries_by_topic": {tpc: by_cc[tpc]} if tpc in by_cc else {},
            "cited": list(live_topic_row(tpc).get("cited") or []) or _cited(row, tpc),
            "turkey": turkey.get(tpc) or {},
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
        "institutions_by_topic": by_inst,
        "countries_by_topic": by_cc,
        "cited": _merge_cited(topics),
        "turkey": {},
    }
