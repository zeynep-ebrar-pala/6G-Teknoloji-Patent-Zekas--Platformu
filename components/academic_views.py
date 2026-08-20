"""
Modül 3 — Akademik Yayın Analizi.
Türkiye ve Avrupa 6G literatürü: yıl, kurum, ülke, atıf, trend.
Kilitli örnek liste yok. Scholar / WoS sayısı uydurulmaz.
"""

from __future__ import annotations

import streamlit as st

from backend.academic_service import AcademicService
from i18n.core import format_int, get_lang, t
from components.charts import (
    render_academic_bar_chart,
    render_academic_database_chart,
    render_academic_trends_chart,
)

PUB_SECTION_KEYS = ["year", "inst", "country", "cited", "trend", "tt_eu"]


def _fmt(n) -> str:
    return format_int(n) if isinstance(n, int) else "—"


def _cc_name(cc: str) -> str:
    key = f"pub.cc.{cc}"
    label = t(key)
    return cc if label == key else label


def _with_source(paper: dict) -> dict:
    out = dict(paper)
    prefix = str(out.get("prefix") or "")
    if not out.get("source"):
        if prefix.startswith("10.1109"):
            out["source"] = "IEEE Xplore"
        elif prefix.startswith("10.1007"):
            out["source"] = "Springer"
        elif prefix.startswith("10.1016"):
            out["source"] = "Elsevier"
    return out


def render_academic_publication_module():
    from components.topic_panels import render_pub_topic_panel
    from components.tt_europe_views import render_tt_europe_pub_section
    from components.ui_helpers import (
        current_view_mode,
        render_link_row,
        render_module_header,
        render_paper_card,
        render_spec_pub_sources,
        select_section,
        show_empty,
        show_plotly,
    )

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
    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("pub.access_title")}</div>
{t("pub.access_body")}
</div>""",
        unsafe_allow_html=True,
    )
    if current_view_mode() == "expert":
        st.markdown(
            f"""<div class="glass-card">
