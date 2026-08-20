"""
Kaynak bağlantıları — kaydın bulunduğu sayfa (Google Patents / DOI + diğer ofisler).
USPTO ppubs deep-link (external.html?q=...pn.) boş SPA verdiği için kullanılmaz.
US tescil için USPTO grant PDF kullanılır (tarayıcıda açılır).
"""

from __future__ import annotations

import re
import urllib.parse
from typing import Dict, List, Optional, Tuple

SPEC_PUB_TOPICS: Dict[str, str] = {
    "ISAC": "integrated sensing and communication",
    "RIS": "reconfigurable intelligent surface",
    "NTN": "non-terrestrial network",
    "AI-RAN": "AI-native radio access network",
    "THz": "terahertz communication",
    "Ambient IoT": "ambient IoT",
}

_PUB_RE = re.compile(r"^([A-Z]{2})(\d+)([A-Z]\d?)$")


def _plus(text: str) -> str:
    return urllib.parse.quote_plus(text)


def _q(text: str) -> str:
    return urllib.parse.quote(text, safe="")


def topic_query(topic: str) -> str:
    return SPEC_PUB_TOPICS.get(topic) or (topic or "6G")


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


def lens_patent_url(pub: str) -> str:
    """Lens ayrıntı sayfası — doğrulanmış ID biçimi; olmazsa yayın no araması."""
    parsed = parse_publication_number(pub)
    if not parsed:
        return f"https://www.lens.org/lens/search/patent/list?q={_q(pub or '')}"
    cc, num, kind = parsed
    if cc == "WO" and len(num) >= 8 and num.startswith("20"):
        lens_id = f"WO_{num[:4]}_{num[4:]}_{kind}"
    elif cc == "US" and kind.startswith("A") and len(num) >= 10 and num.startswith("20"):
        lens_id = f"US_{num[:4]}_{num[4:]}_{kind}"
    else:
        lens_id = f"{cc}_{num}_{kind}"
    return f"https://www.lens.org/lens/patent/{lens_id}"


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


def patent_record_links(pub: str) -> List[Dict[str, str]]:
    """Aynı yayın no: Google Patents + Lens + Espacenet + PATENTSCOPE + USPTO PDF (varsa)."""
    token = (pub or "").strip()
    if not token:
        return []
    links: List[Dict[str, str]] = [
        {"id": "google_patents", "url": google_patents_record_url(token)},
        {"id": "lens", "url": lens_patent_url(token)},
        {"id": "espacenet", "url": espacenet_record_url(token)},
        {"id": "wipo", "url": wipo_record_url(token)},
    ]
    uspto = uspto_grant_pdf_url(token)
    if uspto:
        links.append({"id": "uspto", "url": uspto})
    return links


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
    """DOI her zaman. Yayıncı sayfası yalnızca DOI öneki o yayınevindeyse. Scholar + WoS."""
    doi_clean = (doi or "").strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    if not doi_clean:
        return []
    lower = doi_clean.lower()
    src = (source or "").lower()
    links: List[Dict[str, str]] = [{"id": "doi", "url": doi_url(doi_clean)}]
    if lower.startswith("10.1109") or "ieee" in src:
        links.append(
            {
                "id": "ieee",
                "url": (
                    "https://ieeexplore.ieee.org/search/searchresult.jsp"
                    f"?newsearch=true&queryText={_q('DOI:' + doi_clean)}"
                ),
            }
        )
    if lower.startswith("10.1007") or "springer" in src:
        links.append(
            {
                "id": "springer",
                "url": f"https://link.springer.com/search?query={_q(doi_clean)}",
            }
        )
    if lower.startswith("10.1016") or "elsevier" in src:
        links.append(
            {
                "id": "elsevier",
                "url": f"https://www.sciencedirect.com/search?qs={_q(doi_clean)}",
            }
        )
    links.append(
        {
            "id": "scholar",
            "url": f"https://scholar.google.com/scholar?q={_q(doi_clean)}",
        }
    )
    ut = (wos_ut or "").strip()
    if not ut:
        from data.wos_ut import ut_for_doi

        ut = ut_for_doi(doi_clean)
    wos_url = wos_full_record_url(ut) or wos_doi_openurl(doi_clean)
    links.append({"id": "wos", "url": wos_url})
    return links


def assignee_patent_links(assignee: str) -> List[Dict[str, str]]:
    """Hak sahibi araması — tüm şartname patent ofisleri."""
    name = (assignee or "").strip()
    if not name:
        return []
    return [
        {"id": "google_patents", "url": f"https://patents.google.com/?assignee={_plus(name)}"},
        {"id": "lens", "url": f"https://www.lens.org/lens/search/patent/list?q={_q('assignee:' + name)}"},
        {
            "id": "espacenet",
            "url": f"https://worldwide.espacenet.com/patent/search?q={_plus(f'pa = \"{name}\"')}",
        },
        {
            "id": "wipo",
            "url": f"https://patentscope.wipo.int/search/en/result.jsf?query={_q('PA:(' + name + ')')}",
        },
        {"id": "uspto", "url": f"https://patents.google.com/?assignee={_plus(name)}&country=US"},
    ]


def spec_patent_databases() -> List[Dict[str, str]]:
    """Açılış sayfaları. ppubs deep-link yok."""
    return [
        {"id": "google_patents", "url": "https://patents.google.com/"},
        {"id": "lens", "url": "https://www.lens.org/"},
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
            "id": "ieee",
            "url": (
                "https://ieeexplore.ieee.org/search/searchresult.jsp"
                f"?newsearch=true&queryText={_q(query)}"
            ),
        },
        {"id": "scholar", "url": f"https://scholar.google.com/scholar?q={_plus(query)}"},
        {"id": "springer", "url": f"https://link.springer.com/search?query={_q(query)}"},
        {"id": "elsevier", "url": f"https://www.sciencedirect.com/search?qs={_plus(query)}"},
        {
            "id": "wos",
            "url": (
                "https://www.webofscience.com/wos/woscc/advanced-search?"
                f"search={_q(f'TS=({query})')}"
            ),
        },
    ]


def topic_patent_searches(topic: str) -> List[Dict[str, str]]:
    query = topic_query(topic)
    return [
        {"id": "google_patents", "url": f"https://patents.google.com/?q={_plus(query)}"},
        {"id": "lens", "url": f"https://www.lens.org/lens/search/patent/list?q={_q(query)}"},
        {
            "id": "espacenet",
            "url": f"https://worldwide.espacenet.com/patent/search?q={_plus(query)}",
        },
        {
            "id": "wipo",
            "url": f"https://patentscope.wipo.int/search/en/result.jsf?query={_q(query)}",
        },
        {"id": "uspto", "url": f"https://patents.google.com/?q={_plus(query)}&country=US"},
    ]
