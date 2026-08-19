"""
Şartnamedeki patent / yayın veritabanı bağlantıları.
Sayı çekilmez, uydurulmaz. URL yalnızca kilitli yayın numarası, DOI, firma veya konu ile kurulur.
Patent: Google Patents, Lens.org, Espacenet, WIPO PATENTSCOPE, USPTO.
Yayın: IEEE Xplore, Google Scholar, Springer, Elsevier (+ DOI; WoS arama).
IEEE patent sunmaz — patent kartına IEEE linki konmaz.
"""

from __future__ import annotations

import re
import urllib.parse
from typing import Dict, List

# Şartname Modül 3 konu başlıkları (Cell-Free listede yok).
SPEC_PUB_TOPICS: Dict[str, str] = {
    "ISAC": "integrated sensing and communication",
    "RIS": "reconfigurable intelligent surface",
    "NTN": "non-terrestrial network",
    "AI-RAN": "AI-native radio access network",
    "THz": "terahertz communication",
    "Ambient IoT": "ambient IoT",
}


def _q(text: str) -> str:
    return urllib.parse.quote(text, safe="")


def _plus(text: str) -> str:
    return urllib.parse.quote_plus(text)


def _pub_norm(pub: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "", pub or "").upper()


def _uspto_pn_token(pub: str) -> str | None:
    """US12243096B2 → US-12243096-B2. WO/EP için USPTO deep-link yok."""
    raw = _pub_norm(pub)
    m = re.match(r"^(US)(\d+)([A-Z]\d*)$", raw)
    if not m:
        return None
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"


def patent_record_links(pub: str) -> List[Dict[str, str]]:
    """Tek patent kaydı — şartname ofisleri. Canlı sayım yok."""
    token = (pub or "").strip()
    if not token:
        return []
    compact = _pub_norm(token)
    links = [
        {
            "id": "google_patents",
            "url": f"https://patents.google.com/patent/{token}/en",
        },
        {
            "id": "lens",
            "url": f"https://www.lens.org/lens/search/patent/list?q={_q(token)}",
        },
        {
            "id": "espacenet",
            "url": f"https://worldwide.espacenet.com/patent/search?q=pn%3D{_q(compact)}",
        },
        {
            "id": "wipo",
            "url": (
                "https://patentscope.wipo.int/search/en/result.jsf?query="
                + _q(f"FP:({compact})")
            ),
        },
    ]
    uspto = _uspto_pn_token(token)
    if uspto:
        links.append(
            {
                "id": "uspto",
                "url": (
                    "https://ppubs.uspto.gov/pubwebapp/external.html?q="
                    + _q(f"({uspto}).pn.")
                ),
            }
        )
    return links


def assignee_patent_links(assignee: str) -> List[Dict[str, str]]:
    """Hak sahibi araması. Sonuç sayısı buradan okunmaz."""
    name = (assignee or "").strip()
    if not name:
        return []
    quoted = f'"{name}"'
    return [
        {
            "id": "google_patents",
            "url": f"https://patents.google.com/?assignee={_plus(name)}",
        },
        {
            "id": "lens",
            "url": f"https://www.lens.org/lens/search/patent/list?q=assignee:{_q(quoted)}",
        },
        {
            "id": "espacenet",
            "url": (
                "https://worldwide.espacenet.com/patent/search?q="
                + _q(f'pa all "{name}"')
            ),
        },
        {
            "id": "wipo",
            "url": (
                "https://patentscope.wipo.int/search/en/result.jsf?query="
                + _q(f"PA:({name})")
            ),
        },
        {
            "id": "uspto",
            "url": "https://ppubs.uspto.gov/pubwebapp/",
        },
    ]


def paper_record_links(doi: str, publisher: str = "") -> List[Dict[str, str]]:
    """DOI + şartname mix: IEEE, Scholar, Springer, Elsevier, WoS. Sayı uydurulmaz."""
    doi_clean = (doi or "").strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    if not doi_clean:
        return []
    q = _q(doi_clean)
    _ = publisher
    return [
        {"id": "doi", "url": f"https://doi.org/{doi_clean}"},
        {
            "id": "ieee",
            "url": (
                "https://ieeexplore.ieee.org/search/searchresult.jsp"
                f"?newsearch=true&queryText={q}"
            ),
        },
        {"id": "scholar", "url": f"https://scholar.google.com/scholar?q={q}"},
        {"id": "springer", "url": f"https://link.springer.com/search?query={q}"},
        {"id": "elsevier", "url": f"https://www.sciencedirect.com/search?qs={q}"},
        {
            "id": "wos",
            "url": f"https://www.webofscience.com/wos/woscc/quick-search?value={q}",
        },
    ]


def spec_patent_databases() -> List[Dict[str, str]]:
    return [
        {"id": "google_patents", "url": "https://patents.google.com/"},
        {"id": "lens", "url": "https://www.lens.org/lens/search/patent/page/1"},
        {"id": "espacenet", "url": "https://worldwide.espacenet.com/"},
        {"id": "wipo", "url": "https://patentscope.wipo.int/search/en/search.jsf"},
        {"id": "uspto", "url": "https://www.uspto.gov/patents/search"},
    ]


def spec_pub_databases() -> List[Dict[str, str]]:
    return [
        {"id": "ieee", "url": "https://ieeexplore.ieee.org/"},
        {"id": "scholar", "url": "https://scholar.google.com/"},
        {"id": "springer", "url": "https://link.springer.com/"},
        {"id": "elsevier", "url": "https://www.sciencedirect.com/"},
        {"id": "wos", "url": "https://www.webofscience.com/wos/woscc/basic-search"},
    ]


def topic_pub_searches(topic: str) -> List[Dict[str, str]]:
    query = SPEC_PUB_TOPICS.get(topic) or topic
    q = _q(query)
    return [
        {
            "id": "ieee",
            "url": (
                "https://ieeexplore.ieee.org/search/searchresult.jsp"
                f"?newsearch=true&queryText={q}"
            ),
        },
        {"id": "scholar", "url": f"https://scholar.google.com/scholar?q={q}"},
        {"id": "springer", "url": f"https://link.springer.com/search?query={q}"},
        {"id": "elsevier", "url": f"https://www.sciencedirect.com/search?qs={q}"},
        {
            "id": "wos",
            "url": (
                "https://www.webofscience.com/wos/woscc/quick-search?value=" + q
            ),
        },
    ]


def topic_patent_searches(topic: str) -> List[Dict[str, str]]:
    """Aynı 6G konu ifadesi patent ofislerinde. IEEE yok (patent sunmaz)."""
    query = SPEC_PUB_TOPICS.get(topic) or topic
    q = _q(query)
    plus = _plus(query)
    return [
        {
            "id": "google_patents",
            "url": f"https://patents.google.com/?q={plus}",
        },
        {
            "id": "lens",
            "url": f"https://www.lens.org/lens/search/patent/list?q={q}",
        },
        {
            "id": "espacenet",
            "url": f"https://worldwide.espacenet.com/patent/search?q={q}",
        },
        {
            "id": "wipo",
            "url": (
                "https://patentscope.wipo.int/search/en/result.jsf?query="
                + _q(f"EN_ALL:({query})")
            ),
        },
        {"id": "uspto", "url": "https://ppubs.uspto.gov/pubwebapp/"},
    ]
