"""
Türk Telekom 6G Platform - Türk Telekom Specific Scenarios Frontend Component
Renders interactive Turkish telecom deployment scenario UI using Backend ScenarioEngine.
"""

import streamlit as st

from backend.scenario_engine import DENSITY_KEYS, PRIORITY_KEYS, REGION_KEYS, ScenarioEngine
from i18n.core import format_decimal, format_int, get_lang, t


def render_tt_scenario_calculator():
    """Interactive deployment scenario UI component for Türk Telekom Ar-Ge."""

    st.markdown(
        f"""<div class="glass-card" style="border-left: 5px solid #0099FF; margin-bottom: 20px;">
<h2 style="color: #FFFFFF; margin: 0 0 6px 0; font-size: 1.45rem; overflow-wrap: anywhere;">{t("scenario.title")}</h2>
<p style="color: #CBD5E1; font-size: 0.92rem; margin: 0 0 10px 0;">
{t("scenario.lead")}
</p>
{t("scenario.kpi_body")}
</div>""",
        unsafe_allow_html=True,
    )

    col_inputs, col_results = st.columns([1, 1.15])

    with col_inputs:
        with st.container(border=True):
            st.markdown(t("scenario.params"))

            region = st.selectbox(
                t("scenario.region"),
                list(REGION_KEYS),
                format_func=lambda k: t(f"scenario.region_{k}"),
                help=t("scenario.region_help"),
                key="tt_region",
            )

            user_density = st.select_slider(
                t("scenario.density"),
                options=list(DENSITY_KEYS),
                format_func=lambda k: t(f"scenario.density_{k}"),
                help=t("scenario.density_help"),
                key="tt_density",
            )

            priority = st.radio(
                t("scenario.priority"),
                list(PRIORITY_KEYS),
                format_func=lambda k: t(f"scenario.priority_{k}"),
                help=t("scenario.priority_help"),
                key="tt_priority",
            )

        eval_res = ScenarioEngine.evaluate_scenario(region, user_density, priority)

        st.write("")
        with st.expander(t("scenario.metrics_exp"), expanded=True):
            st.markdown(eval_res["impact_summary"])
            st.caption(t("scenario.capex_caption", value=eval_res["capex_estimate"]))

    with col_results:
        st.caption(t("scenario.kpi_note"))
        with st.container(border=True):
            st.markdown(t("scenario.result_heading"))

            c_header_1, c_header_2 = st.columns([2.2, 1])
            with c_header_1:
                st.markdown(f"#### {eval_res['region_title']}")
            with c_header_2:
                st.info(eval_res["target_year"])

            tech_str = "  ".join([f"`{tech}`" for tech in eval_res["recommended_tech"]])
            st.markdown(t("scenario.techs", techs=tech_str))

            st.divider()

            st.markdown(f"{t('scenario.solution')}\n{eval_res['solution']}")
            st.write("")

            st.success(
                f"{t('scenario.priority_impact')}\n{eval_res['priority_kpi']}\n\n"
                f"{t('scenario.density_profile', value=eval_res['density_kpi'])}"
            )

            st.divider()

            kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
            with kpi_col1:
                st.metric(label=t("scenario.metric_speed"), value=f"{format_int(eval_res['capacity_gbps'])} Gbps")
            with kpi_col2:
                st.metric(
                    label=t("scenario.metric_latency"),
                    value=f"{format_decimal(eval_res['latency_ms'], 1)} ms",
                )
            with kpi_col3:
                energy = format_int(eval_res["energy_score"])
                st.metric(
                    label=t("scenario.metric_energy"),
                    value=f"%{energy}" if get_lang() == "tr" else f"{energy}%",
                )

            st.write("")
            score = format_int(eval_res["feasibility_score"])
            score_disp = f"%{score}" if get_lang() == "tr" else f"{score}%"
            st.markdown(t("scenario.feasibility", score=score_disp))
            st.progress(eval_res["feasibility_score"] / 100.0)
