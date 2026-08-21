"""
Şartname veritabanı toplamları — yalnızca herkese açık veya bireysel API.
Sayı gelmezse None (UI «—»). HTML kazıyıp çubuk uydurulmaz.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import streamlit as st

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


def peek_patent_source_totals(topic: Optional[str]) -> List[Dict[str, Any]]:
    """Disk önbelleği — ağ yok."""
    from backend.patent_apis import lens_explorer_dsl, lens_topic_dsl, peek_lens_count

    label = topic or "6G"
    links = topic_patent_searches(label)
    keys = patent_key_status()
    q = lens_topic_dsl(topic) if topic else lens_explorer_dsl()
    n = peek_lens_count(q)
    return [
        _row(
            "lens",
            _search_url(links, "lens"),
            n,
            _patent_method("lens", n, keys),
        )
    ]


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_patent_source_totals(topic: Optional[str], _keys: str = "") -> List[Dict[str, Any]]:
    """Yalnızca Lens.org patent/search. Yanıt yoksa None (UI —)."""
    label = topic or "6G"
    links = topic_patent_searches(label)
    counts = fetch_office_counts(topic or "", _keys or patent_key_fingerprint())
    keys = patent_key_status()
    n = counts.get("lens")
    return [
        _row(
            "lens",
            _search_url(links, "lens"),
            n,
            _patent_method("lens", n, keys),
        )
    ]


@st.cache_data(ttl=21600, show_spinner=False)
def fetch_pub_source_totals(topic: Optional[str], _keys: str = "") -> List[Dict[str, Any]]:
    """WoS (canlı veya önbellek) + Springer. Anahtar yoksa None."""
    from backend.wos_topic_cache import wos_overlay

    label = topic or "6G"
    links = topic_pub_searches(label, "tr")
    overlay = wos_overlay(topic)
    wos_n = overlay.get("wos_total") if overlay else None
    springer_topics = None
    try:
        from backend.publisher_apis import fetch_springer_topic_totals

        springer_topics = fetch_springer_topic_totals(_keys or key_fingerprint())
    except Exception:
        springer_topics = {}
    springer_n = None
    if topic and isinstance(springer_topics, dict):
        n = springer_topics.get(topic)
        springer_n = n if isinstance(n, int) else None
    rows: List[Dict[str, Any]] = []
    for source_id, n in (("wos", wos_n), ("springer", springer_n)):
        rows.append(
            _row(
                source_id,
                _search_url(links, source_id),
                n if isinstance(n, int) else None,
                f"native_{source_id}" if isinstance(n, int) else "none",
            )
        )
    return rows
