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
    render_tt_vs_leader_chart,
    render_tt_vs_vendors_chart,
)
from components.ui_helpers import (
    current_view_mode,
    render_paper_card,
    render_patent_card,
    render_source_button,
    show_empty,
    show_plotly,
)
from i18n.core import format_int, get_lang, t


def _explainer(kind: str) -> None:
    expert = current_view_mode() == "expert"
    title_k = "tt_eu.what_title" if kind == "patent" else "tt_eu.what_title_pub"
    body_k = "tt_eu.what_body" if kind == "patent" else "tt_eu.what_body_pub"
    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t(title_k)}</div>
{t(body_k)}
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


def _metrics(kind: str) -> None:
    s = TTEuropeService.summary()
    pos = TTEuropeService.europe_position()
    if kind == "patent":
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric(t("tt_eu.metric_pat"), format_int(s["patent_n"]))
        with c2:
            st.metric(t("tt_eu.metric_ep"), format_int(s["ep_n"]))
        with c3:
            st.metric(t("tt_eu.position_m_pat"), "—" if pos["tr_pat_rank"] is None else format_int(pos["tr_pat_rank"]))
        with c4:
            st.metric(t("tt_eu.metric_named"), format_int(s["wholesale_named_n"]))
        return
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(t("tt_eu.metric_papers"), format_int(s["paper_n"]))
    with c2:
        st.metric(t("tt_eu.position_m_pub"), "—" if pos["tr_pub_rank"] is None else format_int(pos["tr_pub_rank"]))
    with c3:
        st.metric(t("tt_eu.position_m_out"), format_int(pos["pub_outside_tr"]))
    with c4:
        st.metric(t("tt_eu.metric_named"), format_int(s["wholesale_named_n"]))


def _named_country_chips(rows: list, lang: str) -> None:
    st.markdown(t("tt_eu.named_heading"))
    st.caption(t("tt_eu.named_caption"))
    chips = []
    ranked = sorted(rows, key=lambda r: (r.get("name_tr") or r.get("iso3") or ""))
    for row in ranked:
        name = row["name_tr"] if lang == "tr" else row["name_en"]
        layer = t(f"tt_eu.layer.{row['layer']}")
        hex_c = row.get("color") or "#64748B"
        chips.append(
            f'<span style="display:inline-block;margin:0 8px 8px 0;padding:7px 12px;'
            f'border-radius:999px;border:1px solid {hex_c};background:{hex_c}22;'
            f'color:#F8FAFC;font-size:0.82rem;">{name} · {layer}</span>'
        )
    st.markdown(
        f'<div style="margin:4px 0 12px 0;">{"".join(chips)}</div>',
        unsafe_allow_html=True,
    )


def _europe_position_banner(kind: str) -> None:
    lang = get_lang()
    pos = TTEuropeService.europe_position()
    lead_key = "name_tr" if lang == "tr" else "name_en"
    leaders = pos.get("europe_pub_leaders") or []
    lead_txt = "; ".join(
        f"{r[lead_key]} — {r['lead']} ({format_int(r['n'])})"
        for r in leaders[:8]
    ) or "—"
    st.markdown(t("tt_eu.position_heading"))
    if kind == "patent":
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric(
                t("tt_eu.position_m_pat"),
                "—" if pos["tr_pat_rank"] is None else format_int(pos["tr_pat_rank"]),
                help=t("tt_eu.position_m_pat_help", n=format_int(pos["tr_pat_n"])),
            )
        with m2:
            st.metric(t("tt_eu.position_m_ep"), format_int(pos["ep_n"]))
        with m3:
            st.metric(t("tt_eu.position_m_us"), format_int(pos["us_n"]))
        with m4:
            st.metric(t("tt_eu.position_m_pat_out"), format_int(pos["pat_outside_tr"]))
        st.markdown(
            t(
                "tt_eu.position_body_pat",
                pat_n=format_int(pos["tr_pat_n"]),
                pat_rank="—" if pos["tr_pat_rank"] is None else format_int(pos["tr_pat_rank"]),
                ep=format_int(pos["ep_n"]),
                us=format_int(pos["us_n"]),
                pat_out=format_int(pos["pat_outside_tr"]),
            ),
            unsafe_allow_html=True,
        )
        return
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(
            t("tt_eu.position_m_pub"),
            "—" if pos["tr_pub_rank"] is None else format_int(pos["tr_pub_rank"]),
            help=t("tt_eu.position_m_pub_help", n=format_int(pos["tr_pub_n"])),
        )
    with m2:
        st.metric(t("tt_eu.metric_papers"), format_int(pos["tr_pub_n"]))
    with m3:
        st.metric(t("tt_eu.position_m_out"), format_int(pos["pub_outside_tr"]))
    with m4:
        st.metric(t("tt_eu.position_m_ep"), format_int(pos["ep_n"]))
    st.markdown(
        t(
            "tt_eu.position_body_pub",
            pub_n=format_int(pos["tr_pub_n"]),
            pub_rank="—" if pos["tr_pub_rank"] is None else format_int(pos["tr_pub_rank"]),
            pub_out=format_int(pos["pub_outside_tr"]),
            leaders=lead_txt,
        ),
        unsafe_allow_html=True,
    )


