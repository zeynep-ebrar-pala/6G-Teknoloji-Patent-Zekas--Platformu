"""
Patent analitik servisi — source-locked doğrulanmış patent kayıtlarından metrik üretir.
"""

from __future__ import annotations

from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
import streamlit as st

from backend.data_validator import load_validated_patents
from data.patents import PATENT_DATA_SOURCE, SPEC_COMPANIES, TECHNOLOGY_DOMAINS, VERIFIED_PATENTS

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
    "NEC Corporation": "NEC",
    "Intel Corporation": "Intel",
    "InterDigital Patent Holdings Inc.": "InterDigital",
    "Northeastern University": "Northeastern Univ.",
    "AT&T Intellectual Property I, L.P.": "AT&T",
    "Deutsche Telekom AG": "Deutsche Telekom",
    "LG Electronics Inc.": "LG Electronics",
}


def _normalize_company(assignee: str) -> str:
    if assignee in _ASSIGNEE_MAP:
        return _ASSIGNEE_MAP[assignee]
    for key, val in _ASSIGNEE_MAP.items():
        if key.split()[0].lower() in assignee.lower():
            return val
    return assignee.split()[0]


def _patents() -> List[Dict[str, Any]]:
    return load_validated_patents(VERIFIED_PATENTS)


def _with_company(patents: List[Dict[str, Any]], company: Optional[str] = None) -> List[Dict[str, Any]]:
    if not company or company == "Tümü":
        return patents
    return [p for p in patents if _normalize_company(p["assignee"]) == company]


@st.cache_data
def _companies_with_patents() -> List[str]:
    return sorted({_normalize_company(p["assignee"]) for p in _patents()})


@st.cache_data
def _build_patent_trends(company: Optional[str] = None) -> pd.DataFrame:
    patents = _with_company(_patents(), company)
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


@st.cache_data
def _build_domain_distribution(company: Optional[str] = None) -> pd.DataFrame:
    patents = _with_company(_patents(), company)
    records = []
    companies = sorted({_normalize_company(p["assignee"]) for p in patents})
    for comp in companies:
        company_patents = [p for p in patents if _normalize_company(p["assignee"]) == comp]
        if not company_patents:
            continue
        domain_counts = Counter(p["domain"] for p in company_patents)
        total = sum(domain_counts.values())
        row: Dict[str, Any] = {"Company": comp}
        for domain in TECHNOLOGY_DOMAINS:
            row[domain] = round(100 * domain_counts.get(domain, 0) / total, 1)
        records.append(row)
    return pd.DataFrame(records)


@st.cache_data
def _build_keywords(company: Optional[str] = None) -> Dict[str, int]:
    stop = {
        "a", "an", "the", "for", "and", "or", "in", "of", "to", "via", "using",
        "method", "apparatus", "system", "methods", "apparatuses", "based",
        "thereof", "therefor", "with", "from",
    }
    counter: Counter = Counter()
    for p in _with_company(_patents(), company):
        words = p["title"].lower().replace("-", " ").replace("(", " ").replace(")", " ").split()
        for w in words:
            w = w.strip(",.")
            if len(w) > 3 and w not in stop:
                counter[w] += 1
    return dict(counter.most_common(20))


@st.cache_data
def _compute_summary(company: Optional[str] = None) -> Dict[str, Any]:
    patents = _with_company(_patents(), company)
    total = len(patents)
    by_company = Counter(_normalize_company(p["assignee"]) for p in patents)
    leader = by_company.most_common(1)[0] if by_company else ("—", 0)
    by_domain = Counter(p["domain"] for p in patents)
    top_domain = by_domain.most_common(1)[0] if by_domain else ("—", 0)
    return {
        "total": total,
        "leader_company": leader[0],
        "leader_count": leader[1],
        "top_domain": top_domain[0],
        "top_domain_count": top_domain[1],
        "source": PATENT_DATA_SOURCE,
        "company_counts": dict(by_company),
    }


