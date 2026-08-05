"""
Türk Telekom 6G Platform - Backend Data Service Layer
Cached for maximum Streamlit Cloud performance and zero-re-render latency.
"""

import streamlit as st
from data.technologies import TECHNOLOGIES

class DataService:
    """Backend Data Access Service for 6G Knowledge Base."""

    @staticmethod
    @st.cache_data
    def get_all_technologies() -> dict:
        """Returns all 7 6G technologies."""
        return TECHNOLOGIES

    @staticmethod
    @st.cache_data
    def get_technology_by_id(tech_id: str) -> dict:
        """Retrieves a specific technology by its unique ID."""
        return TECHNOLOGIES.get(tech_id, None)

    @staticmethod
    @st.cache_data
    def filter_technologies_by_trl(min_trl: int, max_trl: int) -> dict:
        """Filters technologies within a specific TRL range."""
        return {
            t_id: data for t_id, data in TECHNOLOGIES.items()
            if min_trl <= data.get("trl", 0) <= max_trl
        }

    @staticmethod
    def search_technologies(query: str) -> dict:
        """Searches technologies by keyword across titles, summaries, and use cases."""
        query_lower = query.lower()
        results = {}
        for t_id, data in TECHNOLOGIES.items():
            content_str = f"{data['title']} {data['acronym']} {data['executive_summary']} {' '.join(data['use_cases'])}".lower()
            if query_lower in content_str:
                results[t_id] = data
        return results
