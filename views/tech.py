"""6G Teknolojileri — yalnızca seçilen bölüm yüklenir."""

from html import escape

import streamlit as st

from backend.data_service import DataService
from components.content_views import (
    is_beginner,
    render_adv_dis,
    render_comparison_table,
    render_diagram_legend,
    render_formula_cards,
    render_foundation_layer,
    render_global_tt_trl,
    render_use_cases,
)
from components.ui_helpers import current_view_mode, first_text, select_section, show_empty, show_error, show_plotly
from i18n.core import get_lang, t


def _teach_note(text: str) -> None:
    if not text:
        return
    st.markdown(f'<p class="teach-note">{escape(str(text))}</p>', unsafe_allow_html=True)


def _section_label(key: str) -> None:
    st.markdown(
        f'<div class="section-label">{escape(t(key).lstrip("#").strip())}</div>',
        unsafe_allow_html=True,
    )


TECH_SECTION_KEYS = [
    "definition",
    "principle",
    "architecture",
    "use_cases",
    "adv_dis",
    "global_tt",
    "performance",
]

_all_technologies = DataService.get_all_technologies()
selected_tech_id = st.selectbox(
    t("tech.select"),
    options=list(_all_technologies.keys()),
    format_func=lambda x: t(
        "tech.select_fmt",
        icon=_all_technologies[x]["icon"],
        title=_all_technologies[x]["title"],
        trl=_all_technologies[x]["trl"],
    ),
)

tech = _all_technologies[selected_tech_id]
beginner = is_beginner(current_view_mode())
trl_class = "trl-low" if tech["trl"] <= 4 else ("trl-mid" if tech["trl"] == 5 else "trl-high")
depth_cls = "depth-badge-beginner" if beginner else "depth-badge-expert"
lead = tech.get("beginner_kicker") if beginner else first_text(tech.get("trl_desc"))

st.markdown(
    f"""<div class="glass-card tech-banner">
<div class="tech-banner-row">
<div>
<span class="tt-badge">{t("tech.badge")}</span>
<span class="depth-badge {depth_cls}">{t("depth.beginner") if beginner else t("depth.expert")}</span>
<div class="tech-banner-title">{tech['icon']} {tech['title']}</div>
</div>
<span class="trl-pill {trl_class}">{t("trl.maturity", n=tech["trl"])}</span>
</div>
<p class="tech-banner-lead">{escape(lead)}</p>
</div>""",
    unsafe_allow_html=True,
)

_section_labels = [t(f"tech.section.{k}") for k in TECH_SECTION_KEYS]
_section_map = dict(zip(_section_labels, TECH_SECTION_KEYS))
section = _section_map.get(
    select_section(
        t("tech.section_label"),
        _section_labels,
        key=f"tech_section_sb_{selected_tech_id}_{get_lang()}",
    ),
    TECH_SECTION_KEYS[0],
)

if section == "definition":
    render_foundation_layer(tech, compact=not beginner)
    if not beginner:
        render_comparison_table(tech)
        _teach_note(t("tech.math_on_arch"))

elif section == "principle":
    from components.diagrams import render_technology_diagram

    col_p_text, col_p_diag = st.columns([1, 1.1])
    with col_p_text:
        _section_label("tech.principle_beginner" if beginner else "tech.principle_expert")
        if beginner:
            st.markdown(
                f"""<div class="glass-card">
<div style="color:#E2E8F0;font-size:0.98rem;line-height:1.65;">
{first_text(tech.get("beginner_principle"), tech.get("working_principle"))}
</div>
</div>""",
                unsafe_allow_html=True,
            )
        else:
            recall = first_text(tech.get("beginner_principle"))
            if recall:
                with st.expander(t("tech.principle_recall"), expanded=False):
                    st.markdown(
                        f"""<div class="dual-card-beginner">
<div style="color:#E2E8F0;font-size:0.9rem;line-height:1.6;">{recall}</div>
</div>""",
                        unsafe_allow_html=True,
                    )
            st.markdown(
                f"""<div class="glass-card">
<div style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;">
{first_text(tech.get("working_principle"))}
</div>
</div>""",
                unsafe_allow_html=True,
            )
    with col_p_diag:
        _section_label("tech.diagram")
        render_technology_diagram(tech["id"])
        render_diagram_legend(tech["id"])

