"""
Türk Telekom 6G Academic Publication Intelligence Service
Provides logic for paper trends, database distributions, top institutions, countries, and citation metrics.
Optimized with Streamlit cache_data.
"""

import streamlit as st
from typing import Dict, List, Any
import pandas as pd
from data.academic import (
    ACADEMIC_SOURCES,
    PUBLICATION_TRENDS_BY_TECH,
    PUBLICATIONS_BY_DATABASE,
    TOP_RESEARCH_INSTITUTIONS,
    TOP_PUBLISHING_COUNTRIES,
    MOST_CITED_PAPERS
)

class AcademicService:
    """Service layer handling academic publication trends and metadata."""

    @staticmethod
    def get_sources() -> List[str]:
        return ACADEMIC_SOURCES

    @staticmethod
    @st.cache_data
    def get_tech_publication_trends_df() -> pd.DataFrame:
        """Returns annual publication trends per 6G technology topic."""
        return pd.DataFrame(PUBLICATION_TRENDS_BY_TECH)

    @staticmethod
    @st.cache_data
    def get_database_distribution() -> Dict[str, float]:
        """Returns publication share per academic indexing database."""
        return PUBLICATIONS_BY_DATABASE

    @staticmethod
    @st.cache_data
    def get_top_institutions() -> List[Dict[str, Any]]:
        """Returns top publishing global research labs and universities."""
        return TOP_RESEARCH_INSTITUTIONS

    @staticmethod
    @st.cache_data
    def get_top_countries() -> Dict[str, float]:
        """Returns global research publication volume share by country."""
        return TOP_PUBLISHING_COUNTRIES

    @staticmethod
    @st.cache_data
    def get_most_cited_papers() -> List[Dict[str, Any]]:
        """Returns benchmark high-citation 6G papers."""
        return MOST_CITED_PAPERS
