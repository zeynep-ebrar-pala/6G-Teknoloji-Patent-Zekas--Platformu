"""
Modül 2 — Patent Zekası ve Rakip Analizi arayüzü.
Tüm patent kayıtları Google Patents üzerinden doğrulanabilir.
"""

import streamlit as st

from backend.patent_service import PatentService
from i18n.core import format_int, get_lang, t
from components.charts import (
    render_company_counts_chart,
    render_company_patent_domain_chart,
    render_patent_density_heatmap,
    render_patent_keywords_chart,
    render_patent_network_graph,
    render_patent_sunburst,
    render_patent_tfidf_map,
    render_patent_trends_chart,
    render_patent_wordcloud,
)
from components.ui_helpers import (
    render_link_row,
    render_mixed_topic_panel,
    render_module_header,
    render_patent_card,
    render_source_button,
    render_spec_patent_sources,
    select_section,
    show_empty,
    show_plotly,
)
from components.tt_europe_views import render_tt_europe_patent_section

PATENT_SECTION_KEYS = ["tt_eu", "year", "topics", "tree", "map", "list"]


def render_patent_intelligence_module():
    render_module_header(
        t("patent.title"),
        t("patent.subtitle", source=PatentService.get_data_source()),
    )

    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("patent.what_title")}</div>
{t("patent.what_body")}
</div>""",
        unsafe_allow_html=True,
    )

    render_spec_patent_sources()
    render_mixed_topic_panel("patent")
    from backend.source_links import assignee_patent_links

    spec = PatentService.get_spec_companies()
    filter_options = ["all"] + spec
    company = st.selectbox(
        t("patent.filter"),
        options=filter_options,
        index=0,
        format_func=lambda x: t("patent.all") if x == "all" else x,
        key="patent_company_filter",
    )
    company_arg = None if company == "all" else company

    summary = PatentService.get_summary(company_arg)
    patents = PatentService.get_top_patents(company_arg)

    if not patents:
        show_empty(t("patent.empty_company", company=company if company != "all" else t("patent.all")))
        return

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(t("patent.metric_total"), format_int(summary["total"]))
    with col2:
        st.metric(
            t("patent.metric_leader"),
            summary["leader_company"],
            t("patent.metric_leader_delta", n=format_int(summary["leader_count"])),
        )
    with col3:
        st.metric(
            t("patent.metric_domain"),
            summary["top_domain"],
            t("patent.metric_domain_delta", n=format_int(summary["top_domain_count"])),
        )
    with col4:
        st.metric(t("patent.metric_source"), t("sources.patent_metric"))
    if company_arg:
        st.caption(t("sources.assignee_caption", company=company_arg))
        render_link_row(assignee_patent_links(company_arg))
    else:
        render_source_button("https://patents.google.com", t("patent.open_gp"))

    st.divider()

    _labels = [t(f"patent.section.{k}") for k in PATENT_SECTION_KEYS]
    _map = dict(zip(_labels, PATENT_SECTION_KEYS))
    section = _map.get(
        select_section(t("patent.view"), _labels, key=f"patent_section_eu1_{get_lang()}"),
        PATENT_SECTION_KEYS[0],
    )

    if section == "year":
        st.markdown(t("patent.year_heading"))
        st.caption(t("patent.year_caption"))
        df_trends = PatentService.get_patent_trends_df(company_arg)
        if df_trends.empty:
            show_empty(t("patent.empty_trend"))
        else:
            show_plotly(render_patent_trends_chart(df_trends))

        st.markdown(t("patent.companies_heading"))
        counts = PatentService.get_company_counts(company_arg)
        if not counts:
            show_empty(t("patent.empty_counts"))
        else:
            show_plotly(render_company_counts_chart(counts))

    elif section == "topics":
        col_radar, col_kw = st.columns([1.2, 1])
        with col_radar:
            df_domains = PatentService.get_all_companies_domain_df(company_arg)
            if df_domains.empty:
                show_empty(t("patent.empty_domain"))
            else:
                show_plotly(render_company_patent_domain_chart(df_domains))

        with col_kw:
            kw_dict = PatentService.get_patent_keywords(company_arg)
            if not kw_dict:
                show_empty(t("patent.empty_kw"))
            else:
                show_plotly(render_patent_keywords_chart(kw_dict))

        st.markdown(t("patent.wordcloud"))
        st.caption(t("patent.wordcloud_caption"))
        kw_dict = PatentService.get_patent_keywords(company_arg)
        wc_fig = render_patent_wordcloud(kw_dict) if kw_dict else None
        if wc_fig is None:
            show_empty(t("patent.empty_wc"))
        else:
            st.pyplot(wc_fig, clear_figure=True)

    elif section == "tree":
        st.markdown(t("patent.density"))
        df_density = PatentService.get_density_df(company_arg)
        if df_density.empty:
            show_empty(t("patent.empty_density"))
        else:
            show_plotly(render_patent_density_heatmap(df_density))

        st.markdown(t("patent.tree_heading"))
        df_tree = PatentService.get_sunburst_df(company_arg)
        if df_tree.empty:
            show_empty(t("patent.empty_tree"))
        else:
            show_plotly(render_patent_sunburst(df_tree))

    elif section == "map":
        st.markdown(t("patent.map_heading"))
        st.caption(t("patent.map_caption"))
        df_map = PatentService.get_tfidf_map_df(company_arg)
        if df_map.empty:
            show_empty(t("patent.empty_map"))
        else:
            show_plotly(render_patent_tfidf_map(df_map))

        st.markdown(t("patent.network"))
        edges = PatentService.get_network_edges(company_arg)
        if not edges:
            show_empty(t("patent.empty_net"))
        else:
            show_plotly(render_patent_network_graph(edges))

    elif section == "tt_eu":
        render_tt_europe_patent_section()

    else:
        st.markdown(t("patent.list_heading"))
        st.caption(t("patent.list_caption"))
        for pat in patents:
            render_patent_card(pat)
