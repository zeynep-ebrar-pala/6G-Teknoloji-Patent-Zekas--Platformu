"""
Patent Zekası ve Yayın Trendleri — Türk Telekom Avrupa izi bölümü.
"""

from __future__ import annotations

import streamlit as st

from backend.tt_europe_service import TTEuropeService
from components.charts import (
    render_tt_country_rank_chart,
    render_tt_europe_choropleth,
    render_tt_office_chart,
    render_tt_role_kind_chart,
    render_tt_vs_leader_chart,
    render_tt_vs_vendors_chart,
    tt_vs_comparable_rows,
)
from components import ui_helpers as _uh
from data.tt_europe import place_sort_key
from i18n.core import format_int, get_lang, t


def current_view_mode():
    return _uh.current_view_mode()


def render_paper_card(paper):
    return _uh.render_paper_card(paper)


def render_patent_card(patent):
    return _uh.render_patent_card(patent)


def render_source_button(url, label=None):
    return _uh.render_source_button(url, label)


def show_empty(message):
    return _uh.show_empty(message)


def show_plotly(fig):
    return _uh.show_plotly(fig)


def _positive_rows(rows: list, key: str) -> list:
    return [r for r in rows if int(r.get(key) or 0) > 0]


def _metric_row(items: list[tuple[str, int]]) -> None:
    shown = [(lab, n) for lab, n in items if int(n or 0) > 0]
    if not shown:
        return
    cols = st.columns(len(shown))
    for col, (lab, n) in zip(cols, shown):
        with col:
            st.metric(lab, format_int(n))


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


def _metrics(kind: str, domain: str | None = None) -> None:
    s = TTEuropeService.summary(domain)
    if kind == "patent":
        _metric_row(
            [
                (t("tt_eu.metric_us"), s["us_n"]),
                (t("tt_eu.metric_ep"), s["ep_n"]),
                (t("tt_eu.metric_tr"), s.get("tr_n") or 0),
            ]
        )
        return
    pos = TTEuropeService.europe_position(include_pubs=True)
    _metric_row(
        [
            (t("tt_eu.metric_papers"), s["paper_n"]),
            (t("tt_eu.position_m_out"), pos["pub_outside_tr"]),
            (t("tt_eu.metric_named"), s["wholesale_named_n"]),
        ]
    )


def _named_country_cards(rows: list, lang: str) -> None:
    st.markdown(t("tt_eu.named_heading"))
    st.caption(t("tt_eu.named_caption"))
    ranked = sorted(
        rows,
        key=lambda r: place_sort_key(
            str((r.get("name_tr") if lang == "tr" else r.get("name_en")) or ""),
            lang,
        ),
    )
    for row in ranked:
        name = row["name_tr"] if lang == "tr" else row["name_en"]
        body = row["label_tr"] if lang == "tr" else row["label_en"]
        layer = t(f"tt_eu.layer.{row['layer']}")
        hex_c = row.get("color") or "#64748B"
        st.markdown(
            f"""<div class="glass-card" style="margin-bottom:10px;padding:16px 18px;border-left:5px solid {hex_c};">
<span class="trl-pill trl-mid">{layer}</span>
<h4 style="color:#FFFFFF;margin:8px 0 6px 0;">{name}</h4>
<p style="color:#C8D1DC;font-size:0.9rem;line-height:1.55;margin:0;">{body}</p>
</div>""",
            unsafe_allow_html=True,
        )
        url = row.get("source_url") or ""
        if url:
            render_source_button(url, t("tt_eu.open_place"))