def _position_visuals(kind: str, domain: str | None = None) -> None:
    lang = get_lang()
    _europe_position_banner(kind)
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

    if kind == "patent":
        st.markdown(t("tt_eu.vs_heading"))
        st.caption(t("tt_eu.vs_caption"))
        show_plotly(render_tt_vs_vendors_chart(TTEuropeService.vendor_sample_vs_tt(domain)))

    _country_rank(kind)


def _fmt_firm(item: dict | None) -> str:
    if not item:
        return "—"
    if item.get("resolved") is False:
        return f"{item['name']} (—)"
    return f"{item['name']} ({item['n']})"


def _fmt_pat_firm(item: dict | None) -> str:
    if not item:
        return "—"
    n = int(item.get("n") or 0)
    if n <= 0:
        return f"{item['name']} (—)"
    return f"{item['name']} ({n})"


def _country_rank(kind: str) -> None:
    lang = get_lang()
    name_key = "name_tr" if lang == "tr" else "name_en"
    is_pat = kind == "patent"
    st.markdown(t("tt_eu.overview_heading_pat" if is_pat else "tt_eu.overview_heading_pub"))
    st.caption(t("tt_eu.overview_caption_pat" if is_pat else "tt_eu.overview_caption_pub"))
    with st.spinner(t("tt_eu.overview_spin")):
        overview = TTEuropeService.europe_overview()
    if overview:
        if is_pat:
            show_plotly(
                render_tt_vs_leader_chart(
                    overview,
                    name_key,
                    t("tt_eu.overview_vs_title_pat"),
                    t("tt_eu.rank_pat_x"),
                    lead_key="pat_lead_n",
                    tt_key="tt_pat_n",
                    lead_name=t("tt_eu.overview_pat_lead_short"),
                )
            )
            show_plotly(
                render_tt_europe_overview_chart(
                    overview,
                    "pat_lead_n",
                    "tt_pat_rank",
                    name_key,
                    t("tt_eu.overview_pat_title"),
                    t("tt_eu.rank_pat_x"),
                    label_key="pat_lead",
                )
            )
            table = []
            for row in overview:
                pats = row.get("pat_top3") or []
                table.append(
                    {
                        t("tt_eu.named_col_place"): row[name_key],
                        t("tt_eu.overview_pat_1"): _fmt_pat_firm(pats[0] if len(pats) > 0 else None),
                        t("tt_eu.overview_pat_2"): _fmt_pat_firm(pats[1] if len(pats) > 1 else None),
                        t("tt_eu.overview_pat_3"): _fmt_pat_firm(pats[2] if len(pats) > 2 else None),
                        t("tt_eu.overview_tt_pat"): row["tt_pat_n"] if row["tt_pat_n"] else "—",
                        t("tt_eu.rank_col_rank_pat"): row["tt_pat_rank"] if row["tt_pat_rank"] is not None else "—",
                    }
                )
            st.dataframe(table, hide_index=True, width="stretch")
        else:
            show_plotly(
                render_tt_vs_leader_chart(
                    overview,
                    name_key,
                    t("tt_eu.overview_vs_title"),
                    t("tt_eu.rank_pub_x"),
                )
            )
            show_plotly(
                render_tt_europe_overview_chart(
                    overview,
                    "pub_lead_n",
                    "tt_pub_rank",
                    name_key,
                    t("tt_eu.overview_pub_title"),
                    t("tt_eu.rank_pub_x"),
                    label_key="pub_lead",
                )
            )
            table = []
            for row in overview:
                top = row.get("pub_top3") or []
                table.append(
                    {
                        t("tt_eu.named_col_place"): row[name_key],
                        t("tt_eu.overview_pub_1"): _fmt_firm(top[0] if len(top) > 0 else None),
                        t("tt_eu.overview_pub_2"): _fmt_firm(top[1] if len(top) > 1 else None),
                        t("tt_eu.overview_pub_3"): _fmt_firm(top[2] if len(top) > 2 else None),
                        t("tt_eu.overview_tt_pub"): (
                            row["tt_pub_n"] if row.get("tt_pub_resolved") else "—"
                        ),
                        t("tt_eu.rank_col_rank_pub"): row["tt_pub_rank"] if row["tt_pub_rank"] is not None else "—",
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

    st.markdown(t("tt_eu.rank_heading_pat" if is_pat else "tt_eu.rank_heading_pub"))
    st.caption(t("tt_eu.rank_caption_pat" if is_pat else "tt_eu.rank_caption_pub"))
    countries = TTEuropeService.ranked_countries()
    labels = [row["name_tr"] if lang == "tr" else row["name_en"] for row in countries]
    by_label = {labels[i]: countries[i]["cc"] for i in range(len(countries))}
    default_ix = next((i for i, row in enumerate(countries) if row["cc"] == "TR"), 0)
    picked = st.selectbox(
        t("tt_eu.rank_country"),
        labels,
        index=default_ix,
        key=f"tt_eu_rank_cc_{kind}_{lang}",
    )
    cc = by_label.get(picked) or "TR"
    with st.spinner(t("tt_eu.rank_heading").replace("#", "").strip()):
        payload = TTEuropeService.country_rank(cc)
    if not payload.get("ok"):
        return
    rows = payload["rows"]
    tt_row = next((r for r in rows if r.get("is_tt")), {})
    pub_rank = payload.get("tt_pub_rank")
    pat_rank = payload.get("tt_pat_rank")
    if is_pat:
        st.markdown(
            t(
                "tt_eu.rank_tt_pat",
                pat="—" if pat_rank is None else format_int(pat_rank),
                pat_n=format_int(tt_row.get("pat_n") or 0),
                n=format_int(payload.get("field_n") or 0),
            )
        )
        show_plotly(
            render_tt_country_rank_chart(
                rows, "pat_n", t("tt_eu.rank_pat_title"), t("tt_eu.rank_pat_x")
            )
        )
        from backend.source_links import assignee_patent_links

        table = []
        for row in sorted(
            rows,
            key=lambda r: (r["pat_rank"] is None, r["pat_rank"] or 99, r["name"]),
        ):
            pat_links = {item["id"]: item["url"] for item in assignee_patent_links(row["name"])}
            table.append(
                {
                    t("tt_eu.named_col_place"): row["name"],
                    t("tt_eu.rank_col_rank_pat"): row["pat_rank"] if row["pat_rank"] is not None else "—",
                    t("tt_eu.rank_col_pat"): row["pat_n"] if row["pat_n"] else "—",
                    "Google Patents": pat_links.get("google_patents") or row["patents_url"],
                }
            )
        st.dataframe(
            table,
            hide_index=True,
            width="stretch",
            column_config={
                "Google Patents": st.column_config.LinkColumn("Google Patents", display_text="Google"),
            },
        )
        render_source_button(payload["mno_source"], t("tt_eu.rank_open_wiki"))
        return

    st.markdown(
        t(
            "tt_eu.rank_tt_pub",
            pub="—" if pub_rank is None else format_int(pub_rank),
            pub_n=format_int(tt_row.get("pub_n") or 0),
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
    table = []
    for row in sorted(
        rows,
        key=lambda r: (r["pub_rank"] is None, r["pub_rank"] or 99, r["name"]),
    ):
        table.append(
            {
                t("tt_eu.named_col_place"): row["name"],
                t("tt_eu.rank_col_rank_pub"): row["pub_rank"] if row["pub_rank"] is not None else "—",
                t("tt_eu.rank_col_pub"): row["pub_n"] if row.get("pub_resolved") else "—",
                "OpenAlex": row.get("openalex_url") or payload["openalex_url"],
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


def render_tt_europe_patent_section(domain: str | None = None) -> None:
    _explainer("patent")
    _metrics("patent")
    _position_visuals("patent", domain)
    st.markdown(t("tt_eu.office_heading"))
    st.caption(t("tt_eu.office_caption"))
    show_plotly(render_tt_office_chart(TTEuropeService.office_counts()))
    _press_note()
    st.markdown(t("tt_eu.pat_list_heading"))
    st.caption(t("tt_eu.pat_list_caption"))
    pats = TTEuropeService.get_patents()
    if domain:
        pats = [p for p in pats if (p.get("domain") or "") == domain]
    if not pats:
        show_empty(t("patent.empty_topic", topic=domain or "—"))
    else:
        for pat in pats:
            render_patent_card(pat)
    _rd_touchpoints()


def render_tt_europe_pub_section(topic: str | None = None) -> None:
    _explainer("pub")
    _metrics("pub")
    _position_visuals("pub")
    st.markdown(t("tt_eu.oa_heading"))
    st.caption(t("tt_eu.oa_caption"))
    st.markdown(t("tt_eu.papers_heading"))
    st.caption(t("tt_eu.papers_caption"))
    papers = TTEuropeService.get_papers()
    if topic:
        papers = [p for p in papers if (p.get("topic") or "") == topic]
    if not papers:
        show_empty(t("pub.empty_topic", topic=topic or "—"))
    else:
        for paper in papers:
            render_paper_card(paper)
            note = paper.get("note") or ""
            if note:
                st.caption(note)
    _rd_touchpoints()
