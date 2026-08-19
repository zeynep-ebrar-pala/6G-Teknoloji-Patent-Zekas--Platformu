"""
Şartname veritabanı toplamları — yalnızca herkese açık API.
Sayı gelmezse None (UI «—»). HTML kazıyıp çubuk uydurulmaz.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import streamlit as st

from backend.openalex_client import (
    COMBINED_SEARCH,
    TOPIC_SEARCH_QUERIES,
    fetch_publication_trends,
    fetch_topic_yearly_series,
)
from backend.source_links import topic_patent_searches, topic_pub_searches, topic_query

MAILTO = "zeynep.ebrar.pala@example.com"
USER_AGENT = f"6G-Patent-Platform/1.2 (mailto:{MAILTO})"
GP_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "source_totals.json"

CROSSREF_PREFIX = {
    "ieee": "10.1109",
    "springer": "10.1007",
    "elsevier": "10.1016",
}


def _load_disk() -> Dict[str, Any]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _save_disk(payload: Dict[str, Any]) -> None:
    try:
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        CACHE_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        pass


def _cache_get(key: str) -> Optional[int]:
    item = (_load_disk().get("counts") or {}).get(key)
    if isinstance(item, dict) and isinstance(item.get("n"), int):
        return int(item["n"])
    return None


def _cache_put(key: str, n: int) -> None:
    data = _load_disk()
    counts = data.get("counts") or {}
    counts[key] = {
        "n": n,
        "at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }
    data["counts"] = counts
    _save_disk(data)


def _fetch_json(url: str, ua: str, timeout: int = 6) -> Optional[Dict[str, Any]]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": ua, "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, ValueError):
        return None


def _google_patents_total(query: str) -> Optional[int]:
    key = f"gp:{query}"
    cached = _cache_get(key)
    if cached is not None:
        return cached
    inner = f"q={urllib.parse.quote_plus(query)}&num=1"
    url = f"https://patents.google.com/xhr/query?url={urllib.parse.quote(inner)}"
    data = _fetch_json(url, GP_UA, timeout=6)
    if not data:
        return None
    total = (data.get("results") or {}).get("total_num_results")
    if not isinstance(total, int):
        return None
    _cache_put(key, total)
    return total


def _crossref_title_total(query: str, prefix: Optional[str] = None) -> Optional[int]:
    key = f"cr:{prefix or 'all'}:{query}"
    cached = _cache_get(key)
    if cached is not None:
        return cached
    filters = ["from-pub-date:2020", "until-pub-date:2026", "type:journal-article"]
    if prefix:
        filters.append(f"prefix:{prefix}")
    url = (
        "https://api.crossref.org/works"
        f"?query.title={urllib.parse.quote(query)}"
        f"&filter={urllib.parse.quote(','.join(filters), safe=',:.')}"
        "&rows=0"
    )
    data = _fetch_json(url, USER_AGENT, timeout=6)
    if not data:
        return None
    total = (data.get("message") or {}).get("total-results")
    if not isinstance(total, int):
        return None
    _cache_put(key, total)
    return total


def _openalex_topic_total(topic: Optional[str]) -> Optional[int]:
    if topic:
        series = fetch_topic_yearly_series(topic)
        if not series or topic not in series:
            return None
        values = series.get(topic) or []
        if not values:
            return None
        return int(sum(int(v) for v in values))
    trends = fetch_publication_trends()
    if not trends:
        return None
    total = 0
    any_ok = False
    for name in TOPIC_SEARCH_QUERIES:
        vals = trends.get(name)
        if not vals:
            continue
        any_ok = True
        total += sum(int(v) for v in vals)
    return total if any_ok else None


def _search_url(links: List[Dict[str, str]], source_id: str) -> str:
    for item in links:
        if item.get("id") == source_id:
            return str(item.get("url") or "")
    return ""


def _row(source_id: str, url: str, count: Optional[int], method: str) -> Dict[str, Any]:
    return {"id": source_id, "url": url, "count": count, "method": method}


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_patent_source_totals(topic: Optional[str]) -> List[Dict[str, Any]]:
    """Google Patents xhr varsa sayı; Lens/Espacenet/WIPO/USPTO API yok → None."""
    label = topic or "6G"
    query = topic_query(label)
    links = topic_patent_searches(label)
    gp = _google_patents_total(query)
    time.sleep(0.05)
    return [
        _row("google_patents", _search_url(links, "google_patents"), gp, "gp"),
        _row("lens", _search_url(links, "lens"), None, "none"),
        _row("espacenet", _search_url(links, "espacenet"), None, "none"),
        _row("wipo", _search_url(links, "wipo"), None, "none"),
        _row("uspto", _search_url(links, "uspto"), None, "none"),
    ]


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_pub_source_totals(topic: Optional[str]) -> List[Dict[str, Any]]:
    """Crossref önek (IEEE/Springer/Elsevier) + OpenAlex; Scholar/WoS API yok."""
    label = topic or "6G"
    query = topic_query(label) if topic else COMBINED_SEARCH
    links = topic_pub_searches(label)
    oa_url = "https://openalex.org/works"
    rows: List[Dict[str, Any]] = []
    for source_id, prefix in CROSSREF_PREFIX.items():
        n = _crossref_title_total(query, prefix)
        time.sleep(0.12)
        rows.append(_row(source_id, _search_url(links, source_id), n, f"crossref_{source_id}"))
    rows.append(_row("scholar", _search_url(links, "scholar"), None, "none"))
    rows.append(_row("wos", _search_url(links, "wos"), None, "none"))
    rows.append(_row("openalex", oa_url, _openalex_topic_total(topic), "openalex"))
    return rows
