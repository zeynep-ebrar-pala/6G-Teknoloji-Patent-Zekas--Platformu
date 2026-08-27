"""
Modül 2 — Patent Zekası ve Rakip Analizi arayüzü.
Grafikler Lens.org toplamı / çekilen kayıttır. Kilitli örnek yok.
"""

from typing import Any, Dict, List

import streamlit as st

from backend.patent_service import PatentService
from i18n.core import format_int, get_lang, t
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


def _chart_payload() -> Dict[str, Any]:
    from backend.config import get_lens_token
    from backend.patent_prefetch import ensure_prefetch, frames_from_snapshot, snapshot

    topic = st.session_state.get("_pat_topic")
    company_arg = st.session_state.get("_pat_company")
    spec = PatentService.get_spec_companies()
    firms = tuple(spec)
    if get_lens_token():
        ensure_prefetch(topic, firms)
    snap = snapshot(topic, firms)
    firm_all, topic_counts, df_density, df_trends, df_tree = frames_from_snapshot(snap, list(spec))
    if company_arg:
        firm_counts = {company_arg: int(firm_all.get(company_arg) or 0)} if company_arg in firm_all else {}
        firm_names = [company_arg]
        if not df_density.empty:
            df_density = df_density[df_density["Company"] == company_arg]
        if not df_trends.empty and company_arg in df_trends.columns:
            df_trends = df_trends[["Years", company_arg]]
        elif not df_trends.empty:
            df_trends = df_trends.iloc[0:0]
        if not df_tree.empty:
            df_tree = df_tree[df_tree["company"] == company_arg]
        patents = [p for p in (snap.get("rows") or []) if p.get("assignee") == company_arg]
    else:
        firm_counts = firm_all
        firm_names = list(spec)
        patents = list(snap.get("rows") or [])
    return {
        "snap": snap,
        "topic": topic,
        "company_arg": company_arg,
        "firm_counts": firm_counts,
        "firm_names": firm_names,
        "topic_counts": topic_counts,
        "df_density": df_density,
        "df_trends": df_trends,
        "df_tree": df_tree,
        "patents": patents,
    }


def _draw_count_charts(payload: Dict[str, Any], *, heavy: bool) -> None:
    from backend.patent_apis import lens_last_error
    from backend.source_links import assignee_patent_links
    from data.patents import TECHNOLOGY_DOMAINS

    snap = payload["snap"]
    topic = payload["topic"]
    company_arg = payload["company_arg"]
    firm_counts: Dict[str, int] = payload["firm_counts"]
    firm_names: List[str] = payload["firm_names"]
    topic_counts: Dict[str, int] = payload["topic_counts"]
    df_density = payload["df_density"]
    df_trends = payload["df_trends"]
    df_tree = payload["df_tree"]
    patents: List[Dict[str, Any]] = payload["patents"]

    if snap.get("running") or not snap.get("complete"):
        st.caption(t("patent.bg_partial"))
    api_err = (snap.get("error") or "") or lens_last_error()
    if api_err:
        st.warning(t("patent.api_error", detail=str(api_err).replace("{", "(").replace("}", ")")))

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

    st.markdown(t("patent.list_heading"))
    st.caption(t("patent.list_caption"))
    if not patents:
        show_empty(
            t("patent.empty_topic", topic=topic)
            if topic
            else t("patent.empty_company", company=company_arg or t("patent.all"))
        )
    else:
        cap = 12
        for pat in patents[:cap]:
            render_patent_card(pat)
        extra = len(patents) - cap
        if extra > 0:
            st.caption(t("patent.cards_more", n=format_int(cap), rest=format_int(extra)))

    if not heavy:
        return

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


def render_patent_intelligence_module():
    render_module_header(
        t("patent.title"),
        t("patent.subtitle", source=PatentService.get_data_source()),
    )

    def _card(html: str) -> None:
        if hasattr(st, "html"):
            st.html(html)
        else:
            st.markdown(html, unsafe_allow_html=True)

    _card(
        f"""<div class="glass-card">
<div class="teach-label">{t("patent.what_title")}</div>
{t("patent.what_body")}
</div>"""
    )
    _card(
        f"""<div class="glass-card">
<div class="teach-label">{t("patent.access_title")}</div>
{t("patent.access_body")}
</div>"""
    )
    if current_view_mode() == "expert":
        _card(
            f"""<div class="glass-card">
<div class="teach-label">{t("patent.expert_title")}</div>
{t("patent.expert_body")}
</div>"""
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

    spec = PatentService.get_spec_companies()
    filter_options = ["all"] + spec
    company = st.selectbox(
        t("patent.filter"),
        options=filter_options,
        format_func=lambda x: t("patent.all") if x == "all" else x,
        key="patent_company_filter",
    )
    company_arg = None if company == "all" else company
    st.session_state["_pat_topic"] = topic
    st.session_state["_pat_company"] = company_arg
    from backend.config import get_lens_token
    from backend.live_refresh import render_watch
    from backend.patent_prefetch import ensure_prefetch

    if get_lens_token():
        ensure_prefetch(topic, tuple(spec), force=False)
    render_watch("lens", "patent")
    payload = _chart_payload()
    complete = bool(payload["snap"].get("complete"))
    if not complete:
        st.caption(t("patent.bg_partial"))
        if st.button(t("patent.bg_refresh"), key="pat_bg_refresh"):
            st.rerun()
    heavy = complete and st.checkbox(
        t("patent.heavy_toggle"),
        value=False,
        key="pat_heavy_charts",
    )
    _draw_count_charts(payload, heavy=heavy)
