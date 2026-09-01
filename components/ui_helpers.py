"""Ortak UI bileşenleri — kaynak butonları, boş/hata durumları.

Modül seviyesinde i18n import etmez: Streamlit Cloud (Python 3.14) sayfa
yüklemesinde `from components.ui_helpers import ...` ImportError üretmesin.
"""

from __future__ import annotations

import re
from html import escape
from typing import Optional

import streamlit as st


def _t(key: str, **kwargs) -> str:
    from i18n.core import t

    return t(key, **kwargs)


def _format_int(value):
    from i18n.core import format_int

    return format_int(value)


def render_module_header(title: str, subtitle: str, accent: str = "#0099FF", lead: str = "") -> None:
    """Başlık kartı — alt yazı HTML değil; etiket sızıntısı olmasın."""
    st.markdown(
        f'<div class="glass-card module-header" style="border-left:6px solid {accent};margin-bottom:4px;">'
        f'<h2 class="module-header-title">{title}</h2>'
        f"</div>",
        unsafe_allow_html=True,
    )
    if lead:
        st.markdown(lead)
    if subtitle:
        st.caption(subtitle)


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


def _source_label(source_id: str) -> str:
    return _t(f"sources.open_{source_id}").replace(" ↗", "")


def _link_key(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", text or "")[:48]


def render_source_totals(kind: str, topic: Optional[str], key_suffix: str) -> None:
    """Konu seçimine göre şartname DB toplamı. API yoksa —."""
    from backend.publisher_apis import key_fingerprint
    from backend.source_totals import fetch_pub_source_totals
    from i18n.core import format_int

    if kind == "patent":
        from backend.source_totals import peek_patent_source_totals

        rows = peek_patent_source_totals(topic)
    else:
        rows = fetch_pub_source_totals(topic, key_fingerprint())
    st.caption(_t("sources.totals_caption_pat" if kind == "patent" else "sources.totals_caption_pub"))
    table = []
    config = {}
    open_col = _t("sources.total_col_open")
    for row in rows:
        n = row.get("count")
        table.append(
            {
                _t("sources.total_col_db"): _source_label(row["id"]),
                _t("sources.total_col_n"): format_int(n) if isinstance(n, int) else "—",
                _t("sources.total_col_how"): _t(f"sources.method_{row.get('method') or 'none'}"),
                open_col: row.get("url") or "",
            }
        )
    config[open_col] = st.column_config.LinkColumn(open_col, display_text=_t("sources.total_open_text"))
    st.dataframe(table, hide_index=True, width="stretch", column_config=config, key=f"tot_{kind}_{key_suffix}")


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


def render_patent_card(patent: dict) -> None:
    pub = patent.get("publication_number") or patent.get("id", "")
    from backend.source_links import lens_patent_url, patent_record_links

    url = patent.get("source_url") or patent.get("url") or ""
    if not url and pub:
        url = lens_patent_url(str(pub), str(patent.get("lens_id") or ""))

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
    render_link_row(
        patent_record_links(str(pub), source_url=url, lens_id=str(patent.get("lens_id") or "")),
        key_suffix=_link_key(str(pub)),
    )


def render_paper_card(paper: dict) -> None:
    cites = paper.get("citations")
    if isinstance(cites, int):
        cite_label = _t("pub.citations_n", n=cites)
    else:
        cite_label = _t("pub.citations_na")
    doi = paper.get("doi", "")
    from backend.source_links import paper_record_links

    places = []
    for cc in paper.get("ccs") or []:
        key = f"pub.cc.{cc}"
        label = _t(key)
        if label != key:
            places.append(escape(label))
    place_html = (
        f'<p style="color:#94A3B8;font-size:0.8rem;margin:0 0 4px 0;">{", ".join(places)}</p>'
        if places
        else ""
    )
    title = escape(str(paper.get("title") or ""))
    authors = escape(str(paper.get("authors") or ""))
    journal = escape(str(paper.get("journal") or ""))
    year = escape(str(paper.get("year") or ""))
    doi_esc = escape(str(doi))
    cite_esc = escape(str(cite_label))

    st.markdown(
        (
            '<div class="glass-card" style="margin-bottom: 8px; padding: 16px;">'
            '<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;">'
            f'<h4 style="color:#00E5FF;margin:0;line-height:1.4;overflow-wrap:anywhere;">{title}</h4>'
            f'<span class="trl-pill trl-high" style="white-space:normal;">{cite_esc}</span>'
            "</div>"
            f'<p style="color:#C8D1DC;font-size:0.88rem;margin-top:6px;margin-bottom:4px;overflow-wrap:anywhere;">'
            f"{_t('pub.authors')}: {authors} · {journal} ({year})"
            "</p>"
            f"{place_html}"
            f'<p style="color:#64748B;font-size:0.78rem;margin:0;">DOI: {doi_esc}</p>'
            "</div>"
        ),
        unsafe_allow_html=True,
    )
    render_link_row(
        paper_record_links(
            doi,
            str(paper.get("source") or ""),
        ),
        key_suffix=_link_key(str(doi)),
    )


def show_empty(message: str) -> None:
    st.info(message)


def show_error(message: str) -> None:
    st.error(message)


def current_view_mode() -> str:
    mode = st.session_state.get("view_mode", "beginner")
    if mode in ("beginner", "expert"):
        return mode
    return "expert" if "Uzman" in str(mode) else "beginner"


def render_pub_topic_panel(*args, **kwargs):
    """Python 3.14: eski from ui_helpers import render_pub_topic_panel yolu."""
    from components.topic_panels import render_pub_topic_panel as _impl

    return _impl(*args, **kwargs)


def render_patent_topic_panel(*args, **kwargs):
    from components.topic_panels import render_patent_topic_panel as _impl

    return _impl(*args, **kwargs)


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
    """Tek bölüm seçer. index verilmez: her rerun ilk seçeneğe dönmesin."""
    choice = st.selectbox(label, options, key=key)
    return choice or options[0]


def show_plotly(fig) -> None:
    st.plotly_chart(fig, width="stretch")
