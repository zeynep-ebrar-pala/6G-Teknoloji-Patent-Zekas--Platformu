"""
Patent analitik servisi — Lens.org kayıtlarından metrik üretir.
"""

from __future__ import annotations

import re
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import streamlit as st

from backend.data_validator import normalize_patent
from backend.source_links import lens_patent_url
from data.patents import SPEC_COMPANIES, TECHNOLOGY_DOMAINS

TECH_ID_TO_DOMAIN = {
    "isac": "ISAC",
    "ris": "RIS",
    "cell_free": "Cell-Free",
    "thz": "THz",
    "ai_ran": "AI-RAN",
    "ntn": "NTN",
    "ambient_iot": "Ambient IoT",
}

_ASSIGNEE_MAP = {
    "Huawei Technologies Co., Ltd.": "Huawei",
    "Qualcomm Inc.": "Qualcomm",
    "Samsung Electronics Co., Ltd.": "Samsung",
    "Telefonaktiebolaget LM Ericsson AB": "Ericsson",
    "Nokia Solutions & Networks": "Nokia",
    "Nokia Technologies Oy": "Nokia",
    "Nokia Shanghai Bell Co Ltd": "Nokia",
    "ZTE Corporation": "ZTE",
    "ZTE Corp": "ZTE",
    "NEC Corporation": "NEC",
    "Intel Corporation": "Intel",
    "National Institute of Information and Communications Technology": "NICT",
    "InterDigital Patent Holdings Inc.": "InterDigital",
    "Northeastern University": "Northeastern Univ.",
    "AT&T Intellectual Property I, L.P.": "AT&T",
    "Deutsche Telekom AG": "Deutsche Telekom",
    "LG Electronics Inc.": "LG Electronics",
}


_COMPANY_PATTERNS: Tuple[Tuple[str, str], ...] = (
    ("Nokia", r"\bnokia\b"),
    ("Ericsson", r"\bericsson\b"),
    ("Huawei", r"\bhuawei\b"),
    ("Samsung", r"\bsamsung\b"),
    ("Qualcomm", r"\bqualcomm\b"),
    ("ZTE", r"\bzte\b"),
    ("NEC", r"\bnec\b"),
    ("NICT", r"\bnict\b|national institute of information"),
    ("Intel", r"\bintel\b"),
)


def _company_match(assignee: str) -> Optional[str]:
    """Intel ≠ intelligent. NICT tam ad veya kısaltma."""
    text = (assignee or "").lower()
    if not text:
        return None
    for name, pat in _COMPANY_PATTERNS:
        if re.search(pat, text):
            return name
    return None


def _normalize_company(assignee: str) -> str:
    raw = (assignee or "").strip()
    if not raw:
        return raw
    hit = _company_match(raw)
    if hit:
        return hit
    if raw in _ASSIGNEE_MAP:
        return _ASSIGNEE_MAP[raw]
    return raw.split()[0]


_DOMAIN_HINTS = (
    ("ISAC", ("isac", "integrated sensing", "sensing and communication", "joint communication and sensing", "jcas", "6g perception", "perception framework")),
    ("RIS", ("reconfigurable intelligent", "intelligent surface", "intelligent reflecting", "ris-assisted", " metasurface", " ris ")),
    ("Cell-Free", ("cell-free", "cell free", "distributed mimo")),
    ("THz", ("terahertz", "thz ", "sub-thz", "sub thz")),
    ("AI-RAN", ("ai-ran", "ai native", "ai-native", "intelligent ran")),
    ("NTN", ("non-terrestrial", "non terrestrial", "ntn ", "leo satellite", "satellite ran")),
    ("Ambient IoT", ("ambient iot", "ambient internet", "zero-energy iot", "backscatter iot")),
)


def _infer_domain(title: str, snippet: str) -> Optional[str]:
    """Yedili Explorer dışı etiket yok. Eşleşmezse kayıt düşer; Unclassified yok."""
    text = f" {title} {snippet} ".lower()
    for domain, hints in _DOMAIN_HINTS:
        if any(h in text for h in hints):
            return domain
    return None


def _from_lens(raw: Dict[str, Any], domain: str) -> Optional[Dict[str, Any]]:
    pub = raw.get("publication_number") or ""
    lens_id = str(raw.get("lens_id") or "").strip()
    source_url = str(raw.get("source_url") or "").strip() or lens_patent_url(str(pub), lens_id)
    return normalize_patent(
        {
            "publication_number": pub,
            "title": raw.get("title") or "",
            "assignee": raw.get("assignee") or "",
            "year": raw.get("year"),
            "domain": domain,
            "abstract": raw.get("abstract") or "",
            "source": "Lens.org",
            "source_url": source_url,
        }
    )


