"""
OpenAlex API istemcisi — yalnızca doğrulanabilir akademik metadata.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional

import streamlit as st

OPENALEX_BASE = "https://api.openalex.org"
USER_AGENT = "6G-Patent-Platform/1.0 (mailto:zeynep.ebrar.pala@example.com)"

TOPIC_SEARCH_QUERIES: Dict[str, str] = {
    "ISAC": "integrated sensing communication wireless",
    "RIS": "reconfigurable intelligent surface wireless",
    "NTN": "non-terrestrial network satellite 5G",
    "AI-RAN": "O-RAN machine learning radio access network",
    "THz": "terahertz communication wireless",
    "Ambient IoT": "ambient IoT backscatter wireless",
}

TREND_YEARS = list(range(2020, 2026))


def _fetch_json(url: str, timeout: int = 30, retries: int = 3) -> Optional[Dict[str, Any]]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < retries - 1:
                time.sleep(2 ** attempt + 1)
                continue
            return None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt < retries - 1:
                time.sleep(1)
                continue
            return None
    return None


@st.cache_data(ttl=86400, show_spinner=False)
def fetch_work_by_doi(doi: str) -> Optional[Dict[str, Any]]:
    """DOI ile OpenAlex'ten doğrulanmış makale metadata'sı."""
    doi_clean = doi.strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    url = f"{OPENALEX_BASE}/works/https://doi.org/{urllib.parse.quote(doi_clean)}"
    data = _fetch_json(url)
    if not data or not data.get("title"):
        return None
    landing = (data.get("primary_location") or {}).get("landing_page_url") or f"https://doi.org/{doi_clean}"
    return {
        "title": data["title"],
        "authors": ", ".join(
            a.get("author", {}).get("display_name", "")
            for a in data.get("authorships", [])[:6]
            if a.get("author")
        ),
        "journal": (data.get("primary_location") or {}).get("source", {}).get("display_name", ""),
        "year": data.get("publication_year") or 0,
        "citations": int(data.get("cited_by_count") or 0),
        "doi": doi_clean,
        "source": "OpenAlex / Crossref",
        "source_url": landing,
        "openalex_id": data.get("id", "").split("/")[-1],
    }


@st.cache_data(ttl=86400, show_spinner=False)
def _fetch_topic_yearly_counts(search: str) -> Optional[Dict[int, int]]:
    """Tek konu için yıllık sayım — group_by ile tek API çağrısı."""
    year_filter = "|".join(str(y) for y in TREND_YEARS)
    q = urllib.parse.quote(search)
    url = (
        f"{OPENALEX_BASE}/works?search={q}"
        f"&filter=publication_year:{year_filter}"
        f"&group_by=publication_year&per_page=200"
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


@st.cache_data(ttl=86400, show_spinner=False)
def fetch_publication_trends() -> Optional[Dict[str, List[int]]]:
    """Tüm konular için yıllık yayın trendi — OpenAlex group_by (6 istek)."""
    result: Dict[str, List[int]] = {"Years": TREND_YEARS}
    for topic, query in TOPIC_SEARCH_QUERIES.items():
        yearly = _fetch_topic_yearly_counts(query)
        if yearly is None:
            return None
        result[topic] = [yearly.get(year, 0) for year in TREND_YEARS]
        time.sleep(0.5)
    return result


COMBINED_SEARCH = (
    "integrated sensing communication OR reconfigurable intelligent surface "
    "OR non-terrestrial network satellite OR terahertz communication wireless "
    "OR ambient IoT backscatter OR O-RAN machine learning"
)


@st.cache_data(ttl=86400, show_spinner=False)
def fetch_topic_yearly_series(topic: str) -> Optional[Dict[str, List[int]]]:
    """Tek konu için yıllık OpenAlex sayımı. Konu yoksa veya API düşerse None."""
    query = TOPIC_SEARCH_QUERIES.get(topic)
    if not query:
        return None
    yearly = _fetch_topic_yearly_counts(query)
    if yearly is None:
        return None
    return {"Years": TREND_YEARS, topic: [yearly.get(year, 0) for year in TREND_YEARS]}


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


@st.cache_data(ttl=86400, show_spinner=False)
def fetch_top_institutions(limit: int = 10) -> Optional[List[Dict[str, Any]]]:
    """6G konu aramasında en çok yayın yapan kurumlar (OpenAlex group_by)."""
    year_filter = "|".join(str(y) for y in TREND_YEARS)
    q = urllib.parse.quote(COMBINED_SEARCH)
    url = (
        f"{OPENALEX_BASE}/works?search={q}"
        f"&filter=publication_year:{year_filter}"
        f"&group_by=authorships.institutions.id&per_page=200"
    )
    return _parse_group_by(_fetch_json(url), limit)


@st.cache_data(ttl=86400, show_spinner=False)
def fetch_top_countries(limit: int = 10) -> Optional[List[Dict[str, Any]]]:
    """6G konu aramasında en çok yayın yapan ülkeler (OpenAlex group_by)."""
    year_filter = "|".join(str(y) for y in TREND_YEARS)
    q = urllib.parse.quote(COMBINED_SEARCH)
    url = (
        f"{OPENALEX_BASE}/works?search={q}"
        f"&filter=publication_year:{year_filter}"
        f"&group_by=authorships.institutions.country_code&per_page=200"
    )
    return _parse_group_by(_fetch_json(url), limit)

