"""
Modül 3 — Akademik Yayın Analizi arayüzü.
DOI doğrulamalı set her zaman doludur; OpenAlex canlı/önbellek varsa eklenir.
"""

import streamlit as st

from backend.academic_service import AcademicService
from i18n.core import format_int, get_lang, t
from components.charts import (
    render_academic_bar_chart,
    render_academic_database_chart,
    render_academic_trends_chart,
)
from components.ui_helpers import (
    render_module_header,
    render_paper_card,
    render_pub_topic_panel,
    render_source_button,
    render_spec_pub_sources,
    select_section,
    show_empty,
    show_plotly,
)
from components.tt_europe_views import render_tt_europe_pub_section

PUB_SECTION_KEYS = ["tt_eu", "doi", "trend", "inst", "country", "papers"]


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

    summary = AcademicService.get_summary(topic)
    papers = AcademicService.get_most_cited_papers(topic)

    year_label = summary.get("latest_year") or "—"
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(t("pub.metric_doi"), format_int(summary["verified_paper_count"]))
    with c2:
        val = format_int(summary["total_latest_year"]) if summary.get("total_latest_year") is not None else "—"
        st.metric(t("pub.metric_oa_year", year=year_label), val)
    with c3:
        topic_delta = format_int(summary["top_topic_count"]) if summary.get("top_topic_count") else None
        st.metric(t("pub.metric_topic"), summary["top_topic"], topic_delta)
    with c4:
        cites = summary.get("top_paper_citations")
        st.metric(t("pub.metric_cites"), format_int(cites) if isinstance(cites, int) else "—")

    render_source_button(summary.get("openalex_url") or "https://openalex.org/works", t("pub.open_oa"))
    if summary.get("snapshot_at"):
        st.caption(t("pub.snapshot", ts=summary["snapshot_at"]))

    st.divider()

    _labels = [t(f"pub.section.{k}") for k in PUB_SECTION_KEYS]
    _map = dict(zip(_labels, PUB_SECTION_KEYS))
    section = _map.get(
        select_section(t("pub.view"), _labels, key=f"academic_section_eu1_{get_lang()}"),
        PUB_SECTION_KEYS[0],
    )

    if section == "tt_eu":
        render_tt_europe_pub_section(topic)
        return

    if not papers:
        show_empty(t("pub.empty_topic", topic=topic) if topic else t("pub.empty"))
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
        st.markdown(t("pub.oa_heading"))
        st.caption(t("pub.oa_caption"))
        df_acad = AcademicService.get_tech_publication_trends_df(topic)
        if df_acad is None or df_acad.empty:
            show_empty(t("pub.oa_empty"))
            render_source_button("https://openalex.org/works", t("pub.try_oa"))
        else:
            show_plotly(render_academic_trends_chart(df_acad))
            render_source_button("https://openalex.org/works", t("pub.open_oa_counts"))

    elif section == "inst":
        st.markdown(t("pub.inst_heading"))
        if topic:
            verified_inst = AcademicService.get_verified_institutions(topic)
            if verified_inst:
                st.caption(t("pub.inst_fallback"))
                show_plotly(render_academic_bar_chart(verified_inst, t("pub.chart_inst_fb")))
            else:
                show_empty(t("pub.empty_inst"))
        else:
            institutions = AcademicService.get_top_institutions()
            if institutions:
                st.caption(t("pub.oa_groupby"))
                show_plotly(render_academic_bar_chart(institutions, t("pub.chart_inst")))
                render_source_button("https://openalex.org/works", t("pub.open_inst"))
            else:
                verified_inst = AcademicService.get_verified_institutions()
                if verified_inst:
                    st.caption(t("pub.inst_fallback"))
                    show_plotly(render_academic_bar_chart(verified_inst, t("pub.chart_inst_fb")))
                else:
                    show_empty(t("pub.empty_inst"))

    elif section == "country":
        st.markdown(t("pub.cc_heading"))
        if topic:
            verified_cc = AcademicService.get_verified_countries(topic)
            if verified_cc:
                st.caption(t("pub.cc_fallback"))
                show_plotly(render_academic_bar_chart(verified_cc, t("pub.chart_cc_fb")))
            else:
                show_empty(t("pub.empty_cc"))
        else:
            countries = AcademicService.get_top_countries()
            if countries:
                st.caption(t("pub.oa_groupby"))
                show_plotly(render_academic_bar_chart(countries, t("pub.chart_cc")))
                render_source_button("https://openalex.org/works", t("pub.open_cc"))
            else:
                verified_cc = AcademicService.get_verified_countries()
                if verified_cc:
                    st.caption(t("pub.cc_fallback"))
                    show_plotly(render_academic_bar_chart(verified_cc, t("pub.chart_cc_fb")))
                else:
                    show_empty(t("pub.empty_cc"))

    else:
        st.markdown(t("pub.papers_heading"))
        st.caption(t("pub.papers_caption"))
        for paper in papers:
            render_paper_card(paper)
