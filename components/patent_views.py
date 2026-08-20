"""
Modül 2 — Patent Zekası ve Rakip Analizi arayüzü.
Grafikler Lens.org toplamı / çekilen kayıttır. Kilitli örnek yok.
"""

import streamlit as st

from backend.patent_service import PatentService
from i18n.core import format_int, get_lang, t
from components.charts import (
    render_company_counts_chart,
    render_company_patent_domain_chart,
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
    select_section,
    show_empty,
    show_plotly,
)
from components.topic_panels import render_patent_topic_panel
from components.tt_europe_views import render_tt_europe_patent_section

PATENT_SECTION_KEYS = ["charts", "tt_eu"]


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

    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("patent.what_title")}</div>
{t("patent.what_body")}
</div>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("patent.access_title")}</div>
{t("patent.access_body")}
</div>""",
        unsafe_allow_html=True,
    )
    if current_view_mode() == "expert":
        st.markdown(
            f"""<div class="glass-card">
<div class="teach-label">{t("patent.expert_title")}</div>
{t("patent.expert_body")}
</div>""",
            unsafe_allow_html=True,
        )
        st.link_button(t("patent.key_lens"), "https://www.lens.org/lens/user/subscriptions")

    _lens_token_box()
    render_spec_patent_sources()
    topic = render_patent_topic_panel("patent")

    _labels = [t(f"patent.section.{k}") for k in PATENT_SECTION_KEYS]
    _map = dict(zip(_labels, PATENT_SECTION_KEYS))
    section = _map.get(
        select_section(t("patent.view"), _labels, key=f"patent_section_story_{get_lang()}"),
        PATENT_SECTION_KEYS[0],
    )

    if section == "tt_eu":
        render_tt_europe_patent_section(domain=topic)
        return

    from backend.patent_apis import key_fingerprint, live_assignee_counts
    from backend.source_links import assignee_patent_links, topic_query

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
    query = topic_query(topic or "6G")
    keys = key_fingerprint()

    with st.spinner(t("patent.live_gp_spin")):
        xhr_totals = live_assignee_counts(query, tuple(spec) if not company_arg else (company_arg,), keys)
        summary = PatentService.get_summary(company_arg, topic)
        patents = PatentService.get_top_patents(company_arg, topic)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(t("patent.metric_pulled"), format_int(summary["total"]))
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
    st.caption(t("patent.pulled_caption"))
    if company_arg:
        st.caption(t("sources.assignee_caption", company=company_arg))
        render_link_row(assignee_patent_links(company_arg), key_suffix=f"asg_{company_arg}")
    else:
        render_source_button("https://www.lens.org/lens/search/patent/list", t("patent.open_gp"))

    st.markdown(t("patent.companies_heading"))
    st.caption(t("patent.companies_caption"))
    firm_counts = {
        name: n
        for name, n in xhr_totals.items()
        if isinstance(n, int) and n > 0
    }
    if not firm_counts:
        show_empty(t("patent.empty_counts"))
    else:
        show_plotly(render_company_counts_chart(firm_counts))

    st.markdown(t("patent.year_heading"))
    st.caption(t("patent.year_caption"))
    df_trends = PatentService.get_patent_trends_df(company_arg, topic)
    if df_trends.empty:
        show_empty(t("patent.empty_trend"))
    else:
        show_plotly(render_patent_trends_chart(df_trends))

    st.markdown(t("patent.topic_mix_heading"))
    st.caption(t("patent.topic_mix_caption"))
    topic_counts = PatentService.get_topic_counts(company_arg, topic)
    if not topic_counts:
        show_empty(t("patent.empty_domain"))
    else:
        show_plotly(render_patent_topic_mix_chart(topic_counts))

    st.markdown(t("patent.radar_heading"))
    st.caption(t("patent.radar_caption"))
    df_domains = PatentService.get_all_companies_domain_df(company_arg, topic)
    numeric = df_domains.drop(columns=["Company"], errors="ignore") if not df_domains.empty else None
    if df_domains.empty or numeric is None or int(numeric.fillna(0).to_numpy().sum()) == 0:
        show_empty(t("patent.empty_domain"))
    else:
        show_plotly(render_company_patent_domain_chart(df_domains))

    st.markdown(t("patent.wordcloud"))
    st.caption(t("patent.wordcloud_caption"))
    kw_dict = PatentService.get_patent_keywords(company_arg, topic)
    wc_fig = render_patent_wordcloud(kw_dict) if kw_dict else None
    if wc_fig is None:
        show_empty(t("patent.empty_wc"))
    else:
        st.pyplot(wc_fig, clear_figure=True)

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
