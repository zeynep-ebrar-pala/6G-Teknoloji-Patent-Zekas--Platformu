"""
Ana sayfa örümcek ağı — Lens patent + Springer yayın kanıtı.
TRL uydurulmaz; ham toplamlar cache-first, eksikse API.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

import streamlit as st

from backend.patent_service import TECH_ID_TO_DOMAIN
from data.patents import TECHNOLOGY_DOMAINS


def _spec_topic_counts() -> Dict[str, int]:
    """Patent Zekası yolu: konu ∧ şartname firmaları (önbellek)."""
    from backend.patent_prefetch import frames_from_snapshot, snapshot
    from data.patents import SPEC_COMPANIES

    snap = snapshot(None, tuple(SPEC_COMPANIES))
    _, topics, *_ = frames_from_snapshot(snap, list(SPEC_COMPANIES))
    return {str(k): int(v) for k, v in (topics or {}).items() if isinstance(v, int)}


def _patent_n(domain: str, spec_map: Optional[Dict[str, int]] = None) -> Optional[int]:
    """Peek Lens konu total → Patent Zekası konu∧firma → canlı Lens."""
    from backend.patent_apis import lens_topic_count, lens_topic_dsl, peek_lens_count

    peeked = peek_lens_count(lens_topic_dsl(domain))
    if isinstance(peeked, int):
        return peeked
    if spec_map and isinstance(spec_map.get(domain), int):
        return int(spec_map[domain])
    live = lens_topic_count(domain)
    return live if isinstance(live, int) else None


def _pub_n(domain: str) -> Optional[int]:
    from backend.springer_live import live_topic_row

    row = live_topic_row(domain)
    n = row.get("total")
    return int(n) if isinstance(n, int) else None


def _norm(values: List[Optional[int]]) -> List[Optional[float]]:
    nums = [v for v in values if isinstance(v, int) and v >= 0]
    if not nums:
        return [None for _ in values]
    peak = max(nums)
    if peak <= 0:
        return [0.0 if isinstance(v, int) else None for v in values]
    out: List[Optional[float]] = []
    for v in values:
        if not isinstance(v, int):
            out.append(None)
        else:
            out.append(round(100.0 * v / peak, 1))
    return out


@st.cache_data(ttl=3600, show_spinner=False)
def topic_evidence_rows(_fp: str = "") -> List[Dict[str, Any]]:
    """
    Yedi 6G konusu: Lens total + Springer Meta total.
    r_patent / r_pub: seri içi göreli yoğunluk (max=100); hover ham sayı.
    """
    from backend.patent_apis import key_fingerprint as patent_fp
    from backend.publisher_apis import key_fingerprint as pub_fp

    _ = (_fp, patent_fp(), pub_fp())
    spec_map = _spec_topic_counts()
    rows: List[Dict[str, Any]] = []
    for domain in TECHNOLOGY_DOMAINS:
        tech_id = next((tid for tid, name in TECH_ID_TO_DOMAIN.items() if name == domain), "")
        patent = _patent_n(domain, spec_map)
        pub = _pub_n(domain)
        rows.append(
            {
                "domain": domain,
                "tech_id": tech_id,
                "patent": patent,
                "pub": pub,
            }
        )
    patents = [r["patent"] for r in rows]
    pubs = [r["pub"] for r in rows]
    for row, rp, rq in zip(rows, _norm(patents), _norm(pubs)):
        row["r_patent"] = rp
        row["r_pub"] = rq
    return rows


def evidence_fingerprint() -> str:
    from backend.patent_apis import key_fingerprint as patent_fp
    from backend.publisher_apis import key_fingerprint as pub_fp
    from backend.springer_live import load_live

    blob = load_live()
    fetched = str(blob.get("fetched_at") or "")
    return f"{patent_fp()}|{pub_fp()}|{fetched}"