def _fetch_live_vendor_patents(domain: Optional[str] = None) -> List[Dict[str, Any]]:
    """Yedi 6G konusu × şartname firmaları. Konu = arama; Unclassified yok."""
    from backend.config import get_lens_token
    from backend.patent_apis import key_fingerprint, lens_topic_vendor_bundle

    if not get_lens_token():
        return []
    topic = _norm_domain(domain)
    topics = [topic] if topic else list(TECHNOLOGY_DOMAINS)
    keys = key_fingerprint()
    out: List[Dict[str, Any]] = []
    seen: set = set()
    for name in topics:
        bundle = lens_topic_vendor_bundle(name, tuple(SPEC_COMPANIES), keys)
        for raw in bundle.get("rows") or []:
            payload = dict(raw)
            company = _company_match(payload.get("assignee") or "")
            if not company:
                continue
            payload["assignee"] = company
            pub = payload.get("publication_number") or ""
            if not pub or pub in seen:
                continue
            rec = _from_lens(payload, name)
            if not rec:
                continue
            seen.add(pub)
            out.append(rec)
    return out


@st.cache_data(ttl=3600, show_spinner=False)
def _cached_vendor_patents(domain: Optional[str], _keys: str) -> List[Dict[str, Any]]:
    return _fetch_live_vendor_patents(domain)


def _live_vendor_patents(domain: Optional[str] = None) -> List[Dict[str, Any]]:
    from backend.patent_apis import key_fingerprint

    return _cached_vendor_patents(_norm_domain(domain), key_fingerprint())


def _patents(domain: Optional[str] = None) -> List[Dict[str, Any]]:
    return _live_vendor_patents(domain)


def _with_company(patents: List[Dict[str, Any]], company: Optional[str] = None) -> List[Dict[str, Any]]:
    if not company or company == "Tümü":
        return patents
    return [p for p in patents if _normalize_company(p["assignee"]) == company]


def _norm_domain(domain: Optional[str]) -> Optional[str]:
    if not domain or domain in ("all", "Tümü", "All"):
        return None
    return domain


def _scoped(company: Optional[str] = None, domain: Optional[str] = None) -> List[Dict[str, Any]]:
    d = _norm_domain(domain)
    patents = _with_company(_patents(d), company)
    if not d:
        return patents
    return [p for p in patents if (p.get("domain") or "") == d]


def _companies_with_patents() -> List[str]:
    return sorted({_normalize_company(p["assignee"]) for p in _patents()})


def _build_patent_trends(company: Optional[str] = None, domain: Optional[str] = None) -> pd.DataFrame:
    patents = _scoped(company, domain)
    if not patents:
        return pd.DataFrame()
    years = sorted({p["year"] for p in patents})
    rows: Dict[str, List[int]] = {"Years": years}
    companies = sorted({_normalize_company(p["assignee"]) for p in patents})
    for comp in companies:
        counts = [
            sum(
                1
                for p in patents
                if p["year"] == year and _normalize_company(p["assignee"]) == comp
            )
            for year in years
        ]
        if any(c > 0 for c in counts):
            rows[comp] = counts
    return pd.DataFrame(rows)


def _build_domain_distribution(company: Optional[str] = None, domain: Optional[str] = None) -> pd.DataFrame:
    patents = _scoped(company, domain)
    records = []
    companies = sorted({_normalize_company(p["assignee"]) for p in patents})
    axes = list(TECHNOLOGY_DOMAINS)
    for comp in companies:
        company_patents = [p for p in patents if _normalize_company(p["assignee"]) == comp]
        if not company_patents:
            continue
        domain_counts = Counter(p["domain"] for p in company_patents)
        row: Dict[str, Any] = {"Company": comp}
        for dname in axes:
            row[dname] = int(domain_counts.get(dname, 0))
        records.append(row)
    return pd.DataFrame(records)


def _build_keywords(company: Optional[str] = None, domain: Optional[str] = None) -> Dict[str, int]:
    stop = {
        "a", "an", "the", "for", "and", "or", "in", "of", "to", "via", "using",
        "method", "apparatus", "system", "methods", "apparatuses", "based",
        "thereof", "therefor", "with", "from",
    }
    counter: Counter = Counter()
    for p in _scoped(company, domain):
        words = p["title"].lower().replace("-", " ").replace("(", " ").replace(")", " ").split()
        for w in words:
            w = w.strip(",.")
            if len(w) > 3 and w not in stop:
                counter[w] += 1
    return dict(counter.most_common(20))


