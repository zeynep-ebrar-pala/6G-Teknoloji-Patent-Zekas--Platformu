"""
Şartname veritabanı toplamları — yalnızca herkese açık veya bireysel API.
Sayı gelmezse None (UI «—»). HTML kazıyıp çubuk uydurulmaz.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import streamlit as st

from backend.literature_client import literature_bundle
from backend.patent_apis import fetch_office_counts, key_fingerprint as patent_key_fingerprint, key_status as patent_key_status
from backend.publisher_apis import key_fingerprint
from backend.source_links import topic_patent_searches, topic_pub_searches, topic_query


def _search_url(links: List[Dict[str, str]], source_id: str) -> str:
    for item in links:
        if item.get("id") == source_id:
            return str(item.get("url") or "")
    return ""


def _row(source_id: str, url: str, count: Optional[int], method: str) -> Dict[str, Any]:
    return {"id": source_id, "url": url, "count": count, "method": method}


def _patent_method(source_id: str, n: Optional[int], keys: Dict[str, bool]) -> str:
    if source_id == "google_patents":
        return "gp"
    if isinstance(n, int):
        return f"native_{source_id}"
    if source_id == "wipo":
        return "none"
    if not keys.get(source_id):
        return "need_key"
    return "api_empty"


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_patent_source_totals(topic: Optional[str], _keys: str = "") -> List[Dict[str, Any]]:
    """Google Patents xhr; Lens / Espacenet / USPTO bireysel anahtar. WIPO anahtarsız JSON yok."""
    label = topic or "6G"
    query = topic_query(label)
    links = topic_patent_searches(label)
    counts = fetch_office_counts(query, _keys or patent_key_fingerprint())
    keys = patent_key_status()
    return [
        _row(
            source_id,
            _search_url(links, source_id),
            counts.get(source_id),
            _patent_method(source_id, counts.get(source_id), keys),
        )
        for source_id in ("google_patents", "lens", "espacenet", "wipo", "uspto")
    ]


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_pub_source_totals(topic: Optional[str], _keys: str = "") -> List[Dict[str, Any]]:
    """IEEE / Springer / Elsevier / WoS / Scholar native API. Anahtar yoksa None."""
    label = topic or "6G"
    links = topic_pub_searches(label, "tr")
    bundle = literature_bundle("tr", topic, _keys or key_fingerprint())
    pubs = bundle.get("publishers") or {}
    rows: List[Dict[str, Any]] = []
    for source_id in ("ieee", "springer", "elsevier"):
        n = pubs.get(source_id)
        rows.append(
            _row(
                source_id,
                _search_url(links, source_id),
                n if isinstance(n, int) else None,
                f"native_{source_id}",
            )
        )
    scholar_n = pubs.get("scholar")
    rows.append(
        _row(
            "scholar",
            _search_url(links, "scholar"),
            scholar_n if isinstance(scholar_n, int) else None,
            "native_scholar" if isinstance(scholar_n, int) else "none",
        )
    )
    wos_n = pubs.get("wos")
    rows.append(
        _row(
            "wos",
            _search_url(links, "wos"),
            wos_n if isinstance(wos_n, int) else None,
            "native_wos" if isinstance(wos_n, int) else "none",
        )
    )
    return rows