elif section == "architecture":
    _section_label("tech.arch_heading")
    arch = first_text(tech.get("beginner_arch"))
    st.markdown(
        f"""<div class="dual-card-beginner">
<div class="teach-label">{escape(t("tech.arch_layers"))}</div>
<div style="color:#E2E8F0;font-size:0.95rem;line-height:1.65;margin-top:8px;">
{arch}
</div>
</div>""",
        unsafe_allow_html=True,
    )
    if not beginner:
        st.markdown(
            f"""<div class="dual-card-expert">
<div class="teach-label">{escape(t("tech.arch_expert"))}</div>
<div style="color:#E2E8F0;font-size:0.92rem;line-height:1.6;margin-top:8px;">
{tech['system_architecture']}
</div>
</div>""",
            unsafe_allow_html=True,
        )
        render_formula_cards(tech)

elif section == "use_cases":
    render_use_cases(tech, beginner=beginner)

elif section == "adv_dis":
    render_adv_dis(tech, beginner=beginner)

elif section == "global_tt":
    render_global_tt_trl(tech, beginner=beginner, trl_class=trl_class)

else:
    from backend.academic_service import AcademicService
    from backend.config import get_lens_token, get_springer_api_key
    from backend.patent_service import PatentService, TECH_ID_TO_DOMAIN
    from backend.springer_live import ensure_prefetch as ensure_springer
    from components.charts import (
        render_academic_trends_chart,
        render_technology_performance_charts,
        render_technology_record_counts_chart,
    )

    _section_label("tech.perf_heading")
    _teach_note(t("tech.perf_caption"))
    perf_figs, perf_note = render_technology_performance_charts(tech["id"])
    if perf_figs:
        if perf_note:
            _teach_note(perf_note)
        for fig in perf_figs:
            show_plotly(fig)
    else:
        show_empty(t("tech.empty_perf"))

    st.divider()
    _section_label("tech.records_heading")
    _teach_note(t("tech.records_caption"))
    domain = PatentService.domain_for_tech(tech["id"])
    pub_topic = TECH_ID_TO_DOMAIN.get(tech["id"])

    if not get_lens_token():
        show_empty(t("tech.empty_patents_token"))
    else:
        df_pat = PatentService.get_domain_yearly_df(tech["id"])
        if df_pat.empty:
            show_empty(t("tech.empty_patents", domain=domain or tech["acronym"]))
        else:
            show_plotly(render_technology_record_counts_chart(df_pat, domain or tech["acronym"]))
            st.caption(t("tech.pat_chart_caption"))

    if not get_springer_api_key():
        show_empty(t("tech.empty_pub_token"))
    elif pub_topic:
        from backend.live_refresh import render_watch

        ensure_springer()
        render_watch("springer", "pub")
        df_pub = AcademicService.get_topic_yearly_df(pub_topic)
        if df_pub is None or df_pub.empty:
            show_empty(t("tech.pub_fail"))
        else:
            show_plotly(render_academic_trends_chart(df_pub, t("pub.chart_trend")))
            st.caption(t("tech.pub_chart_caption"))
    else:
        show_empty(t("tech.pub_fail"))

    st.divider()
    _section_label("tech.refs")
    _teach_note(t("tech.refs_caption"))
    ref_items = "".join(
        [
            f"""<p style='margin-bottom:8px; font-size:0.88rem; line-height:1.5; overflow-wrap:anywhere;'>
            📖 <a href="{ref['url']}" target="_blank" rel="noopener noreferrer"
            style="color:#00E5FF; text-decoration:none; border-bottom:1px solid rgba(0,229,255,0.35);">
            {ref['text']}</a></p>"""
            for ref in tech["references"]
        ]
    )
    st.markdown(f"""<div class="glass-card">{ref_items}</div>""", unsafe_allow_html=True)
