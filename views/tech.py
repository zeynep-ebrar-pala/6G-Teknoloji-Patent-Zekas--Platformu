"""6G Teknolojileri — yalnızca seçilen bölüm yüklenir."""

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
from components.ui_helpers import (
    current_view_mode,
    first_text,
    show_empty,
    show_error,
    show_plotly,
)
from i18n.core import t
from i18n.widgets import select_keyed_section

TECH_SECTION_KEYS = [
    "definition",
    "principle",
    "architecture",
    "use_cases",
    "adv_dis",
    "global_tt",
    "performance",
]

TECHNOLOGIES = DataService.get_all_technologies()
selected_tech_id = st.selectbox(
    t("tech.select"),
    options=list(TECHNOLOGIES.keys()),
    format_func=lambda x: t(
        "tech.select_fmt",
        icon=TECHNOLOGIES[x]["icon"],
        title=TECHNOLOGIES[x]["title"],
        trl=TECHNOLOGIES[x]["trl"],
    ),
)

tech = DataService.get_technology_by_id(selected_tech_id)
beginner = is_beginner(current_view_mode())
trl_class = "trl-low" if tech["trl"] <= 4 else ("trl-mid" if tech["trl"] == 5 else "trl-high")

st.markdown(
    f"""<div class="glass-card" style="border-left: 6px solid #0099FF;">
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
<div>
<span class="tt-badge">{t("tech.badge")}</span>
<h2 style="color: #FFF; margin: 4px 0 0 0; overflow-wrap: anywhere;">{tech['icon']} {tech['title']}</h2>
</div>
<span class="trl-pill {trl_class}">{t("trl.maturity", n=tech["trl"])}</span>
</div>
</div>""",
    unsafe_allow_html=True,
)

section = select_keyed_section(
    t("tech.section_label"),
    TECH_SECTION_KEYS,
    key=f"tech_section_{selected_tech_id}",
    prefix="tech.section",
)

if section == "definition":
    st.markdown(t("tech.def_heading"))
    render_foundation_layer(tech, compact=not beginner)
    if not beginner:
        st.markdown(
            f"""<div class="dual-card-expert">
<h4 style="color:#00C2FF;margin-top:0;margin-bottom:12px;">{t("tech.expert_def")}</h4>
<div style="color:#E2E8F0;font-size:0.95rem;line-height:1.6;">
{tech['system_architecture']}
</div>
</div>""",
            unsafe_allow_html=True,
        )
        render_comparison_table(tech)

elif section == "principle":
    from components.diagrams import render_technology_diagram

    col_p_text, col_p_diag = st.columns([1, 1.1])
    with col_p_text:
        principle = first_text(
            tech.get("beginner_principle") if beginner else None,
            tech.get("working_principle"),
        )
        heading = t("tech.principle_beginner") if beginner else t("tech.principle_expert")
        st.markdown(f"### {heading}")
        if not beginner:
            st.markdown(
                f"""<div class="dual-card-beginner">
<div style="color:#E2E8F0;font-size:0.9rem;line-height:1.6;">
{first_text(tech.get("beginner_principle"))}
</div>
</div>""",
                unsafe_allow_html=True,
            )
        st.markdown(
            f"""<div class="glass-card">
<div style="color:#E2E8F0;font-size:0.95rem;line-height:1.65;">
{principle}
</div>
</div>""",
            unsafe_allow_html=True,
        )
    with col_p_diag:
        st.markdown(t("tech.diagram"))
        render_technology_diagram(tech["id"])
        render_diagram_legend(tech["id"])

elif section == "architecture":
    st.markdown(t("tech.arch_heading"))
    arch = first_text(tech.get("beginner_arch"))
    st.markdown(
        f"""<div class="dual-card-beginner">
<h4 style="color:#00C853;margin-top:0;">{t("tech.arch_layers")}</h4>
<div style="color:#E2E8F0;font-size:0.95rem;line-height:1.65;">
{arch}
</div>
</div>""",
        unsafe_allow_html=True,
    )
    if not beginner:
        st.markdown(
            f"""<div class="dual-card-expert">
<h4 style="color:#00C2FF;margin-top:0;">{t("tech.arch_expert")}</h4>
<div style="color:#E2E8F0;font-size:0.92rem;line-height:1.6;">
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
    from backend.patent_service import PatentService
    from components.charts import (
        render_academic_trends_chart,
        render_technology_record_counts_chart,
    )

    st.markdown(t("tech.perf_heading"))
    st.caption(t("tech.perf_caption"))
    domain = PatentService.domain_for_tech(tech["id"])
    df_pat = PatentService.get_domain_yearly_df(tech["id"])
    if df_pat.empty:
        show_empty(t("tech.empty_patents", domain=domain or tech["acronym"]))
    else:
        show_plotly(render_technology_record_counts_chart(df_pat, domain or tech["acronym"]))

    openalex_topic = {
        "isac": "ISAC",
        "ris": "RIS",
        "thz": "THz",
        "ai_ran": "AI-RAN",
        "ntn": "NTN",
        "ambient_iot": "Ambient IoT",
    }.get(tech["id"])
    if openalex_topic:
        df_pub = AcademicService.get_topic_yearly_df(openalex_topic)
        if df_pub is None or df_pub.empty:
            show_error(t("tech.openalex_fail"))
        else:
            show_plotly(render_academic_trends_chart(df_pub))
    else:
        st.caption(t("tech.cell_free_oa"))

    st.divider()
    st.markdown(t("tech.refs"))
    st.caption(t("tech.refs_caption"))
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
