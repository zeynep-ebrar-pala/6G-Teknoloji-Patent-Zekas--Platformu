"""
Türk Telekom Görünümü — Ne yapıldı? / Ne yapılacak? sayfa düzeni.
"""

from __future__ import annotations

from html import escape

import streamlit as st

from backend.data_service import DataService
from components.tt_scenarios import render_tt_scenario_calculator
from i18n.core import get_lang, t, t_value


def _beginner_surfaces() -> dict:
    from data.beginner_surfaces import BEGINNER_SURFACES

    return BEGINNER_SURFACES


def render_done_banner() -> None:
    badges = [
        ("#22C55E", t("tt_page.done.badge_announce")),
        ("#3B82F6", t("tt_page.done.badge_patent")),
        ("#A855F7", t("tt_page.done.badge_pub")),
        ("#FFB020", t("tt_page.done.badge_standard")),
        ("#E20074", t("tt_page.done.badge_tti")),
    ]
    badge_html = "".join(
        f'<span class="trl-pill trl-mid" style="margin-right:6px;margin-bottom:4px;border:1px solid {color};">{escape(lab)}</span>'
        for color, lab in badges
    )
    st.markdown(
        f"""<div class="glass-card" style="border-left:5px solid #22C55E;margin-bottom:16px;">
<h2 style="color:#FFFFFF;margin:0 0 8px 0;font-size:1.35rem;">{escape(t("tt_page.done.banner_title"))}</h2>
<p style="color:#CBD5E1;font-size:0.92rem;line-height:1.6;margin:0 0 10px 0;">{escape(t("tt_page.done.banner_body"))}</p>
<p style="color:#94A3B8;font-size:0.82rem;margin:0 0 6px 0;">{escape(t("tt_page.done.badges"))}</p>
<div>{badge_html}</div>
</div>""",
        unsafe_allow_html=True,
    )


def render_tt_tech_summary() -> None:
    st.markdown(t("tt_page.done.tech_heading"))
    st.caption(t("tt_page.done.tech_caption"))
    surfaces = _beginner_surfaces()
    overlay_en: dict = {}
    if get_lang() == "en":
        from data.tech_overlay_en import TECH_OVERLAY_EN

        overlay_en = TECH_OVERLAY_EN
    techs = DataService.get_all_technologies()
    for tech_id, tech in techs.items():
        scenarios = (
            overlay_en.get(tech_id, {}).get("tt_scenarios")
            or surfaces.get(tech_id, {}).get("tt_scenarios")
            or tech.get("tt_scenarios")
            or []
        )
        if not scenarios:
            continue
        title = f"{tech.get('icon', '')} {tech.get('title', tech_id)} (TRL {tech.get('trl', '—')})"
        with st.expander(title, expanded=False):
            for item in scenarios:
                if isinstance(item, dict):
                    head = escape(str(item.get("title") or ""))
                    body = escape(str(item.get("body") or ""))
                    if head:
                        st.markdown(
                            f"<p style='color:#F8FAFC;font-size:0.9rem;margin:0 0 6px 0;'><strong>{head}</strong><br>"
                            f"<span style='color:#C8D1DC;'>{body}</span></p>",
                            unsafe_allow_html=True,
                        )
                    elif body:
                        st.markdown(
                            f"<p style='color:#C8D1DC;font-size:0.9rem;margin:0;'>{body}</p>",
                            unsafe_allow_html=True,
                        )
                elif item:
                    st.markdown(
                        f"<p style='color:#C8D1DC;font-size:0.9rem;margin:0 0 6px 0;'>{item}</p>",
                        unsafe_allow_html=True,
                    )
    try:
        st.page_link("views/tech.py", label=t("tt_page.done.open_tech"), icon="📡")
    except Exception:
        st.caption(t("tt_page.done.open_tech"))


def render_roadmap_banner() -> None:
    st.markdown(
        f"""<div class="glass-card" style="border-left:5px solid #64748B;margin-bottom:16px;">
<h2 style="color:#FFFFFF;margin:0 0 8px 0;font-size:1.35rem;">{escape(t("tt_page.roadmap.banner_title"))}</h2>
<p style="color:#CBD5E1;font-size:0.92rem;line-height:1.6;margin:0;">{escape(t("tt_page.roadmap.banner_body"))}</p>
</div>""",
        unsafe_allow_html=True,
    )


def render_strategy_table() -> None:
    st.markdown(t("tt_page.roadmap.strategy_heading"))
    st.caption(t("tt_page.roadmap.strategy_caption"))
    rows = t_value("tt_page.strategy")
    if not isinstance(rows, list) or not rows:
        return
    table = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        table.append(
            {
                t("tt_page.roadmap.strategy_col_goal"): row.get("goal", ""),
                t("tt_page.roadmap.strategy_col_tech"): row.get("tech", ""),
                t("tt_page.roadmap.strategy_col_trl"): row.get("trl", ""),
                t("tt_page.roadmap.strategy_col_source"): row.get("source", ""),
            }
        )
    if table:
        st.dataframe(table, hide_index=True, width="stretch")


def render_tt_roadmap_section() -> None:
    render_roadmap_banner()
    render_strategy_table()
    st.markdown("---")
    st.markdown(f"### {t('tt_page.roadmap.scenario_sub')}")
    render_tt_scenario_calculator(compact_header=True)


def render_tt_done_section() -> None:
    """Ne yapıldı? — kaynaklı patent, makale, duyuru ve Avrupa izi."""
    from backend.tt_europe_service import TTEuropeService
    from components.charts import render_tt_vs_vendors_chart
    from components.tt_europe_views import (
        _collab_block,
        _country_rank,
        _geo_presence,
        _rd_touchpoints,
        render_patent_card,
        render_paper_card,
        show_empty,
        show_plotly,
    )

    render_done_banner()
    render_tt_tech_summary()

    st.markdown(t("tt_page.done.field_heading"))
    _rd_touchpoints()

    st.markdown(t("tt_page.done.records_heading"))
    st.caption(t("tt_page.done.records_caption"))

    st.markdown(t("tt_eu.pat_list_heading"))
    st.caption(t("tt_eu.pat_list_caption"))
    pats = TTEuropeService.get_patents()
    if not pats:
        show_empty(t("tt_eu.empty_topic", topic="—"))
    else:
        for pat in pats:
            render_patent_card(pat)

    st.markdown(t("tt_eu.papers_heading"))
    st.caption(t("tt_eu.papers_caption"))
    papers = TTEuropeService.get_papers()
    if not papers:
        show_empty(t("pub.empty_topic", topic="—"))
    else:
        for paper in papers:
            render_paper_card(paper)
            note = paper.get("note") or ""
            if note:
                st.caption(note)

    vs = {
        name: n
        for name, n in TTEuropeService.vendor_sample_vs_tt(None).items()
        if int(n or 0) > 0
    }
    if vs:
        st.markdown(t("tt_eu.vs_heading"))
        st.caption(t("tt_eu.vs_caption"))
        show_plotly(render_tt_vs_vendors_chart(vs))

    _country_rank("patent")
    _geo_presence()
    _collab_block(include_touchpoints=False)
    _country_rank("pub")