<div class="teach-label">{t("pub.expert_title")}</div>
{t("pub.expert_body")}
</div>""",
            unsafe_allow_html=True,
        )

    render_spec_pub_sources()
    topic, region = render_pub_topic_panel("pub")
    bundle = AcademicService.get_bundle(region, topic)
    pubs = bundle.get("publishers") or {}

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.metric(t("pub.metric_ieee"), _fmt(pubs.get("ieee")))
    with c2:
        st.metric(t("pub.metric_scholar"), _fmt(pubs.get("scholar")))
    with c3:
        st.metric(t("pub.metric_springer"), _fmt(pubs.get("springer")))
    with c4:
        st.metric(t("pub.metric_elsevier"), _fmt(pubs.get("elsevier")))
    with c5:
        st.metric(t("pub.metric_wos"), _fmt(pubs.get("wos")))
    st.caption(t("pub.source_metric_caption"))
    if current_view_mode() == "expert":
        from backend.publisher_apis import REGISTER

        k1, k2, k3, k4, k5 = st.columns(5)
        with k1:
            st.link_button(t("pub.key_ieee"), REGISTER["ieee"])
        with k2:
            st.link_button(t("pub.key_springer"), REGISTER["springer"])
        with k3:
            st.link_button(t("pub.key_elsevier"), REGISTER["elsevier"])
        with k4:
            st.link_button(t("pub.key_wos"), REGISTER["wos"])
        with k5:
            st.link_button(t("pub.key_scholar"), REGISTER["scholar"])

    wos = bundle.get("chart_source") == "wos"
    tr_n = bundle.get("total_tr")
    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        st.metric(t("pub.metric_tr"), _fmt(tr_n))
    with col_b:
        st.metric(t("pub.metric_wos_core"), _fmt(bundle.get("wos_total")))
    with col_c:
        peak_label = t("pub.metric_peak_year_wos") if wos else t("pub.metric_peak_year")
        years = bundle.get("year_counts") or {}
        if years:
            peak = max(years, key=lambda y: years[y])
            st.metric(peak_label, peak, t("pub.metric_peak_delta", n=_fmt(years[peak])))
        else:
            series = bundle.get("year_series") or {}
            best = None
            for name, yc in series.items():
                if not yc:
                    continue
                y = max(yc, key=lambda k: yc[k])
                cand = (int(yc[y]), str(y), str(name))
                if best is None or cand[0] > best[0]:
                    best = cand
            if best:
                st.metric(
                    peak_label,
                    f"{best[1]} · {best[2]}",
                    t("pub.metric_peak_delta", n=_fmt(best[0])),
                )
            else:
                st.metric(peak_label, "—")
    with col_d:
        countries = bundle.get("countries") or []
        if countries:
            top = countries[0]
            st.metric(
                t("pub.metric_top_cc"),
                _cc_name(top["cc"]),
                t("pub.metric_topic_delta", n=_fmt(top["count"])),
            )
        else:
            st.metric(t("pub.metric_top_cc"), "—")
    if wos and bundle.get("wos_fetched_at"):
        st.caption(t("pub.snapshot", ts=bundle["wos_fetched_at"]))

    from backend.source_links import topic_pub_searches

    render_link_row(
        topic_pub_searches(topic or "6G", region),
        key_suffix=f"pub_src_{region}_{topic or 'all'}",
    )

    _labels = [t(f"pub.section.{k}") for k in PUB_SECTION_KEYS]
    _map = dict(zip(_labels, PUB_SECTION_KEYS))
    section = _map.get(
        select_section(t("pub.view"), _labels, key=f"academic_section_story_{get_lang()}"),
        PUB_SECTION_KEYS[0],
    )

    if section == "tt_eu":
        render_tt_europe_pub_section(topic)
        return

    def _trend_fig():
        df = AcademicService.get_trend_df(region, topic)
        if df is None or df.empty:
            return None
        if wos:
            return render_academic_trends_chart(df, t("pub.chart_trend_wos"))
        rename = {c: _cc_name(c) for c in df.columns if c != "Years"}
        return render_academic_trends_chart(df.rename(columns=rename))

    if section == "year":
        st.markdown(t("pub.year_heading"))
        st.caption(t("pub.year_caption_wos") if wos else t("pub.year_caption"))
        years = bundle.get("year_counts") or {}
        year_title = t("pub.chart_year_wos") if wos else t("pub.chart_year")
        if years:
            show_plotly(
                render_academic_database_chart(years, year_title, t("pub.chart_year_x"))
            )
        else:
            fig = _trend_fig()
            if fig is not None:
                show_plotly(fig)
            else:
                show_empty(t("pub.empty_year"))
        topics = bundle.get("topics") or {}
        if len(topics) > 1:
            show_plotly(
                render_academic_bar_chart(
                    [{"name": k, "count": v} for k, v in topics.items()],
                    t("pub.chart_topic_wos") if wos else t("pub.chart_topic"),
                )
            )

    elif section == "inst":
        st.markdown(t("pub.inst_heading"))
        st.caption(t("pub.inst_caption_wos") if wos else t("pub.inst_caption"))
        inst = bundle.get("institutions") or []
        if inst:
            show_plotly(
                render_academic_bar_chart(
                    inst,
                    t("pub.chart_inst_wos") if wos else t("pub.chart_inst"),
                )
            )
        else:
            show_empty(t("pub.empty_inst_wos") if wos else t("pub.empty_inst"))

    elif section == "country":
        st.markdown(t("pub.cc_heading"))
        st.caption(t("pub.cc_caption_wos") if wos else t("pub.cc_caption"))
        rows = [
            {"name": _cc_name(r["cc"]), "count": r["count"]}
            for r in (bundle.get("countries") or [])
        ]
        if rows:
            show_plotly(
                render_academic_bar_chart(
                    rows,
                    t("pub.chart_cc_wos") if wos else t("pub.chart_cc"),
                )
            )
        else:
            show_empty(t("pub.empty_cc_wos") if wos else t("pub.empty_cc"))

    elif section == "cited":
        st.markdown(t("pub.cited_heading"))
        st.caption(t("pub.cited_caption_wos") if wos else t("pub.cited_caption"))
        papers = bundle.get("cited") or []
        if not papers:
            show_empty(t("pub.empty_cited"))
        else:
            for paper in papers:
                render_paper_card(_with_source(paper))

    else:
        st.markdown(t("pub.trend_heading"))
        st.caption(t("pub.trend_caption_wos") if wos else t("pub.trend_caption"))
        fig = _trend_fig()
        if fig is not None:
            show_plotly(fig)
        else:
            show_empty(t("pub.empty_year"))
        render_link_row(
            topic_pub_searches(topic or "6G", region),
            key_suffix=f"pub_trend_{region}_{topic or 'all'}",
        )
