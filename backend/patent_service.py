"""
Türk Telekom 6G Patent Intelligence Service
Provides business logic for patent trend analysis, domain distributions, keyword analysis, and NetworkX citation topology.
Optimized with Streamlit cache_data for high performance in cloud deployments.
"""

import streamlit as st
from typing import Dict, List, Any
import pandas as pd
from data.patents import (
    PATENT_COMPANIES,
    TECHNOLOGY_DOMAINS,
    PATENT_TRENDS,
    COMPANY_DOMAIN_DISTRIBUTION,
    PATENT_KEYWORDS,
    TOP_PATENTS_FEED
)

class PatentService:
    """Service layer handling patent intelligence data transformations."""

    @staticmethod
    def get_companies() -> List[str]:
        return PATENT_COMPANIES

    @staticmethod
    @st.cache_data
    def get_patent_trends_df() -> pd.DataFrame:
        """Returns annual patent application trends per company as DataFrame."""
        return pd.DataFrame(PATENT_TRENDS)

    @staticmethod
    def get_company_domain_distribution(company: str) -> Dict[str, float]:
        """Returns percentage breakdown of patents across 6G domains for a company."""
        return COMPANY_DOMAIN_DISTRIBUTION.get(company, {})

    @staticmethod
    @st.cache_data
    def get_all_companies_domain_df() -> pd.DataFrame:
        """Returns domain breakdown matrix across all companies for comparison radar/bar charts."""
        records = []
        for company, dist in COMPANY_DOMAIN_DISTRIBUTION.items():
            row = {"Company": company}
            row.update(dist)
            records.append(row)
        return pd.DataFrame(records)

    @staticmethod
    @st.cache_data
    def get_patent_keywords() -> Dict[str, int]:
        """Returns frequency of keywords in patent claim texts."""
        return PATENT_KEYWORDS

    @staticmethod
    @st.cache_data
    def get_top_patents() -> List[Dict[str, Any]]:
        """Returns curated high-impact patents list."""
        return TOP_PATENTS_FEED
