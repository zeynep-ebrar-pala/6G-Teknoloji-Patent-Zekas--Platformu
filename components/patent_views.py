"""
Modül 2 — Patent Zekası ve Rakip Analizi arayüzü.
Grafikler Lens.org toplamı / çekilen kayıttır. Kilitli örnek yok.
"""

import streamlit as st

from backend.patent_service import PatentService, sort_patent_rows
from data.app_build import APP_BUILD
from i18n.core import format_int, t
from components.charts import (
    render_company_counts_chart,
    render_company_patent_domain_chart,
    render_patent_density_heatmap,
    render_patent_sunburst,
    render_patent_tfidf_map,
    render_patent_trends_chart,
    render_patent_topic_mix_chart,
    render_patent_wordcloud,
)

from components.ui_helpers import (
    current_view_mode,
    render_link_row,
    render_module_header,
    render_patent_card,
    render_source_button,
    render_spec_patent_sources,
    show_empty,
    show_plotly,
)
from components.topic_panels import render_patent_topic_panel


def _lens_token_box() -> None:
    from backend.config import get_lens_token

    if get_lens_token():
        return
    st.warning(t("patent.token_missing"))
    entered = st.text_input(t("patent.token_label"), type="password", key="lens_token_box")
    st.caption(t("patent.token_help"))
    if entered.strip():
        st.session_state["lens_token"] = entered.strip()
        st.rerun()
    st.link_button(t("patent.key_lens"), "https://www.lens.org/lens/user/subscriptions")


def render_patent_intelligence_module():
    render_module_header(
        t("patent.title"),
        t("patent.subtitle", source=PatentService.get_data_source()),
    )
    st.caption(t("patent.tt_eu_build", build=APP_BUILD))

    st.markdown(f"**{t('patent.what_title')}**")
    st.markdown(t("patent.what_body"))
    st.markdown(f"**{t('patent.access_title')}**")
    st.markdown(t("patent.access_body"))
    if current_view_mode() == "expert":
        with st.expander(t("patent.expert_title"), expanded=False):
            st.markdown(t("patent.expert_body"))
        st.link_button(t("patent.key_lens"), "https://www.lens.org/lens/user/subscriptions")

    _lens_token_box()
    render_spec_patent_sources()
    topic = render_patent_topic_panel("patent")

    from backend.patent_apis import key_fingerprint, lens_last_error, live_assignee_counts
    from backend.source_links import assignee_patent_links
    from data.patents import TECHNOLOGY_DOMAINS

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
    keys = key_fingerprint()

    with st.spinner(t("patent.live_gp_spin")):
        xhr_totals = live_assignee_counts(
            topic or "",
            tuple(spec) if not company_arg else (company_arg,),
            keys,
        )
        topic_counts = PatentService.get_topic_counts(company_arg, topic)
        df_density = PatentService.get_density_df(company_arg, topic)
        df_trends = PatentService.get_patent_trends_df(company_arg, topic)
        patents = sort_patent_rows(PatentService.get_top_patents(company_arg, topic))

    api_err = lens_last_error()
    if api_err:
        st.warning(t("patent.api_error", detail=str(api_err).replace("{", "(").replace("}", ")")))

    firm_names = [company_arg] if company_arg else list(spec)
    firm_counts = {
        name: int(xhr_totals[name]) if isinstance(xhr_totals.get(name), int) else 0
        for name in firm_names
    }
    if firm_counts and any(firm_counts.values()):
        leader_company, leader_count = max(firm_counts.items(), key=lambda kv: kv[1])
    else:
        leader_company, leader_count = "—", 0
    if topic_counts and any(int(v) > 0 for v in topic_counts.values()):
        top_domain, top_domain_count = max(topic_counts.items(), key=lambda kv: int(kv[1]))
    else:
        top_domain, top_domain_count = "—", 0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(t("patent.metric_pulled"), format_int(len(patents)))
    with col2:
        st.metric(
            t("patent.metric_leader"),
            leader_company,
            t("patent.metric_leader_delta", n=format_int(leader_count)),
        )
    with col3:
        st.metric(
            t("patent.metric_domain"),
            top_domain,
            t("patent.metric_domain_delta", n=format_int(top_domain_count)),
        )
    with col4:
        st.metric(t("patent.metric_source"), t("sources.patent_metric"))
    st.caption(t("patent.pulled_caption"))
    if company_arg:
        st.caption(t("sources.assignee_caption", company=company_arg))
        render_link_row(assignee_patent_links(company_arg), key_suffix=f"asg_{company_arg}")
    else:
        render_source_button("https://www.lens.org/lens/search/patent/list", t("patent.open_gp"))

    st.markdown(t("patent.companies_heading"))
    st.caption(t("patent.companies_caption"))
    if not any(firm_counts.values()):
        show_empty(t("patent.empty_counts"))
    else:
        show_plotly(render_company_counts_chart(firm_counts, order=firm_names))

    st.markdown(t("patent.year_heading"))
    st.caption(t("patent.year_caption"))
    if df_trends.empty:
        show_empty(t("patent.empty_trend"))
    else:
        show_plotly(render_patent_trends_chart(df_trends))

    st.markdown(t("patent.topic_mix_heading"))
    st.caption(t("patent.topic_mix_caption"))
    if not any(int(v) > 0 for v in topic_counts.values()):
        show_empty(t("patent.empty_domain"))
    else:
        show_plotly(render_patent_topic_mix_chart(topic_counts, order=list(TECHNOLOGY_DOMAINS)))

    st.markdown(t("patent.radar_heading"))
    st.caption(t("patent.radar_caption"))
    numeric = df_density.drop(columns=["Company"], errors="ignore") if not df_density.empty else None
    if df_density.empty or numeric is None or int(numeric.fillna(0).to_numpy().sum()) == 0:
        show_empty(t("patent.empty_domain"))
    else:
        show_plotly(render_company_patent_domain_chart(df_density))

    st.markdown(t("patent.wordcloud"))
    st.caption(t("patent.wordcloud_caption"))
    kw_dict = PatentService.get_patent_keywords(company_arg, topic)
    wc_fig = render_patent_wordcloud(kw_dict) if kw_dict else None
    if wc_fig is None:
        show_empty(t("patent.empty_wc"))
    else:
        st.pyplot(wc_fig, clear_figure=True)

    st.markdown(t("patent.tree_heading"))
    st.caption(t("patent.tree_caption"))
    df_tree = PatentService.get_sunburst_df(company_arg, topic)
    if df_tree.empty:
        show_empty(t("patent.empty_tree"))
    else:
        show_plotly(render_patent_sunburst(df_tree))

    st.markdown(t("patent.density"))
    st.caption(t("patent.density_caption"))
    if df_density.empty or int(df_density.drop(columns=["Company"], errors="ignore").fillna(0).to_numpy().sum()) == 0:
        show_empty(t("patent.empty_density"))
    else:
        show_plotly(render_patent_density_heatmap(df_density))

    st.markdown(t("patent.map_heading"))
    st.caption(t("patent.map_caption"))
    df_map = PatentService.get_tfidf_map_df(company_arg, topic)
    if df_map.empty:
        show_empty(t("patent.empty_map"))
    else:
        show_plotly(render_patent_tfidf_map(df_map))

    st.markdown(t("patent.list_heading"))
    st.caption(t("patent.list_caption"))
    if not patents:
        show_empty(
            t("patent.empty_topic", topic=topic)
            if topic
            else t("patent.empty_company", company=company if company != "all" else t("patent.all"))
        )
        return
    for pat in patents:
        render_patent_card(pat)
