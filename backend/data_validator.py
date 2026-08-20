"""
Source-locked veri doğrulama ve normalizasyon.
Doğrulanamayan kayıtlar production'a alınmaz.
"""

from __future__ import annotations

from typing import Any, Dict, List
from urllib.parse import urlparse

REQUIRED_PATENT_FIELDS = (
    "publication_number",
    "title",
    "assignee",
    "year",
    "domain",
    "source",
    "source_url",
)

REQUIRED_PAPER_FIELDS = (
    "title",
    "authors",
    "journal",
    "year",
    "doi",
    "source",
    "source_url",
)

ALLOWED_PATENT_HOSTS = ("patents.google.com", "lens.org")
ALLOWED_PAPER_HOSTS = ("doi.org", "ieeexplore.ieee.org", "link.springer.com", "sciencedirect.com")


def _valid_url(url: str, allowed_hosts: tuple) -> bool:
    if not url or not isinstance(url, str):
        return False
    try:
        parsed = urlparse(url.strip())
        if parsed.scheme not in ("http", "https"):
            return False
        host = (parsed.netloc or "").lower().removeprefix("www.")
        return any(host == h or host.endswith("." + h) for h in allowed_hosts)
    except Exception:
        return False


def normalize_patent(raw: Dict[str, Any]) -> Dict[str, Any] | None:
    """Patent kaydını source-locked modele dönüştürür; geçersizse None."""
    pub = raw.get("publication_number") or raw.get("id")
    source_url = raw.get("source_url") or raw.get("url")
    if not pub or not raw.get("title") or not source_url:
        return None
    if not _valid_url(source_url, ALLOWED_PATENT_HOSTS):
        return None

    return {
        "publication_number": str(pub).strip(),
        "title": str(raw["title"]).strip(),
        "assignee": str(raw.get("assignee", "")).strip(),
        "inventors": raw.get("inventors") or [],
        "year": int(raw["year"]),
        "domain": str(raw.get("domain", "")).strip(),
        "abstract": str(raw.get("abstract", "")).strip(),
        "source": raw.get("source") or "Google Patents",
        "source_url": source_url.strip(),
        "id": str(pub).strip(),
        "url": source_url.strip(),
    }


def normalize_paper(raw: Dict[str, Any]) -> Dict[str, Any] | None:
    """Akademik yayın kaydını source-locked modele dönüştürür."""
    doi = (raw.get("doi") or "").strip()
    source_url = raw.get("source_url") or raw.get("url")
    if not raw.get("title") or not doi or not source_url:
        return None
    if not doi.startswith("10."):
        return None
    if not _valid_url(source_url, ALLOWED_PAPER_HOSTS):
        return None

    return {
        "title": str(raw["title"]).strip(),
        "authors": str(raw.get("authors", "")).strip(),
        "journal": str(raw.get("journal", "")).strip(),
        "year": int(raw["year"]),
        "doi": doi,
        "citations": int(raw["citations"]) if raw.get("citations") is not None else None,
        "source": raw.get("source") or "Crossref / DOI",
        "source_url": source_url.strip(),
        "url": source_url.strip(),
        "topic": str(raw.get("topic") or "").strip(),
        "wos_ut": str(raw.get("wos_ut") or "").strip(),
    }


def load_validated_patents(raw_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for raw in raw_list:
        norm = normalize_patent(raw)
        if norm:
            out.append(norm)
    return out


def load_validated_papers(raw_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for raw in raw_list:
        norm = normalize_paper(raw)
        if norm:
            out.append(norm)
    return out
