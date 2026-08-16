"""Ortak UI bileşenleri — kaynak linkleri, boş/hata durumları."""

from __future__ import annotations

import streamlit as st


def render_module_header(title: str, subtitle: str, accent: str = "#0099FF") -> None:
    st.markdown(
        f"""
        <div class="glass-card" style="border-left: 6px solid {accent}; margin-bottom: 8px;">
            <h2 style="margin: 0; color: #FFF; font-size: 1.45rem;">{title}</h2>
            <p style="color: #C8D1DC; font-size: 0.92rem; margin-top: 6px; margin-bottom: 0;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_source_footer(source: str, source_url: str, link_label: str) -> None:
    """Kaynak bilgisi + tarayıcıda açılan doğrudan link."""
    st.markdown(
        f"""
        <div style="margin-top: 8px; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.08);
             font-size: 0.82rem; color: #94A3B8;">
            <strong>Source:</strong> {source} ·
            <a href="{source_url}" target="_blank" rel="noopener noreferrer"
               style="color:#00E5FF; font-weight:600; text-decoration:none;
               border-bottom:1px solid rgba(0,229,255,0.35);">{link_label}</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_patent_card(patent: dict) -> None:
    pub = patent["publication_number"]
    st.markdown(
        f"""
        <div class="glass-card" style="margin-bottom: 14px; padding: 18px;">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
                <span style="color:#00E5FF;font-weight:700;font-family:'JetBrains Mono',monospace;">{pub}</span>
                <span class="trl-pill trl-mid">{patent.get('domain','')}</span>
            </div>
            <h4 style="color:#FFFFFF;margin-top:8px;margin-bottom:6px;">{patent['title']}</h4>
            <p style="color:#C8D1DC;font-size:0.88rem;margin-bottom:8px;">{patent.get('abstract','')}</p>
            <p style="color:#94A3B8;font-size:0.8rem;margin:0;">
                Assignee: <strong>{patent.get('assignee','')}</strong> · Yıl: <strong>{patent.get('year','')}</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_source_footer(patent["source"], patent["source_url"], "Kaynakta Aç ↗")


def render_paper_card(paper: dict) -> None:
    cites = paper.get("citations")
    if isinstance(cites, int):
        cite_label = f"{cites:,} Atıf"
    else:
        cite_label = "Atıf: —"
    st.markdown(
        f"""
        <div class="glass-card" style="margin-bottom: 12px; padding: 16px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;">
                <h4 style="color:#00E5FF;margin:0;line-height:1.4;">{paper['title']}</h4>
                <span class="trl-pill trl-high" style="white-space:nowrap;">{cite_label}</span>
            </div>
            <p style="color:#C8D1DC;font-size:0.88rem;margin-top:6px;margin-bottom:4px;">
                Yazarlar: {paper.get('authors','')} · {paper.get('journal','')} ({paper.get('year','')})
            </p>
            <p style="color:#64748B;font-size:0.78rem;margin:0;">DOI: {paper.get('doi','')}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_source_footer(paper["source"], paper["source_url"], "Makaleyi Kaynakta Aç ↗")


def show_empty(message: str) -> None:
    st.info(message)


def show_error(message: str) -> None:
    st.error(message)