def _europe_position_banner(kind: str, domain: str | None = None) -> None:
    lang = get_lang()
    pos = TTEuropeService.europe_position(include_pubs=(kind != "patent"))
    if kind == "patent" and domain:
        offices = TTEuropeService.office_counts(domain)
        pos = {
            **pos,
            "ep_n": int(offices.get("EP") or 0),
            "us_n": int(offices.get("US") or 0),
            "tr_n": int(offices.get("TR") or 0),
        }
    lead_key = "name_tr" if lang == "tr" else "name_en"
    leaders = pos.get("europe_pub_leaders") or []
    lead_txt = "; ".join(
        f"{r[lead_key]} — {r['lead']} ({format_int(r['n'])})"
        for r in leaders[:8]
    ) or "—"
    st.markdown(t("tt_eu.position_heading"))
    if kind == "patent":
        _metric_row(
            [
                (t("tt_eu.position_m_us"), pos["us_n"]),
                (t("tt_eu.position_m_ep"), pos["ep_n"]),
                (t("tt_eu.metric_tr"), pos.get("tr_n") or 0),
            ]
        )
        st.markdown(
            t(
                "tt_eu.position_body_pat",
                us=format_int(pos["us_n"]),
            ),
            unsafe_allow_html=True,
        )
        return
    pub_items = [(t("tt_eu.metric_papers"), pos["tr_pub_n"])]
    if pos["tr_pub_rank"] is not None:
        pub_items.insert(0, (t("tt_eu.position_m_pub"), pos["tr_pub_rank"]))
    if int(pos["pub_outside_tr"] or 0) > 0:
        pub_items.append((t("tt_eu.position_m_out"), pos["pub_outside_tr"]))
    _metric_row(pub_items)
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


def _geo_presence() -> None:
    """İsimli ülkeler + TTI toptan — patent sayısı değildir."""
    lang = get_lang()
    st.markdown(t("tt_eu.map_heading"))
    st.caption(t("tt_eu.map_caption"))
    rows = TTEuropeService.map_rows()
    try:
        show_plotly(render_tt_europe_choropleth(rows, lang=lang))
    except Exception:
        st.info(t("tt_eu.map_fail"))
    _named_country_cards(rows, lang)
    ir = TTEuropeService.get_ir_wholesale()
    st.caption(ir["attribution_tr"] if lang == "tr" else ir["attribution_en"])
    c_ir, c_tti = st.columns(2)
    with c_ir:
        render_source_button(ir["url"], t("tt_eu.open_ir"))
    with c_tti:
        render_source_button(ir["tti_url"], t("tt_eu.open_tti"))


def _collab_block(*, draw_chart: bool = True) -> None:
    """İşbirliği / standart / basın — tescil değildir."""
    st.markdown(t("tt_eu.role_heading"))
    st.caption(t("tt_eu.role_caption"))
    if draw_chart:
        show_plotly(render_tt_role_kind_chart(TTEuropeService.role_kind_counts()))
    _rd_touchpoints()


def _fmt_firm(item: dict | None) -> str:
    if not item:
        return "—"
    if item.get("resolved") is False:
        return f"{item['name']} (—)"
    return f"{item['name']} ({item['n']})"


def _fmt_pat_hits(items: list | None) -> str:
    """Yalnızca örnek kümede kaydı olan firmalar; 0’lık 2./3. sütun yok."""
    hits = [it for it in (items or []) if int(it.get("n") or 0) > 0]
    if not hits:
        return "—"
    return " · ".join(f"{it['name']} ({it['n']})" for it in hits)