def _compute_summary(company: Optional[str] = None, domain: Optional[str] = None) -> Dict[str, Any]:
    patents = _scoped(company, domain)
    total = len(patents)
    by_company = Counter(_normalize_company(p["assignee"]) for p in patents)
    leader = by_company.most_common(1)[0] if by_company else ("—", 0)
    by_domain = Counter(p["domain"] for p in patents if p.get("domain") in TECHNOLOGY_DOMAINS)
    top_domain = by_domain.most_common(1)[0] if by_domain else ("—", 0)
    return {
        "total": total,
        "leader_company": leader[0],
        "leader_count": leader[1],
        "top_domain": top_domain[0],
        "top_domain_count": top_domain[1],
        "source": "Lens.org",
        "company_counts": dict(by_company),
        "topic_counts": {d: int(by_domain.get(d, 0)) for d in TECHNOLOGY_DOMAINS},
    }


def _build_network_edges(company: Optional[str] = None, domain: Optional[str] = None) -> List[Tuple[str, str]]:
    seen: set = set()
    edges: List[Tuple[str, str]] = []
    for p in _scoped(company, domain):
        edge = (_normalize_company(p["assignee"]), p["domain"])
        if edge not in seen:
            seen.add(edge)
            edges.append(edge)
    return edges


def _build_density_df(company: Optional[str] = None, domain: Optional[str] = None) -> pd.DataFrame:
    patents = _scoped(company, domain)
    companies = [company] if company else list(SPEC_COMPANIES)
    rows = []
    for comp in companies:
        row = {"Company": comp}
        for dname in TECHNOLOGY_DOMAINS:
            row[dname] = sum(
                1
                for p in patents
                if _normalize_company(p["assignee"]) == comp and p["domain"] == dname
            )
        rows.append(row)
    return pd.DataFrame(rows)


def _build_sunburst_df(company: Optional[str] = None, domain: Optional[str] = None) -> pd.DataFrame:
    records = []
    for p in _scoped(company, domain):
        records.append(
            {
                "company": _normalize_company(p["assignee"]),
                "domain": p["domain"],
                "patent": p["publication_number"],
            }
        )
    return pd.DataFrame(records)


def _build_tfidf_map(company: Optional[str] = None, domain: Optional[str] = None) -> pd.DataFrame:
    patents = _scoped(company, domain)
    if len(patents) < 2:
        return pd.DataFrame()
    try:
        from sklearn.decomposition import PCA
        from sklearn.feature_extraction.text import TfidfVectorizer
    except ImportError:
        return pd.DataFrame()

    titles = [p["title"] for p in patents]
    vectorizer = TfidfVectorizer(stop_words="english", max_features=80)
    matrix = vectorizer.fit_transform(titles)
    n_components = 2 if matrix.shape[0] >= 2 else 1
    coords = PCA(n_components=n_components, random_state=42).fit_transform(matrix.toarray())
    rows = []
    for idx, p in enumerate(patents):
        rows.append(
            {
                "x": float(coords[idx, 0]),
                "y": float(coords[idx, 1]) if coords.shape[1] > 1 else 0.0,
                "title": p["title"],
                "company": _normalize_company(p["assignee"]),
                "domain": p["domain"],
                "id": p["publication_number"],
                "year": p["year"],
            }
        )
    return pd.DataFrame(rows)


def _domain_yearly_counts(domain: str) -> pd.DataFrame:
    patents = [p for p in _patents(domain) if p["domain"] == domain]
    if not patents:
        return pd.DataFrame()
    years = sorted({p["year"] for p in patents})
    counts = [sum(1 for p in patents if p["year"] == y) for y in years]
    return pd.DataFrame({"Years": years, domain: counts})


