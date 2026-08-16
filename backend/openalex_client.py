"""
OpenAlex API istemcisi — az istek, disk önbelleği, uydurma sayı yok.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import streamlit as st

OPENALEX_BASE = "https://api.openalex.org"
MAILTO = "zeynep.ebrar.pala@example.com"
USER_AGENT = f"6G-Patent-Platform/1.1 (mailto:{MAILTO})"

TOPIC_SEARCH_QUERIES: Dict[str, str] = {
    "ISAC": "integrated sensing communication wireless",
    "RIS": "reconfigurable intelligent surface wireless",
    "NTN": "non-terrestrial network satellite 5G",
    "AI-RAN": "O-RAN machine learning radio access network",
    "THz": "terahertz communication wireless",
    "Ambient IoT": "ambient IoT backscatter wireless",
}

TREND_YEARS = list(range(2020, 2026))

CACHE_PATH = Path(__file__).resolve().parents[1] / "data" / "cache" / "openalex_snapshot.json"

COMBINED_SEARCH = (
    "integrated sensing communication OR reconfigurable intelligent surface "
    "OR non-terrestrial network satellite OR terahertz communication wireless "
    "OR ambient IoT backscatter OR O-RAN machine learning"
)


def _with_mailto(url: str) -> str:
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}mailto={urllib.parse.quote(MAILTO)}"


def _fetch_json(url: str, timeout: int = 25, retries: int = 4) -> Optional[Dict[str, Any]]:
    req = urllib.request.Request(_with_mailto(url), headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(min(8, 2 ** attempt + 1))
                continue
            return None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt < retries - 1:
                time.sleep(1)
                continue
            return None
    return None


def _load_disk_cache() -> Dict[str, Any]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def _save_disk_cache(payload: Dict[str, Any]) -> None:
    try:
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        CACHE_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError:
        pass


def snapshot_meta() -> Dict[str, str]:
    cache = _load_disk_cache()
    return {
        "fetched_at": str(cache.get("fetched_at") or ""),
        "source_url": str(cache.get("source_url") or "https://openalex.org"),
    }


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_works_by_dois(dois: Tuple[str, ...]) -> Dict[str, Dict[str, Any]]:
    """Birden fazla DOI'yi tek OpenAlex isteğinde çeker."""
    if not dois:
        return {}
    clean = [
        d.strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
        for d in dois
        if d
    ]
    joined = "|".join(urllib.parse.quote(d, safe="") for d in clean)
    url = f"{OPENALEX_BASE}/works?filter=doi:{joined}&per-page=50"
    data = _fetch_json(url)
    out: Dict[str, Dict[str, Any]] = {}
    if not data or "results" not in data:
        cache = _load_disk_cache().get("works_by_doi") or {}
        return {k: v for k, v in cache.items() if k in [c.lower() for c in clean]}
    for item in data["results"]:
        doi = (item.get("doi") or "").replace("https://doi.org/", "").replace("http://doi.org/", "")
        if not doi:
            continue
        landing = (item.get("primary_location") or {}).get("landing_page_url") or f"https://doi.org/{doi}"
        institutions = []
        countries = []
        for auth in item.get("authorships") or []:
            for inst in auth.get("institutions") or []:
                name = inst.get("display_name")
                if name:
                    institutions.append(name)
                cc = inst.get("country_code")
                if cc:
                    countries.append(cc)
        out[doi.lower()] = {
            "title": item.get("title") or "",
            "citations": int(item.get("cited_by_count") or 0),
            "source_url": landing,
            "institutions": institutions,
            "countries": countries,
            "year": item.get("publication_year") or 0,
        }
    if out:
        cache = _load_disk_cache()
        cache["works_by_doi"] = {**(cache.get("works_by_doi") or {}), **out}
        cache["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        cache["source_url"] = "https://openalex.org/works"
        _save_disk_cache(cache)
    return out


@st.cache_data(ttl=86400, show_spinner=False)
def fetch_work_by_doi(doi: str) -> Optional[Dict[str, Any]]:
    batch = fetch_works_by_dois((doi,))
    key = doi.strip().removeprefix("https://doi.org/").lower()
    hit = batch.get(key)
    if not hit:
        return None
    return {
        "title": hit["title"],
        "citations": hit["citations"],
        "source_url": hit["source_url"],
        "doi": key,
        "source": "OpenAlex / Crossref",
        "year": hit.get("year") or 0,
        "authors": "",
        "journal": "",
        "openalex_id": "",
    }


def _fetch_topic_yearly_counts(search: str) -> Optional[Dict[int, int]]:
    year_filter = "|".join(str(y) for y in TREND_YEARS)
    q = urllib.parse.quote(search)
    url = (
        f"{OPENALEX_BASE}/works?search={q}"
        f"&filter=publication_year:{year_filter}"
        f"&group_by=publication_year&per-page=200"
    )
    data = _fetch_json(url)
    if not data or "group_by" not in data:
        return None
    counts: Dict[int, int] = {}
    for bucket in data["group_by"]:
        key = bucket.get("key")
        if key is not None:
            counts[int(key)] = int(bucket.get("count", 0))
    return counts


def _parse_group_by(data: Optional[Dict[str, Any]], limit: int) -> Optional[List[Dict[str, Any]]]:
    if not data or "group_by" not in data:
        return None
    rows: List[Dict[str, Any]] = []
    for bucket in data["group_by"]:
        key = bucket.get("key")
        if not key or str(key).lower() in ("unknown", "null"):
            continue
        name = bucket.get("key_display_name") or str(key).split("/")[-1]
        rows.append({"name": name, "count": int(bucket.get("count", 0)), "key": str(key)})
    rows.sort(key=lambda r: r["count"], reverse=True)
    return rows[:limit]


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_publication_trends() -> Optional[Dict[str, List[int]]]:
    """Konu bazlı yıllık sayım. Tek konu düşerse diğerleri korunur; hepsi düşerse disk önbelleği."""
    result: Dict[str, List[int]] = {"Years": TREND_YEARS}
    any_ok = False
    for topic, query in TOPIC_SEARCH_QUERIES.items():
        yearly = _fetch_topic_yearly_counts(query)
        if yearly is None:
            continue
        result[topic] = [yearly.get(year, 0) for year in TREND_YEARS]
        any_ok = True
        time.sleep(0.2)
    if any_ok:
        cache = _load_disk_cache()
        cache["trends"] = result
        cache["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        cache["source_url"] = "https://openalex.org/works"
        _save_disk_cache(cache)
        return result
    cached = _load_disk_cache().get("trends")
    return cached if cached and "Years" in cached else None


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_topic_yearly_series(topic: str) -> Optional[Dict[str, List[int]]]:
    query = TOPIC_SEARCH_QUERIES.get(topic)
    if not query:
        return None
    yearly = _fetch_topic_yearly_counts(query)
    if yearly is None:
        cached = (_load_disk_cache().get("trends") or {}).get(topic)
        years = (_load_disk_cache().get("trends") or {}).get("Years") or TREND_YEARS
        if cached:
            return {"Years": years, topic: cached}
        return None
    return {"Years": TREND_YEARS, topic: [yearly.get(year, 0) for year in TREND_YEARS]}


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_top_institutions(limit: int = 10) -> Optional[List[Dict[str, Any]]]:
    year_filter = "|".join(str(y) for y in TREND_YEARS)
    q = urllib.parse.quote(COMBINED_SEARCH)
    url = (
        f"{OPENALEX_BASE}/works?search={q}"
        f"&filter=publication_year:{year_filter}"
        f"&group_by=authorships.institutions.id&per-page=200"
    )
    rows = _parse_group_by(_fetch_json(url), limit)
    if rows:
        cache = _load_disk_cache()
        cache["institutions"] = rows
        cache["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        cache["source_url"] = "https://openalex.org/works"
        _save_disk_cache(cache)
        return rows
    return _load_disk_cache().get("institutions")


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_top_countries(limit: int = 10) -> Optional[List[Dict[str, Any]]]:
    year_filter = "|".join(str(y) for y in TREND_YEARS)
    q = urllib.parse.quote(COMBINED_SEARCH)
    url = (
        f"{OPENALEX_BASE}/works?search={q}"
        f"&filter=publication_year:{year_filter}"
        f"&group_by=authorships.institutions.country_code&per-page=200"
    )
    rows = _parse_group_by(_fetch_json(url), limit)
    if rows:
        cache = _load_disk_cache()
        cache["countries"] = rows
        cache["fetched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        cache["source_url"] = "https://openalex.org/works"
        _save_disk_cache(cache)
        return rows
    return _load_disk_cache().get("countries")
