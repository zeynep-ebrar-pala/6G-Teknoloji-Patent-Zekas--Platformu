"""
Patent Zekası ve Yayın Trendleri — Türk Telekom Avrupa izi bölümü.
"""

from __future__ import annotations

import streamlit as st

from backend.tt_europe_service import TTEuropeService
from components.charts import (
    render_tt_country_rank_chart,
    render_tt_europe_choropleth,
    render_tt_europe_overview_chart,
    render_tt_office_chart,
    render_tt_role_kind_chart,
    render_tt_vs_vendors_chart,
)
from components.ui_helpers import (
    current_view_mode,
    render_paper_card,
    render_patent_card,
    render_source_button,
    show_plotly,
)
from i18n.core import format_int, get_lang, t


def _explainer() -> None:
    expert = current_view_mode() == "expert"
    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("tt_eu.what_title")}</div>
{t("tt_eu.what_body")}
</div>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""<div class="glass-card" style="border-left: 5px solid #E20074;">
<div class="teach-label">{t("tt_eu.role_title")}</div>
{t("tt_eu.role_body")}
</div>""",
        unsafe_allow_html=True,
    )
    if expert:
        st.markdown(
            f"""<div class="glass-card">
<div class="teach-label">{t("tt_eu.expert_title")}</div>
{t("tt_eu.expert_body")}
</div>""",
            unsafe_allow_html=True,
        )


def _metrics() -> None:
    s = TTEuropeService.summary()
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(t("tt_eu.metric_pat"), format_int(s["patent_n"]))
    with c2:
        st.metric(t("tt_eu.metric_ep"), format_int(s["ep_n"]))
    with c3:
        st.metric(t("tt_eu.metric_papers"), format_int(s["paper_n"]))
    with c4:
        st.metric(t("tt_eu.metric_named"), format_int(s["wholesale_named_n"]))


def _named_country_chips(rows: list, lang: str) -> None:
    st.markdown(t("tt_eu.named_heading"))
    st.caption(t("tt_eu.named_caption"))
    order = ("hq", "wholesale", "rd_collab", "standards", "mou_venue")
    ranked = sorted(rows, key=lambda r: (order.index(r["layer"]) if r["layer"] in order else 99, r["iso3"]))
    table = []
    for row in ranked:
        table.append(
            {
                t("tt_eu.named_col_place"): row["name_tr"] if lang == "tr" else row["name_en"],
                "ISO": row["iso3"],
                t("tt_eu.named_col_layer"): t(f"tt_eu.layer.{row['layer']}"),
            }
        )
    st.dataframe(table, hide_index=True, width="stretch")


def _position_visuals(*, show_vendor_compare: bool) -> None:
    lang = get_lang()
    st.markdown(t("tt_eu.map_heading"))
    st.caption(t("tt_eu.map_caption"))
    rows = TTEuropeService.map_rows()
    try:
        show_plotly(render_tt_europe_choropleth(rows, lang=lang))
    except Exception:
        st.info(t("tt_eu.map_fail"))
    _named_country_chips(rows, lang)
    ir = TTEuropeService.get_ir_wholesale()
    st.caption(ir["attribution_tr"] if lang == "tr" else ir["attribution_en"])
    c_ir, c_tti = st.columns(2)
    with c_ir:
        render_source_button(ir["url"], t("tt_eu.open_ir"))
    with c_tti:
        render_source_button(ir["tti_url"], t("tt_eu.open_tti"))

    st.markdown(t("tt_eu.role_heading"))
    st.caption(t("tt_eu.role_caption"))
    show_plotly(render_tt_role_kind_chart(TTEuropeService.role_kind_counts()))

    if show_vendor_compare:
        st.markdown(t("tt_eu.vs_heading"))
        st.caption(t("tt_eu.vs_caption"))
        show_plotly(render_tt_vs_vendors_chart(TTEuropeService.vendor_sample_vs_tt()))

    _country_rank()


def _country_rank() -> None:
    lang = get_lang()
    name_key = "name_tr" if lang == "tr" else "name_en"
    st.markdown(t("tt_eu.overview_heading"))
    st.caption(t("tt_eu.overview_caption"))
    with st.spinner(t("tt_eu.overview_spin")):
        overview = TTEuropeService.europe_overview()
    if overview:
        col_p, col_a = st.columns(2)
        with col_p:
            show_plotly(
                render_tt_europe_overview_chart(
                    overview,
                    "tt_pub_n",
                    "tt_pub_rank",
                    name_key,
                    t("tt_eu.overview_pub_title"),
                    t("tt_eu.rank_pub_x"),
                )
            )
        with col_a:
            show_plotly(
                render_tt_europe_overview_chart(
                    overview,
                    "tt_pat_n",
                    "tt_pat_rank",
                    name_key,
                    t("tt_eu.overview_pat_title"),
                    t("tt_eu.rank_pat_x"),
                )
            )
        table = []
        for row in overview:
            table.append(
                {
                    t("tt_eu.named_col_place"): row[name_key],
                    t("tt_eu.rank_col_rank_pub"): row["tt_pub_rank"],
                    t("tt_eu.overview_tt_pub"): row["tt_pub_n"],
                    t("tt_eu.overview_pub_lead"): f"{row['pub_lead']} ({row['pub_lead_n']})",
                    t("tt_eu.rank_col_rank_pat"): row["tt_pat_rank"],
                    t("tt_eu.overview_tt_pat"): row["tt_pat_n"],
                    t("tt_eu.overview_pat_lead"): f"{row['pat_lead']} ({row['pat_lead_n']})",
                    "OpenAlex": row.get("openalex_url") or "",
                }
            )
        st.dataframe(
            table,
            hide_index=True,
            width="stretch",
            column_config={
                "OpenAlex": st.column_config.LinkColumn("OpenAlex", display_text="OpenAlex"),
            },
        )

    st.markdown(t("tt_eu.rank_heading"))
    st.caption(t("tt_eu.rank_caption"))
    countries = TTEuropeService.ranked_countries()
    lang = get_lang()
    labels = [row["name_tr"] if lang == "tr" else row["name_en"] for row in countries]
    by_label = {labels[i]: countries[i]["cc"] for i in range(len(countries))}
    default_ix = next((i for i, row in enumerate(countries) if row["cc"] == "TR"), 0)
    picked = st.selectbox(t("tt_eu.rank_country"), labels, index=default_ix, key=f"tt_eu_rank_cc_{lang}")
    cc = by_label.get(picked) or "TR"
    with st.spinner(t("tt_eu.rank_heading").replace("#", "").strip()):
        payload = TTEuropeService.country_rank(cc)
    if not payload.get("ok"):
        return
    rows = payload["rows"]
    tt_row = next((r for r in rows if r.get("is_tt")), {})
    st.markdown(
        t(
            "tt_eu.rank_tt",
            pub=format_int(payload.get("tt_pub_rank") or 0),
            pat=format_int(payload.get("tt_pat_rank") or 0),
            pub_n=format_int(tt_row.get("pub_n") or 0),
            pat_n=format_int(tt_row.get("pat_n") or 0),
            n=format_int(payload.get("field_n") or 0),
        )
    )
    if payload.get("oa_ok"):
        show_plotly(
            render_tt_country_rank_chart(
                rows, "pub_n", t("tt_eu.rank_pub_title"), t("tt_eu.rank_pub_x")
            )
        )
    else:
        st.info(t("tt_eu.rank_oa_fail"))
    show_plotly(
        render_tt_country_rank_chart(
            rows, "pat_n", t("tt_eu.rank_pat_title"), t("tt_eu.rank_pat_x")
        )
    )
    table = []
    for row in sorted(rows, key=lambda r: (r["pub_rank"], r["name"])):
        table.append(
            {
                t("tt_eu.named_col_place"): row["name"],
                t("tt_eu.rank_col_rank_pub"): row["pub_rank"],
                t("tt_eu.rank_col_pub"): row["pub_n"],
                t("tt_eu.rank_col_rank_pat"): row["pat_rank"],
                t("tt_eu.rank_col_pat"): row["pat_n"],
                "OpenAlex": payload["openalex_url"],
                "Google Patents": row["patents_url"],
            }
        )
    st.dataframe(
        table,
        hide_index=True,
        width="stretch",
        column_config={
            "OpenAlex": st.column_config.LinkColumn("OpenAlex", display_text="OpenAlex"),
            "Google Patents": st.column_config.LinkColumn("Google Patents", display_text="Patents"),
        },
    )
    c_oa, c_wiki = st.columns(2)
    with c_oa:
        render_source_button(payload["openalex_url"], t("tt_eu.rank_open_oa"))
    with c_wiki:
        render_source_button(payload["mno_source"], t("tt_eu.rank_open_wiki"))


def _rd_touchpoints() -> None:
    st.markdown(t("tt_eu.presence_heading"))
    st.caption(t("tt_eu.presence_caption"))
    lang = get_lang()
    for row in TTEuropeService.get_touchpoints():
        title = row["title_tr"] if lang == "tr" else row["title_en"]
        detail = row["detail_tr"] if lang == "tr" else row["detail_en"]
        place = row["country_name_tr"] if lang == "tr" else row["country_name_en"]
        st.markdown(
            f"""<div class="glass-card" style="margin-bottom:8px;padding:16px;">