class PatentService:
    """Doğrulanmış patent verisi servis katmanı."""

    @staticmethod
    def get_companies() -> List[str]:
        return _companies_with_patents()

    @staticmethod
    def get_spec_companies() -> List[str]:
        return list(SPEC_COMPANIES)

    @staticmethod
    def get_data_source() -> str:
        from backend.config import get_lens_token

        if not get_lens_token():
            return "Lens.org (token yok)"
        live_n = len(_live_vendor_patents(None))
        if live_n:
            return f"Lens.org ({live_n} çekilen kayıt)"
        return "Lens.org (yanıt yok)"

    @staticmethod
    def get_summary(company: Optional[str] = None, domain: Optional[str] = None) -> Dict[str, Any]:
        return _compute_summary(company, domain)

    @staticmethod
    def get_company_domain_distribution(company: str) -> Dict[str, float]:
        df = _build_domain_distribution(company)
        row = df[df["Company"] == company]
        if row.empty:
            return {}
        return {col: float(row.iloc[0][col]) for col in TECHNOLOGY_DOMAINS if col in row.columns}

    @staticmethod
    def get_patent_keywords(company: Optional[str] = None, domain: Optional[str] = None) -> Dict[str, int]:
        return _build_keywords(company, domain)

    @staticmethod
    def get_top_patents(company: Optional[str] = None, domain: Optional[str] = None) -> List[Dict[str, Any]]:
        return sorted(
            _scoped(company, domain),
            key=lambda p: (-int(p["year"]), str(p.get("publication_number") or p.get("id") or "")),
        )

    @staticmethod
    def get_network_edges(company: Optional[str] = None, domain: Optional[str] = None) -> List[tuple]:
        return _build_network_edges(company, domain)

    @staticmethod
    def get_company_counts(company: Optional[str] = None, domain: Optional[str] = None) -> Dict[str, int]:
        raw = _compute_summary(company, domain).get("company_counts") or {}
        return {str(k): int(v) for k, v in raw.items() if int(v) > 0}

    @staticmethod
    def get_topic_counts(company: Optional[str] = None, domain: Optional[str] = None) -> Dict[str, int]:
        from backend.patent_apis import key_fingerprint, live_company_topic_matrix, live_topic_or_counts

        axes = tuple([domain] if _norm_domain(domain) else TECHNOLOGY_DOMAINS)
        firms = tuple([company] if company else SPEC_COMPANIES)
        keys = key_fingerprint()
        if company:
            matrix = live_company_topic_matrix(tuple(TECHNOLOGY_DOMAINS), firms, keys)
            row = matrix.get(company) or {}
            return {d: int(row.get(d, 0) or 0) for d in TECHNOLOGY_DOMAINS}
        return {d: int((live_topic_or_counts(axes, firms, keys) or {}).get(d, 0) or 0) for d in axes}

    @staticmethod
    def get_density_df(company: Optional[str] = None, domain: Optional[str] = None) -> pd.DataFrame:
        from backend.patent_apis import key_fingerprint, live_company_topic_matrix

        firms = tuple([company] if company else SPEC_COMPANIES)
        axes = list(TECHNOLOGY_DOMAINS)
        matrix = live_company_topic_matrix(tuple(axes), firms, key_fingerprint())
        rows = []
        for comp in firms:
            row: Dict[str, Any] = {"Company": comp}
            for dname in axes:
                row[dname] = int((matrix.get(comp) or {}).get(dname, 0) or 0)
            rows.append(row)
        return pd.DataFrame(rows)

    @staticmethod
    def get_all_companies_domain_df(
        company: Optional[str] = None, domain: Optional[str] = None
    ) -> pd.DataFrame:
        return PatentService.get_density_df(company, domain)

    @staticmethod
    def get_patent_trends_df(company: Optional[str] = None, domain: Optional[str] = None) -> pd.DataFrame:
        from backend.patent_apis import key_fingerprint, live_company_year_counts

        firms = tuple([company] if company else SPEC_COMPANIES)
        years = tuple(range(2020, 2027))
        raw = live_company_year_counts(domain or "", firms, years, key_fingerprint())
        rows: Dict[str, List[int]] = {"Years": list(years)}
        for comp in firms:
            counts = [int((raw.get(comp) or {}).get(y, 0) or 0) for y in years]
            rows[comp] = counts
        return pd.DataFrame(rows)

    @staticmethod
    def get_sunburst_df(company: Optional[str] = None, domain: Optional[str] = None) -> pd.DataFrame:
        df = PatentService.get_density_df(company, domain)
        if df.empty:
            return pd.DataFrame()
        records = []
        axes = [c for c in df.columns if c != "Company"]
        for _, row in df.iterrows():
            comp = str(row["Company"])
            for dname in axes:
                n = int(row.get(dname) or 0)
                if n <= 0:
                    continue
                records.append({"company": comp, "domain": dname, "n": n})
        return pd.DataFrame(records)

    @staticmethod
    def get_tfidf_map_df(company: Optional[str] = None, domain: Optional[str] = None) -> pd.DataFrame:
        return _build_tfidf_map(company, domain)

    @staticmethod
    def get_domain_yearly_df(tech_id: str) -> pd.DataFrame:
        domain = TECH_ID_TO_DOMAIN.get(tech_id, "")
        if not domain:
            return pd.DataFrame()
        return _domain_yearly_counts(domain)

    @staticmethod
    def domain_for_tech(tech_id: str) -> str:
        return TECH_ID_TO_DOMAIN.get(tech_id, "")