def _country_rank(kind: str) -> None:
    lang = get_lang()
    name_key = "name_tr" if lang == "tr" else "name_en"
    is_pat = kind == "patent"
    st.markdown(t("tt_eu.overview_heading_pat" if is_pat else "tt_eu.overview_heading_pub"))
    st.caption(t("tt_eu.overview_caption_pat" if is_pat else "tt_eu.overview_caption_pub"))
    spin = t("tt_eu.overview_spin_pat" if is_pat else "tt_eu.overview_spin")
    with st.spinner(spin):
        overview = TTEuropeService.europe_overview(include_pubs=not is_pat)
    if overview:
        if is_pat:
            pat_rows = [
                row
                for row in overview
                if int(row.get("tt_pat_n") or 0) > 0 or int(row.get("pat_lead_n") or 0) > 0
            ]
            pat_rows.sort(
                key=lambda r: (int(r.get("tt_pat_n") or 0), int(r.get("pat_lead_n") or 0)),
                reverse=True,
            )
            if pat_rows:
                vs_rows = tt_vs_comparable_rows(
                    pat_rows, lead_key="pat_lead_n", tt_key="tt_pat_n", lead_name_key="pat_lead"
                )
                if vs_rows:
                    show_plotly(
                        render_tt_vs_leader_chart(
                            vs_rows,
                            name_key,
                            t("tt_eu.overview_vs_title_pat"),
                            t("tt_eu.rank_pat_x"),
                            lead_key="pat_lead_n",
                            tt_key="tt_pat_n",
                            lead_name=t("tt_eu.overview_pat_lead_short"),
                        )
                    )
                else:
                    st.info(t("tt_eu.overview_vs_empty_pat"))
                table = []
                for row in pat_rows:
                    table.append(
                        {
                            t("tt_eu.named_col_place"): row[name_key],
                            t("tt_eu.overview_hits_pat"): _fmt_pat_hits(row.get("pat_top3")),
                            t("tt_eu.overview_tt_pat"): row["tt_pat_n"],
                        }
                    )
                if table:
                    st.dataframe(table, hide_index=True, width="stretch")
            else:
                show_empty(t("tt_eu.overview_empty_pat"))
        else:
            tt_only = [r for r in overview if int(r.get("tt_pub_n") or 0) > 0]
            if not tt_only:
                show_empty(t("tt_eu.overview_empty_pub"))
            table = []
            for row in overview:
                if int(row.get("tt_pub_n") or 0) <= 0:
                    continue
                top = row.get("pub_top3") or []
                table.append(
                    {
                        t("tt_eu.named_col_place"): row[name_key],
                        t("tt_eu.overview_pub_1"): _fmt_firm(top[0] if len(top) > 0 else None),
                        t("tt_eu.overview_pub_2"): _fmt_firm(top[1] if len(top) > 1 else None),
                        t("tt_eu.overview_pub_3"): _fmt_firm(top[2] if len(top) > 2 else None),
                        t("tt_eu.overview_tt_pub"): row["tt_pub_n"],
                        t("ui.source").replace(" ↗", ""): row.get("pub_search_url") or "",
                    }
                )
            src_col = t("ui.source").replace(" ↗", "")
            st.dataframe(
                table,
                hide_index=True,
                width="stretch",
                column_config={
                    src_col: st.column_config.LinkColumn(src_col, display_text="IEEE"),
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
    with st.spinner(t("tt_eu.rank_spin")):
        payload = TTEuropeService.country_rank(cc, include_pubs=not is_pat)
    if not payload.get("ok"):
        return
    rows = payload["rows"]
    tt_row = next((r for r in rows if r.get("is_tt")), {})
    if is_pat:
        drawn = _positive_rows(rows, "pat_n")
        pat_n = int(tt_row.get("pat_n") or 0)
        if not drawn:
            st.info(t("tt_eu.rank_empty_pat"))
            render_source_button(payload["mno_source"], t("tt_eu.rank_open_wiki"))
            return
        st.markdown(
            t(
                "tt_eu.rank_tt_pat",
                pat_n=format_int(pat_n),
            )
        )
        show_plotly(
            render_tt_country_rank_chart(
                drawn, "pat_n", t("tt_eu.rank_pat_title"), t("tt_eu.rank_pat_x")
            )
        )
        from backend.source_links import assignee_patent_links

        table = []
        for row in sorted(drawn, key=lambda r: (-int(r.get("pat_n") or 0), r["name"])):
            pat_links = {item["id"]: item["url"] for item in assignee_patent_links(row["name"])}
            table.append(
                {
                    t("tt_eu.rank_col_firm"): row["name"],
                    t("tt_eu.rank_col_pat"): row["pat_n"],
                    t("sources.open_google_patents").replace(" ↗", ""): pat_links.get("google_patents")
                    or row.get("patents_url")
                    or "",
                }
            )
        gp_col = t("sources.open_google_patents").replace(" ↗", "")
        st.dataframe(
            table,
            hide_index=True,
            width="stretch",
            column_config={
                gp_col: st.column_config.LinkColumn(gp_col, display_text="Google"),
            },
        )
        render_source_button(payload["mno_source"], t("tt_eu.rank_open_wiki"))
        return

    pub_drawn = _positive_rows(rows, "pub_n") if payload.get("pub_ok") else []
    st.markdown(
        t(
            "tt_eu.rank_tt_pub",
            pub_n=format_int(tt_row.get("pub_n") or 0),
        )
    )
    if not pub_drawn:
        st.info(t("tt_eu.rank_oa_fail"))
        render_source_button(payload.get("pub_search_url") or "", t("tt_eu.rank_open_oa"))
        render_source_button(payload["mno_source"], t("tt_eu.rank_open_wiki"))
        return
    src_col = t("ui.source").replace(" ↗", "")
    table = []
    for row in sorted(pub_drawn, key=lambda r: (-int(r.get("pub_n") or 0), r["name"])):
        table.append(
            {
                t("tt_eu.rank_col_firm"): row["name"],
                t("tt_eu.rank_col_pub"): row["pub_n"],
                src_col: row.get("pub_search_url") or payload.get("pub_search_url") or "",
            }
        )
    st.dataframe(
        table,
        hide_index=True,
        width="stretch",
        column_config={
            src_col: st.column_config.LinkColumn(src_col, display_text="IEEE"),
        },
    )
    c_ieee, c_wiki = st.columns(2)
    with c_ieee:
        render_source_button(payload.get("pub_search_url") or "", t("tt_eu.rank_open_oa"))
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


def render_tt_europe_patent_section(domain: str | None = None) -> None:
    _explainer("patent")
    _metrics("patent", domain)
    offices = TTEuropeService.office_counts(domain)
    positive_offices = {k: n for k, n in offices.items() if int(n or 0) > 0}
    st.markdown(t("tt_eu.office_heading"))
    st.caption(t("tt_eu.office_caption"))
    if positive_offices:
        if domain:
            st.info(t("tt_eu.office_lock_one", topic=domain, us=format_int(offices.get("US") or 0)))
        else:
            st.info(t("tt_eu.office_lock_all", us=format_int(offices.get("US") or 0)))
        show_plotly(render_tt_office_chart(positive_offices))
    else:
        show_empty(t("tt_eu.empty_topic", topic=domain or "—"))
    st.markdown(t("tt_eu.pat_list_heading"))
    st.caption(t("tt_eu.pat_list_caption"))
    pats = TTEuropeService.get_patents()
    if domain:
        pats = [p for p in pats if (p.get("domain") or "") == domain]
    if not pats:
        show_empty(t("tt_eu.empty_topic", topic=domain or "—"))
    else:
        for pat in pats:
            render_patent_card(pat)
    _europe_position_banner("patent", domain)
    vs = {
        name: n
        for name, n in TTEuropeService.vendor_sample_vs_tt(domain).items()
        if int(n or 0) > 0
    }
    if vs:
        st.markdown(t("tt_eu.vs_heading"))
        st.caption(t("tt_eu.vs_caption"))
        show_plotly(render_tt_vs_vendors_chart(vs))
    _country_rank("patent")
    _geo_presence()
    _collab_block()


def render_tt_europe_pub_section(topic: str | None = None) -> None:
    _explainer("pub")
    _metrics("pub", topic)
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
    _europe_position_banner("pub")
    _country_rank("pub")
    _collab_block(draw_chart=False)