<span class="trl-pill trl-mid">{place}</span>
<h4 style="color:#FFFFFF;margin:8px 0 6px 0;">{title}</h4>
<p style="color:#C8D1DC;font-size:0.88rem;margin:0;">{detail}</p>
</div>""",
            unsafe_allow_html=True,
        )
        render_source_button(row["url"], t("tt_eu.open_touch"))


def _press_note() -> None:
    claim = TTEuropeService.get_press_claims()
    text = claim["attribution_tr"] if get_lang() == "tr" else claim["attribution_en"]
    st.caption(text)
    render_source_button(claim["url"], t("tt_eu.open_press"))


def render_tt_europe_patent_section() -> None:
    _explainer()
    _metrics()
    _position_visuals(show_vendor_compare=True)
    st.markdown(t("tt_eu.office_heading"))
    st.caption(t("tt_eu.office_caption"))
    show_plotly(render_tt_office_chart(TTEuropeService.office_counts()))
    _press_note()
    st.markdown(t("tt_eu.pat_list_heading"))
    st.caption(t("tt_eu.pat_list_caption"))
    for pat in TTEuropeService.get_patents():
        render_patent_card(pat)
    _rd_touchpoints()


def render_tt_europe_pub_section() -> None:
    _explainer()
    _metrics()
    _position_visuals(show_vendor_compare=False)
    st.markdown(t("tt_eu.oa_heading"))
    st.caption(t("tt_eu.oa_caption"))
    st.markdown(t("tt_eu.papers_heading"))
    st.caption(t("tt_eu.papers_caption"))
    for paper in TTEuropeService.get_papers():
        render_paper_card(paper)
        note = paper.get("note") or ""
        if note:
            st.caption(note)
    _rd_touchpoints()