@st.cache_data
def _build_network_edges(company: Optional[str] = None) -> List[Tuple[str, str]]:
    seen: set = set()
    edges: List[Tuple[str, str]] = []
    for p in _with_company(_patents(), company):
        edge = (_normalize_company(p["assignee"]), p["domain"])
        if edge not in seen:
            seen.add(edge)
            edges.append(edge)
    return edges


@st.cache_data
def _build_density_df(company: Optional[str] = None) -> pd.DataFrame:
    patents = _with_company(_patents(), company)
    companies = sorted({_normalize_company(p["assignee"]) for p in patents})
    rows = []
    for comp in companies:
        row = {"Company": comp}
        for domain in TECHNOLOGY_DOMAINS:
            row[domain] = sum(
                1
                for p in patents
                if _normalize_company(p["assignee"]) == comp and p["domain"] == domain
            )
        rows.append(row)
    return pd.DataFrame(rows)


@st.cache_data
def _build_sunburst_df(company: Optional[str] = None) -> pd.DataFrame:
    records = []
    for p in _with_company(_patents(), company):
        records.append(
            {
                "company": _normalize_company(p["assignee"]),
                "domain": p["domain"],
                "patent": p["publication_number"],
            }
        )
    return pd.DataFrame(records)


@st.cache_data
def _build_tfidf_map(company: Optional[str] = None) -> pd.DataFrame:
    patents = _with_company(_patents(), company)
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


@st.cache_data
def _domain_yearly_counts(domain: str) -> pd.DataFrame:
    patents = [p for p in _patents() if p["domain"] == domain]
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
        return PATENT_DATA_SOURCE

    @staticmethod
    def get_summary(company: Optional[str] = None) -> Dict[str, Any]:
        return _compute_summary(company)

    @staticmethod
    def get_patent_trends_df(company: Optional[str] = None) -> pd.DataFrame:
        return _build_patent_trends(company)

    @staticmethod
    def get_company_domain_distribution(company: str) -> Dict[str, float]:
        df = _build_domain_distribution(company)
        row = df[df["Company"] == company]
        if row.empty:
            return {}
        return {col: float(row.iloc[0][col]) for col in TECHNOLOGY_DOMAINS if col in row.columns}

    @staticmethod
    def get_all_companies_domain_df(company: Optional[str] = None) -> pd.DataFrame:
        return _build_domain_distribution(company)

    @staticmethod
    def get_patent_keywords(company: Optional[str] = None) -> Dict[str, int]:
        return _build_keywords(company)

    @staticmethod
    def get_top_patents(company: Optional[str] = None) -> List[Dict[str, Any]]:
        return sorted(_with_company(_patents(), company), key=lambda p: p["year"], reverse=True)

    @staticmethod
    def get_network_edges(company: Optional[str] = None) -> List[tuple]:
        return _build_network_edges(company)

    @staticmethod
    def get_company_counts(company: Optional[str] = None) -> Dict[str, int]:
        return _compute_summary(company).get("company_counts", {})

    @staticmethod
    def get_density_df(company: Optional[str] = None) -> pd.DataFrame:
        return _build_density_df(company)

    @staticmethod
    def get_sunburst_df(company: Optional[str] = None) -> pd.DataFrame:
        return _build_sunburst_df(company)

    @staticmethod
    def get_tfidf_map_df(company: Optional[str] = None) -> pd.DataFrame:
        return _build_tfidf_map(company)

    @staticmethod
    def get_domain_yearly_df(tech_id: str) -> pd.DataFrame:
        domain = TECH_ID_TO_DOMAIN.get(tech_id, "")
        if not domain:
            return pd.DataFrame()
        return _domain_yearly_counts(domain)

    @staticmethod
    def domain_for_tech(tech_id: str) -> str:
        return TECH_ID_TO_DOMAIN.get(tech_id, "")
