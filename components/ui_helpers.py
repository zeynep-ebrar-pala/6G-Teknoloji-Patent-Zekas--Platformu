"""Ortak UI bileşenleri — kaynak butonları, boş/hata durumları."""

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


def render_source_button(url: str, label: str = "Kaynakta Aç ↗") -> None:
    """Orijinal sayfayı yeni sekmede açan gerçek Streamlit butonu."""
    if not url:
        st.caption("Kaynak bağlantısı yok.")
        return
    st.link_button(label, url, use_container_width=True, type="primary")


def render_patent_card(patent: dict) -> None:
    pub = patent.get("publication_number") or patent.get("id", "")
    url = patent.get("source_url") or patent.get("url") or ""
    if pub and not url:
        url = f"https://patents.google.com/patent/{pub}/en"

    st.markdown(
        f"""
        <div class="glass-card" style="margin-bottom: 8px; padding: 18px;">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
                <span style="color:#00E5FF;font-weight:700;font-family:'JetBrains Mono',monospace;">{pub}</span>
                <span class="trl-pill trl-mid">{patent.get('domain','')}</span>
            </div>
            <h4 style="color:#FFFFFF;margin-top:8px;margin-bottom:6px;">{patent['title']}</h4>
            <p style="color:#C8D1DC;font-size:0.88rem;margin-bottom:8px;">{patent.get('abstract','')}</p>
            <p style="color:#94A3B8;font-size:0.8rem;margin:0;">
                Assignee: <strong>{patent.get('assignee','')}</strong> · Yıl: <strong>{patent.get('year','')}</strong>
            </p>
            <p style="color:#64748B;font-size:0.75rem;margin:8px 0 0 0;word-break:break-all;">{url}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_source_button(url, f"{pub} — Google Patents'te Aç ↗")


def render_paper_card(paper: dict) -> None:
    cites = paper.get("citations")
    if isinstance(cites, int):
        cite_label = f"{cites:,} Atıf"
    else:
        cite_label = "Atıf: —"
    doi = paper.get("doi", "")
    url = paper.get("source_url") or paper.get("url") or (f"https://doi.org/{doi}" if doi else "")
    st.markdown(
        f"""
        <div class="glass-card" style="margin-bottom: 8px; padding: 16px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;">
                <h4 style="color:#00E5FF;margin:0;line-height:1.4;">{paper['title']}</h4>
                <span class="trl-pill trl-high" style="white-space:nowrap;">{cite_label}</span>
            </div>
            <p style="color:#C8D1DC;font-size:0.88rem;margin-top:6px;margin-bottom:4px;">
                Yazarlar: {paper.get('authors','')} · {paper.get('journal','')} ({paper.get('year','')})
            </p>
            <p style="color:#64748B;font-size:0.78rem;margin:0;">DOI: {doi}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_source_button(url, "Makaleyi DOI ile Aç ↗")


def show_empty(message: str) -> None:
    st.info(message)


def show_error(message: str) -> None:
    st.error(message)
