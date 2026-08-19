"""Ortak UI bileşenleri — kaynak butonları, boş/hata durumları.

Modül seviyesinde i18n import etmez: Streamlit Cloud (Python 3.14) sayfa
yüklemesinde `from components.ui_helpers import ...` ImportError üretmesin.
"""

from __future__ import annotations

import streamlit as st


def _t(key: str, **kwargs) -> str:
    from i18n.core import t

    return t(key, **kwargs)


def _format_int(value):
    from i18n.core import format_int

    return format_int(value)


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
        st.caption(_t("ui.no_source"))
        return
    st.link_button(label or _t("ui.source"), url, width="stretch", type="primary")


def render_link_row(
    links: list[dict],
    *,
    label_prefix: str = "sources.open_",
    key_suffix: str = "",
) -> None:
    """Şartname veritabanı butonları. URL yoksa basılmaz; sayı uydurulmaz."""
    usable = [item for item in links if item.get("url") and item.get("id")]
    if not usable:
        return
    cols = st.columns(len(usable))
    for col, item in zip(cols, usable):
        with col:
            kwargs = {"width": "stretch"}
            if key_suffix:
                kwargs["key"] = f"lnk_{label_prefix}{item['id']}_{key_suffix}"
            st.link_button(
                _t(f"{label_prefix}{item['id']}"),
                item["url"],
                **kwargs,
            )


def render_spec_patent_sources() -> None:
    from backend.source_links import spec_patent_databases

    st.markdown(_t("sources.patent_heading"))
    st.caption(_t("sources.patent_caption"))
    render_link_row(spec_patent_databases(), key_suffix="pat_home")


def render_spec_pub_sources() -> None:
    from backend.source_links import spec_pub_databases

    st.markdown(_t("sources.pub_heading"))
    st.caption(_t("sources.pub_caption"))
    render_link_row(spec_pub_databases(), key_suffix="pub_home")


def render_patent_topic_panel(key_suffix: str = "pat") -> str | None:
    """Konu seçimi kilitli patent kümesini ve ofis aramasını birlikte değiştirir."""
    from backend.source_links import SPEC_PUB_TOPICS, topic_patent_searches
    from i18n.core import get_lang

    st.markdown(_t("sources.topic_pat_heading"))
    st.caption(_t("sources.topic_pat_caption"))
    options = ["all"] + list(SPEC_PUB_TOPICS.keys())
    topic = st.selectbox(
        _t("sources.topic_search"),
        options,
        format_func=lambda x: _t("sources.topic_all") if x == "all" else x,
        key=f"spec_pat_topic_{key_suffix}_{get_lang()}",
    )
    if topic == "all":
        st.caption(_t("sources.topic_all_caption"))
        render_link_row(topic_patent_searches("6G"), key_suffix=f"{key_suffix}_all")
        return None
    st.caption(_t("sources.topic_result_caption", topic=topic, q=SPEC_PUB_TOPICS[topic]))
    render_link_row(topic_patent_searches(topic), key_suffix=f"{key_suffix}_{topic}")
    return topic


def render_pub_topic_panel(key_suffix: str = "pub") -> str | None:
    """Konu seçimi kilitli makale kümesini ve yayın aramasını birlikte değiştirir."""
    from backend.source_links import SPEC_PUB_TOPICS, topic_pub_searches
    from i18n.core import get_lang

    st.markdown(_t("sources.topic_pub_heading"))
    st.caption(_t("sources.topic_pub_caption"))
    options = ["all"] + list(SPEC_PUB_TOPICS.keys())
    topic = st.selectbox(
        _t("sources.topic_search"),
        options,
        format_func=lambda x: _t("sources.topic_all") if x == "all" else x,
        key=f"spec_pub_topic_{key_suffix}_{get_lang()}",
    )
    if topic == "all":
        st.caption(_t("sources.topic_all_caption_pub"))
        render_link_row(topic_pub_searches("6G"), key_suffix=f"{key_suffix}_all")
        return None
    st.caption(_t("sources.topic_result_caption_pub", topic=topic, q=SPEC_PUB_TOPICS[topic]))
    render_link_row(topic_pub_searches(topic), key_suffix=f"{key_suffix}_{topic}")
    return topic


def render_patent_card(patent: dict) -> None:
    pub = patent.get("publication_number") or patent.get("id", "")
    from backend.source_links import google_patents_record_url

    url = patent.get("source_url") or patent.get("url") or ""
    if not url and pub:
        url = google_patents_record_url(pub)
    if url and "ppubs.uspto.gov" in url:
        url = google_patents_record_url(pub)

    st.markdown(
        f"""
        <div class="glass-card" style="margin-bottom: 8px; padding: 18px;">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
                <span style="color:#00E5FF;font-weight:700;font-family:'JetBrains Mono',monospace;">{patent.get('year','')} · {pub}</span>
                <span class="trl-pill trl-mid">{patent.get('domain','')}</span>
            </div>
            <h4 style="color:#FFFFFF;margin-top:8px;margin-bottom:6px;overflow-wrap:anywhere;">{patent['title']}</h4>
            <p style="color:#C8D1DC;font-size:0.88rem;margin-bottom:8px;overflow-wrap:anywhere;">{patent.get('abstract','')}</p>
            <p style="color:#94A3B8;font-size:0.8rem;margin:0;">
                {_t("patent.assignee")}: <strong>{patent.get('assignee','')}</strong> · {_t("patent.year")}: <strong>{patent.get('year','')}</strong>
            </p>
            <p style="color:#64748B;font-size:0.75rem;margin:8px 0 0 0;word-break:break-all;">{url}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_source_button(url, _t("patent.open_record", pub=pub))


def render_paper_card(paper: dict) -> None:
    cites = paper.get("citations")
    if isinstance(cites, int):
        cite_label = _t("pub.citations_n", n=_format_int(cites))
    else:
        cite_label = _t("pub.citations_na")
    doi = paper.get("doi", "")
    from backend.source_links import doi_url as _doi_url

    url = paper.get("source_url") or paper.get("url") or _doi_url(doi)
    st.markdown(
        f"""
        <div class="glass-card" style="margin-bottom: 8px; padding: 16px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;">
                <h4 style="color:#00E5FF;margin:0;line-height:1.4;overflow-wrap:anywhere;">{paper['title']}</h4>
                <span class="trl-pill trl-high" style="white-space:normal;">{cite_label}</span>
            </div>
            <p style="color:#C8D1DC;font-size:0.88rem;margin-top:6px;margin-bottom:4px;overflow-wrap:anywhere;">
                {_t("pub.authors")}: {paper.get('authors','')} · {paper.get('journal','')} ({paper.get('year','')})
            </p>
            <p style="color:#64748B;font-size:0.78rem;margin:0;">DOI: {doi}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_source_button(url, _t("pub.open_doi"))


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
    """Tek bölüm seçer. selectbox bütün seçenekleri gösterir; haplar uzun etiketleri keser."""
    choice = st.selectbox(label, options, index=0, key=key)
    return choice or options[0]


def show_plotly(fig) -> None:
    st.plotly_chart(fig, width="stretch")
