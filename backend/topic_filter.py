"""
6G konu süzgeci — Springer/Crossref çekilen kayıttan alakasız başlığı düşürür.
Sayı uydurulmaz; eşleşmeyen kayıt listeden çıkar, yerine başka DOI basılmaz.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List, Optional

_SIXTH = re.compile(r"\b6[\-\s]?g\b|sixth[\-\s]+generation", re.I)

_OFFTOPIC = re.compile(
    r"connectome|brain[\-\s]and[\-\s]cord|\bneuro(?:science|n|log)|\bsynaps|"
    r"hippocamp|\bcortical\b|protein folding|crispr|\bgenome\b|"
    r"quantum chromodynamics|\bclimate change\b",
    re.I,
)

TOPIC_PATTERNS: Dict[str, List[re.Pattern[str]]] = {
    "ISAC": [
        re.compile(r"\bisac\b", re.I),
        re.compile(r"integrated sensing", re.I),
        re.compile(r"\bjcas\b", re.I),
        re.compile(r"sensing and communication", re.I),
    ],
    "RIS": [
        re.compile(r"\bris\b", re.I),
        re.compile(r"reconfigurable intelligent", re.I),
        re.compile(r"intelligent reflecting", re.I),
        re.compile(r"\birs\b", re.I),
    ],
    "Cell-Free": [
        re.compile(r"cell[\-\s]?free", re.I),
        re.compile(r"cellfree", re.I),
    ],
    "THz": [
        re.compile(r"\bthz\b", re.I),
        re.compile(r"terahertz", re.I),
    ],
    "AI-RAN": [
        re.compile(r"ai[\-\s]?ran", re.I),
        re.compile(r"ai[\-\s]?native", re.I),
        re.compile(r"ran intelligent", re.I),
        re.compile(r"radio access network", re.I),
    ],
    "NTN": [
        re.compile(r"\bntn\b", re.I),
        re.compile(r"non[\-\s]?terrestrial", re.I),
        re.compile(r"satellite.*(?:6g|ran|communication)", re.I),
    ],
    "Ambient IoT": [
        re.compile(r"ambient iot", re.I),
        re.compile(r"zero[\-\s]?energy", re.I),
        re.compile(r"backscatter", re.I),
    ],
}

_ALL_TOPIC: List[re.Pattern[str]] = [p for group in TOPIC_PATTERNS.values() for p in group]

_WIRELESS = re.compile(
    r"\b(?:wireless|telecom|communication|networks?|ran|mimo|beamform|"
    r"slicing|reconfigurable|terahertz|satellite|iot|sensing|radio|b5g)\b",
    re.I,
)


def _blob(paper: Dict[str, Any]) -> str:
    return f"{paper.get('title') or ''} {paper.get('abstract') or ''} {paper.get('journal') or ''}"


def _has_topic_token(text: str, topic: str) -> bool:
    pats = TOPIC_PATTERNS.get(topic) or []
    return any(p.search(text) for p in pats)


def paper_on_topic(paper: Dict[str, Any], topic: Optional[str] = None) -> bool:
    """Başlık/özet seçilen konuya değmeli. Konu seçiliyken 6G+wireless yeterli değildir."""
    if not isinstance(paper, dict):
        return False
    text = _blob(paper)
    if not str(paper.get("title") or "").strip():
        return False
    if _OFFTOPIC.search(text) and not _SIXTH.search(text):
        return False
    tpc = (topic or "").strip() or None
    if tpc:
        return _has_topic_token(text, tpc)
    has_token = any(p.search(text) for p in _ALL_TOPIC)
    if _SIXTH.search(text) and (has_token or _WIRELESS.search(text)):
        return True
    if has_token and _WIRELESS.search(text):
        return True
    return False


def filter_cited(
    papers: Iterable[Any],
    topic: Optional[str] = None,
    *,
    limit: int = 10,
) -> List[Dict[str, Any]]:
    kept: List[Dict[str, Any]] = []
    seen = set()
    for paper in papers:
        if not isinstance(paper, dict) or not paper_on_topic(paper, topic):
            continue
        doi = str(paper.get("doi") or "").strip().lower()
        key = doi or str(paper.get("title") or "").casefold()
        if not key or key in seen:
            continue
        seen.add(key)
        kept.append(paper)
    kept.sort(
        key=lambda p: (
            -int(p.get("citations") or 0),
            -int(p.get("year") or 0),
            str(p.get("title") or ""),
        )
    )
    return kept[:limit]
