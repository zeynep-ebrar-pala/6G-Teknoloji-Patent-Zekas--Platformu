"""Ortak UI bileşenleri — kaynak butonları, boş/hata durumları, i18n."""

from __future__ import annotations

import streamlit as st

from i18n.core import format_int, get_lang, t


def render_module_header(title: str, subtitle: str, accent: str = "#0099FF") -> None:
    st.markdown(
        f"""
        <div class="glass-card" style="border-left: 6px solid {accent}; margin-bottom: 8px;">
            <h2 style="margin: 0; color: #FFF; font-size: 1.45rem; overflow-wrap: anywhere;">{title}</h2>
            <p style="color: #C8D1DC; font-size: 0.92rem; margin-top: 6px; margin-bottom: 0; overflow-wrap: anywhere;">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_source_button(url: str, label: str | None = None) -> None:
    """Orijinal sayfayı yeni sekmede açan gerçek Streamlit butonu."""
    if not url:
        st.caption(t("ui.no_source"))
        return
    st.link_button(label or t("ui.source"), url, width="stretch", type="primary")


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
            <h4 style="color:#FFFFFF;margin-top:8px;margin-bottom:6px;overflow-wrap:anywhere;">{patent['title']}</h4>
            <p style="color:#C8D1DC;font-size:0.88rem;margin-bottom:8px;overflow-wrap:anywhere;">{patent.get('abstract','')}</p>
            <p style="color:#94A3B8;font-size:0.8rem;margin:0;">
                {t("patent.assignee")}: <strong>{patent.get('assignee','')}</strong> · {t("patent.year")}: <strong>{patent.get('year','')}</strong>
            </p>
            <p style="color:#64748B;font-size:0.75rem;margin:8px 0 0 0;word-break:break-all;">{url}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_source_button(url, t("patent.open_record", pub=pub))


def render_paper_card(paper: dict) -> None:
    cites = paper.get("citations")
    if isinstance(cites, int):
        cite_label = t("pub.citations_n", n=format_int(cites))
    else:
        cite_label = t("pub.citations_na")
    doi = paper.get("doi", "")
    url = paper.get("source_url") or paper.get("url") or (f"https://doi.org/{doi}" if doi else "")
    st.markdown(
        f"""
        <div class="glass-card" style="margin-bottom: 8px; padding: 16px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;">
                <h4 style="color:#00E5FF;margin:0;line-height:1.4;overflow-wrap:anywhere;">{paper['title']}</h4>
                <span class="trl-pill trl-high" style="white-space:normal;">{cite_label}</span>
            </div>
            <p style="color:#C8D1DC;font-size:0.88rem;margin-top:6px;margin-bottom:4px;overflow-wrap:anywhere;">
                {t("pub.authors")}: {paper.get('authors','')} · {paper.get('journal','')} ({paper.get('year','')})
            </p>
            <p style="color:#64748B;font-size:0.78rem;margin:0;">DOI: {doi}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_source_button(url, t("pub.open_doi"))


def show_empty(message: str) -> None:
    st.info(message)


def show_error(message: str) -> None:
    st.error(message)


def current_view_mode() -> str:
    mode = st.session_state.get("view_mode", "beginner")
    if mode in ("beginner", "expert"):
        return mode
    return "expert" if "Uzman" in str(mode) else "beginner"


def first_text(*vals) -> str:
    """Kart/HTML alanlarında None veya boş string basılmasını önler."""
    for val in vals:
        if val is None:
            continue
        text = str(val).strip()
        if text and text.lower() != "none":
            return text
    return ""


def select_section(label: str, options: list[str], key: str) -> str:
    """Tek bölüm seçer; st.tabs gibi görünmeyen sekmelerin hepsini çalıştırmaz."""
    choice = st.pills(label, options, default=options[0], key=key)
    return choice or options[0]


def select_keyed_section(label: str, keys: list[str], key: str, prefix: str) -> str:
    """Sabit anahtarlarla bölüm seçer; dil değişince etiketler yenilenir, seçim sıfırlanabilir."""
    labels = [t(f"{prefix}.{k}") for k in keys]
    mapping = dict(zip(labels, keys))
    widget_key = f"{key}_{get_lang()}"
    choice = st.pills(label, labels, default=labels[0], key=widget_key)
    return mapping.get(choice or labels[0], keys[0])


def show_plotly(fig) -> None:
    st.plotly_chart(fig, width="stretch")
