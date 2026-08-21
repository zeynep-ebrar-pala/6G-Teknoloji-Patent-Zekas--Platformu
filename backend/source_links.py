"""
Kaynak bağlantıları — sayfada yalnızca kullanılan siteler:
patent: Lens.org; yayın: DOI, Springer, WoS.
"""

from __future__ import annotations

import re
import urllib.parse
from typing import Dict, List, Optional, Tuple

SPEC_PUB_TOPICS: Dict[str, str] = {
    "ISAC": "integrated sensing and communication",
    "RIS": "reconfigurable intelligent surface",
    "Cell-Free": "cell-free massive MIMO",
    "THz": "terahertz communication",
    "AI-RAN": "AI-native radio access network",
    "NTN": "non-terrestrial network",
    "Ambient IoT": "ambient IoT",
}

# Lens query_string eşanlamları — ham «6G» değil; Unclassified üretmez.
TOPIC_TERMS: Dict[str, tuple] = {
    "ISAC": (
        "integrated sensing and communication",
        "joint communication and sensing",
        "sensing and communication",
        "ISAC",
        "JCAS",
        "6G perception",
    ),
    "RIS": (
        "reconfigurable intelligent surface",
        "intelligent reflecting surface",
        "RIS-assisted",
        "intelligent metasurface",
    ),
    "Cell-Free": (
        "cell-free massive MIMO",
        "cell-free MIMO",
        "cell free massive MIMO",
        "cell-free RAN",
    ),
    "THz": (
        "terahertz communication",
        "THz communication",
        "sub-THz communication",
        "THz RAN",
    ),
    "AI-RAN": (
        "AI-RAN",
        "AI-native RAN",
        "AI native radio",
        "intelligent RAN",
    ),
    "NTN": (
        "non-terrestrial network",
        "non-terrestrial networks",
        "NTN 6G",
        "6G NTN",
    ),
    "Ambient IoT": (
        "ambient IoT",
        "ambient internet of things",
        "zero-energy IoT",
        "6G ambient",
    ),
}

_PUB_RE = re.compile(r"^([A-Z]{2})(\d+)([A-Z]\d?)$")


def _plus(text: str) -> str:
    return urllib.parse.quote_plus(text)


def _q(text: str) -> str:
    return urllib.parse.quote(text, safe="")


def topic_query(topic: str) -> str:
    if not topic or topic in ("6G", "all", "Tümü", "All"):
        return " OR ".join(f'"{phrase}"' for phrase in SPEC_PUB_TOPICS.values())
    return SPEC_PUB_TOPICS.get(topic) or topic


def parse_publication_number(pub: str) -> Optional[Tuple[str, str, str]]:
    token = re.sub(r"[^A-Za-z0-9]", "", pub or "").upper()
    match = _PUB_RE.match(token)
    if not match:
        return None
    return match.group(1), match.group(2), match.group(3)


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


def lens_patent_url(pub: str, lens_id: str = "") -> str:
    """Lens kayıt sayfası — lens_id varsa onu kullan; yoksa yayın no araması."""
    lid = (lens_id or "").strip()
    if lid:
        return f"https://www.lens.org/lens/patent/{lid}"
    parsed = parse_publication_number(pub)
    if not parsed:
        return f"https://www.lens.org/lens/search/patent/list?q={_q(pub or '')}"
    cc, num, kind = parsed
    if cc == "WO" and len(num) >= 8 and num.startswith("20"):
        reconstructed = f"WO_{num[:4]}_{num[4:]}_{kind}"
    elif cc == "US" and kind.startswith("A") and len(num) >= 10 and num.startswith("20"):
        reconstructed = f"US_{num[:4]}_{num[4:]}_{kind}"
    else:
        reconstructed = f"{cc}_{num}_{kind}"
    return f"https://www.lens.org/lens/patent/{reconstructed}"


def lens_search_url(query: str) -> str:
    q = (query or "6G").strip() or "6G"
    return f"https://www.lens.org/lens/search/patent/list?q={_q(q)}"


def espacenet_record_url(pub: str) -> str:
    parsed = parse_publication_number(pub)
    if not parsed:
        return f"https://worldwide.espacenet.com/patent/search?q={_plus(pub or '')}"
    cc, num, kind = parsed
    return (
        "https://worldwide.espacenet.com/publicationDetails/biblio"
        f"?FT=D&CC={cc}&NR={num}&KC={kind}"
    )


def wipo_record_url(pub: str) -> str:
    parsed = parse_publication_number(pub)
    if parsed and parsed[0] == "WO":
        return f"https://patentscope.wipo.int/search/en/detail.jsf?docId=WO{parsed[1]}"
    compact = re.sub(r"[^A-Za-z0-9]", "", pub or "")
    if not compact:
        return "https://patentscope.wipo.int/search/en/search.jsf"
    return (
        "https://patentscope.wipo.int/search/en/result.jsf"
        f"?query={_q(f'FP:({compact})')}"
    )


