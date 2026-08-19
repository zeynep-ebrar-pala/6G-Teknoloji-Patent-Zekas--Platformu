"""
Modül 3 — Akademik Yayın Analizi arayüzü.
DOI kilitli set tam sayı olarak çizilir. Google Scholar kayıt araması açılır; sayım API’si yoktur.
"""

import streamlit as st

from backend.academic_service import AcademicService
from i18n.core import format_int, get_lang, t
from components.charts import (
    render_academic_bar_chart,
    render_academic_database_chart,
)
from components.ui_helpers import (
    render_link_row,
    render_module_header,
    render_paper_card,
    render_spec_pub_sources,
    select_section,
    show_empty,
    show_plotly,
)
from components.topic_panels import render_pub_topic_panel
from components.tt_europe_views import render_tt_europe_pub_section

PUB_SECTION_KEYS = ["doi", "trend", "where", "tt_eu"]


def render_academic_publication_module():
    render_module_header(
        t("pub.title"),
        t("pub.subtitle", source=AcademicService.get_data_source()),
        accent="#00C2FF",
    )

    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("pub.what_title")}</div>
{t("pub.what_body")}
</div>""",
        unsafe_allow_html=True,
    )

    render_spec_pub_sources()
    topic = render_pub_topic_panel("pub")

    papers = AcademicService.get_most_cited_papers(topic)
    year_counts = AcademicService.get_verified_year_counts(topic)
    topic_counts = AcademicService.get_verified_topic_counts(topic)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(t("pub.metric_doi"), format_int(len(papers)))
    with col2:
        peak_year, peak_n = "—", "—"
        if year_counts:
            peak_year = max(year_counts, key=lambda y: year_counts[y])
            peak_n = format_int(year_counts[peak_year])
        st.metric(t("pub.metric_peak_year"), peak_year, t("pub.metric_peak_delta", n=peak_n) if peak_n != "—" else None)
    with col3:
        top_topic, top_n = "—", None
        if topic_counts:
            top_topic = max(topic_counts, key=topic_counts.get)
            top_n = format_int(topic_counts[top_topic])
        st.metric(t("pub.metric_topic"), top_topic, t("pub.metric_topic_delta", n=top_n) if top_n else None)
    with col4:
        st.metric(t("pub.metric_cites"), "—")
    st.caption(t("pub.scholar_metric_caption"))
    from backend.source_links import topic_pub_searches

    scholar = [item for item in topic_pub_searches(topic or "6G") if item.get("id") == "scholar"]
    if scholar:
        render_link_row(scholar, key_suffix=f"pub_scholar_{topic or 'all'}")

    st.markdown(t("pub.papers_heading"))
    st.caption(t("pub.papers_caption"))
    if not papers:
        show_empty(t("pub.empty_topic", topic=topic) if topic else t("pub.empty"))
    else:
        for paper in papers:
            render_paper_card(paper)

    st.divider()

    _labels = [t(f"pub.section.{k}") for k in PUB_SECTION_KEYS]
    _map = dict(zip(_labels, PUB_SECTION_KEYS))
    section = _map.get(
        select_section(t("pub.view"), _labels, key=f"academic_section_story_{get_lang()}"),
        PUB_SECTION_KEYS[0],
    )

    if section == "tt_eu":
        render_tt_europe_pub_section(topic)
        return

    if not papers:
        return

    if section == "doi":
        st.markdown(t("pub.doi_heading"))
        st.caption(t("pub.doi_caption"))
        year_counts = AcademicService.get_verified_year_counts(topic)
        topic_counts = AcademicService.get_verified_topic_counts(topic)
        db_dist = AcademicService.get_database_distribution(topic)
        col_y, col_t = st.columns(2)
        with col_y:
            if year_counts:
                show_plotly(
                    render_academic_database_chart(year_counts, t("pub.chart_year"), t("pub.chart_year_x"))
                )
            else:
                show_empty(t("pub.empty_year"))
        with col_t:
            if topic_counts:
                show_plotly(
                    render_academic_bar_chart(
                        [{"name": k, "count": v} for k, v in topic_counts.items()],
                        t("pub.chart_topic"),
                    )
                )
        if db_dist:
            show_plotly(render_academic_database_chart(db_dist, t("pub.chart_publisher")))

    elif section == "trend":
        st.markdown(t("pub.scholar_heading"))
        st.caption(t("pub.scholar_caption"))
        if year_counts:
            show_plotly(
                render_academic_database_chart(year_counts, t("pub.chart_year"), t("pub.chart_year_x"))
            )
        else:
            show_empty(t("pub.empty_year"))
        from backend.source_links import topic_pub_searches as _pub_s

        render_link_row(_pub_s(topic or "6G"), key_suffix=f"pub_trend_{topic or 'all'}")

    else:
        st.markdown(t("pub.inst_heading"))
        st.caption(t("pub.inst_fallback"))
        verified_inst = AcademicService.get_verified_institutions(topic)
        if verified_inst:
            show_plotly(render_academic_bar_chart(verified_inst, t("pub.chart_inst_fb")))
        else:
            show_empty(t("pub.empty_inst"))

        st.markdown(t("pub.cc_heading"))
        st.caption(t("pub.cc_fallback"))
        verified_cc = AcademicService.get_verified_countries(topic)
        if verified_cc:
            show_plotly(render_academic_bar_chart(verified_cc, t("pub.chart_cc_fb")))
        else:
            show_empty(t("pub.empty_cc"))
