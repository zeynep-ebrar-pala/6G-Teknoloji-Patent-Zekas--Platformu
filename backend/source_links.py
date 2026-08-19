"""
Kaynak bağlantıları — yalnızca tarayıcıda açılan, doğrulanmış sayfalar.
Kartlarda tek link: kaydın alındığı sayfa (Google Patents veya DOI).
USPTO ppubs deep-link (external.html?q=...pn.) boş sayfa verdiği için kullanılmaz.
"""

from __future__ import annotations

import urllib.parse
from typing import Dict, List

SPEC_PUB_TOPICS: Dict[str, str] = {
    "ISAC": "integrated sensing and communication",
    "RIS": "reconfigurable intelligent surface",
    "NTN": "non-terrestrial network",
    "AI-RAN": "AI-native radio access network",
    "THz": "terahertz communication",
    "Ambient IoT": "ambient IoT",
}


def _plus(text: str) -> str:
    return urllib.parse.quote_plus(text)


def _q(text: str) -> str:
    return urllib.parse.quote(text, safe="")


def google_patents_record_url(pub: str) -> str:
    token = (pub or "").strip()
    if not token:
        return "https://patents.google.com/"
    return f"https://patents.google.com/patent/{token}/en"


def doi_url(doi: str) -> str:
    doi_clean = (doi or "").strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    if not doi_clean:
        return ""
    return f"https://doi.org/{doi_clean}"


def assignee_patent_links(assignee: str) -> List[Dict[str, str]]:
    """Hak sahibi — Google Patents (kayıtların alındığı site)."""
    name = (assignee or "").strip()
    if not name:
        return []
    return [
        {
            "id": "google_patents",
            "url": f"https://patents.google.com/?assignee={_plus(name)}",
        }
    ]


def spec_patent_databases() -> List[Dict[str, str]]:
    """Açılış sayfaları (HTTP 200). ppubs deep-link yok."""
    return [
        {"id": "google_patents", "url": "https://patents.google.com/"},
        {"id": "lens", "url": "https://www.lens.org/"},
        {"id": "wipo", "url": "https://patentscope.wipo.int/search/en/search.jsf"},
        {"id": "uspto", "url": "https://www.uspto.gov/patents/search"},
    ]


def spec_pub_databases() -> List[Dict[str, str]]:
    return [
        {"id": "ieee", "url": "https://ieeexplore.ieee.org/"},
        {"id": "scholar", "url": "https://scholar.google.com/"},
        {"id": "springer", "url": "https://link.springer.com/"},
    ]


def topic_pub_searches(topic: str) -> List[Dict[str, str]]:
    query = SPEC_PUB_TOPICS.get(topic) or topic
    return [
        {
            "id": "ieee",
            "url": (
                "https://ieeexplore.ieee.org/search/searchresult.jsp"
                f"?newsearch=true&queryText={_q(query)}"
            ),
        }
    ]


def topic_patent_searches(topic: str) -> List[Dict[str, str]]:
    query = SPEC_PUB_TOPICS.get(topic) or topic
    return [
        {
            "id": "google_patents",
            "url": f"https://patents.google.com/?q={_plus(query)}",
        }
    ]