def uspto_grant_pdf_url(pub: str) -> str:
    """Yalnızca US B1/B2 tescil PDF. A1 ve ppubs SPA yok."""
    parsed = parse_publication_number(pub)
    if not parsed:
        return ""
    cc, num, kind = parsed
    if cc != "US" or not kind.startswith("B"):
        return ""
    return f"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/{num}"


def patent_record_links(pub: str, source_url: str = "", lens_id: str = "") -> List[Dict[str, str]]:
    """Kartta Lens.org kaydı."""
    url = (source_url or "").strip()
    if url and "lens.org" in url.lower():
        return [{"id": "lens", "url": url}]
    token = (pub or "").strip()
    if not token and not lens_id:
        return []
    return [{"id": "lens", "url": lens_patent_url(token, lens_id)}]


def wos_full_record_url(ut: str) -> str:
    """WoS Core Collection tam kayıt. UT yoksa boş."""
    token = (ut or "").strip().upper()
    if not token:
        return ""
    if not token.startswith("WOS:"):
        token = f"WOS:{token}"
    return f"https://www.webofscience.com/wos/woscc/full-record/{token}"


def wos_doi_openurl(doi: str) -> str:
    """Clarivate OpenURL — oturum açıksa DOI’yi WoS kaydına çözer."""
    doi_clean = (doi or "").strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    if not doi_clean:
        return "https://www.webofscience.com/wos/woscc/basic-search"
    return (
        "https://ws.isiknowledge.com/cps/openurl/service?"
        + urllib.parse.urlencode(
            {"url_ver": "Z39.88-2004", "rft_id": f"info:doi/{doi_clean}"}
        )
    )


def paper_record_links(doi: str, source: str = "", wos_ut: str = "") -> List[Dict[str, str]]:
    """DOI her zaman. Springer kaydıysa Springer; WoS tam kayıt veya DOI OpenURL."""
    doi_clean = (doi or "").strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    if not doi_clean:
        return []
    lower = doi_clean.lower()
    src = (source or "").lower()
    links: List[Dict[str, str]] = [{"id": "doi", "url": doi_url(doi_clean)}]
    if lower.startswith("10.1007") or "springer" in src:
        links.append(
            {
                "id": "springer",
                "url": f"https://link.springer.com/search?query={_q(doi_clean)}",
            }
        )
    ut = (wos_ut or "").strip()
    if not ut:
        from data.wos_ut import ut_for_doi

        ut = ut_for_doi(doi_clean)
    wos_url = wos_full_record_url(ut) or wos_doi_openurl(doi_clean)
    links.append({"id": "wos", "url": wos_url})
    return links


def wos_text_search_url(query: str) -> str:
    q = (query or "6G").strip() or "6G"
    return (
        "https://www.webofscience.com/wos/woscc/advanced-search?"
        f"search={_q(f'TS=({q})')}"
    )


def assignee_patent_links(assignee: str) -> List[Dict[str, str]]:
    """Hak sahibi araması — Lens.org applicant.name."""
    name = (assignee or "").strip()
    if not name:
        return []
    return [{"id": "lens", "url": lens_search_url(f"applicant.name:({name})")}]


def spec_patent_databases() -> List[Dict[str, str]]:
    return [{"id": "lens", "url": "https://www.lens.org/lens/search/patent/list"}]


def spec_pub_databases() -> List[Dict[str, str]]:
    return [
        {"id": "wos", "url": "https://www.webofscience.com/wos/woscc/basic-search"},
        {"id": "springer", "url": "https://link.springer.com/"},
    ]


def topic_pub_searches(topic: str, region: str = "both") -> List[Dict[str, str]]:
    """6G + konu. Türkiye seçilince aramaya Turkey eklenir. Sayı çekilmez."""
    base = topic_query(topic)
    query = f"6G {base}".strip() if base and base != "6G" else "6G"
    if region == "tr":
        query = f"{query} Turkey"
    elif region == "eu":
        query = f"{query} Europe"
    return [
        {
            "id": "wos",
            "url": (
                "https://www.webofscience.com/wos/woscc/advanced-search?"
                f"search={_q(f'TS=({query})')}"
            ),
        },
        {"id": "springer", "url": f"https://link.springer.com/search?query={_q(query)}"},
    ]


def topic_patent_searches(topic: str) -> List[Dict[str, str]]:
    query = topic_query(topic)
    return [{"id": "lens", "url": lens_search_url(query)}]
