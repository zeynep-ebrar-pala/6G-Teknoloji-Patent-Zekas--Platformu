"""
Türk Telekom 6G Platform - Türk Telekom Specific Scenarios Frontend Component
Renders interactive Turkish telecom deployment scenario UI using Backend ScenarioEngine.
"""

import streamlit as st

from backend.scenario_engine import DENSITY_KEYS, PRIORITY_KEYS, REGION_KEYS, ScenarioEngine
from i18n.core import format_decimal, format_int, get_lang, t


def render_tt_scenario_calculator(compact_header: bool = False):
    """Interactive deployment scenario UI — simulation output, not field KPIs."""

    if not compact_header:
        st.markdown(
            f"""<div class="glass-card" style="border-left: 5px solid #64748B; margin-bottom: 20px;">
<h2 style="color: #FFFFFF; margin: 0 0 6px 0; font-size: 1.45rem; overflow-wrap: anywhere;">{t("scenario.title")}</h2>
<p style="color: #CBD5E1; font-size: 0.92rem; margin: 0 0 10px 0;">
{t("scenario.lead")}
</p>
{t("scenario.kpi_body")}
</div>""",
            unsafe_allow_html=True,
        )
    else:
        st.caption(t("scenario.lead"))
        with st.expander(t("scenario.assumptions_title"), expanded=False):
            st.markdown(t("scenario.kpi_body"), unsafe_allow_html=True)

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
            st.markdown(
                f'<span class="trl-pill trl-low" style="margin-bottom:8px;">{t("scenario.sim_badge")}</span>',
                unsafe_allow_html=True,
            )
            st.markdown(t("scenario.result_heading"))

            c_header_1, c_header_2 = st.columns([2.2, 1])
            with c_header_1:
                st.markdown(f"#### {eval_res['region_title']}")
            with c_header_2:
                st.caption(f"{t('scenario.year_label')}: {eval_res['target_year']}")

            tech_str = "  ".join([f"`{tech}`" for tech in eval_res["recommended_tech"]])
            st.markdown(t("scenario.techs", techs=tech_str))

            st.divider()

            st.markdown(f"**{t('scenario.solution_label')}**\n{eval_res['solution']}")
            st.write("")

            st.info(
                f"**{t('scenario.priority_label')}**\n{eval_res['priority_kpi']}\n\n"
                f"{t('scenario.density_profile', value=eval_res['density_kpi'])}"
            )

            st.divider()

            _render_sim_metric_row(eval_res)

            st.write("")
            score = format_int(eval_res["feasibility_score"])
            score_disp = f"%{score}" if get_lang() == "tr" else f"{score}%"
            st.markdown(t("scenario.feasibility", score=score_disp))
            st.caption(t("scenario.feasibility_note"))
            st.progress(eval_res["feasibility_score"] / 100.0)

            _render_verified_bridge(eval_res["recommended_tech"])


def _render_sim_metric_row(eval_res: dict) -> None:
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    capacity = format_int(eval_res["capacity_gbps"])
    latency = format_decimal(eval_res["latency_ms"], 1)
    energy = format_int(eval_res["energy_score"])
    energy_disp = f"%{energy}" if get_lang() == "tr" else f"{energy}%"
    sim = t("scenario.sim_badge")
    with kpi_col1:
        st.markdown(
            f"""<div style="background:rgba(100,116,139,0.25);border:1px dashed #64748B;border-radius:8px;padding:10px;">
<div style="color:#94A3B8;font-size:0.72rem;">{sim}</div>
<div style="color:#CBD5E1;font-size:0.8rem;">{t("scenario.metric_speed")}</div>
<div style="color:#FFFFFF;font-size:1.4rem;font-weight:700;">{capacity} Gbps</div>
</div>""",
            unsafe_allow_html=True,
        )
    with kpi_col2:
        st.markdown(
            f"""<div style="background:rgba(100,116,139,0.25);border:1px dashed #64748B;border-radius:8px;padding:10px;">
<div style="color:#94A3B8;font-size:0.72rem;">{sim}</div>
<div style="color:#CBD5E1;font-size:0.8rem;">{t("scenario.metric_latency")}</div>
<div style="color:#FFFFFF;font-size:1.4rem;font-weight:700;">{latency} ms</div>
</div>""",
            unsafe_allow_html=True,
        )
    with kpi_col3:
        st.markdown(
            f"""<div style="background:rgba(100,116,139,0.25);border:1px dashed #64748B;border-radius:8px;padding:10px;">
<div style="color:#94A3B8;font-size:0.72rem;">{sim}</div>
<div style="color:#CBD5E1;font-size:0.8rem;">{t("scenario.metric_energy")}</div>
<div style="color:#FFFFFF;font-size:1.4rem;font-weight:700;">{energy_disp}</div>
</div>""",
            unsafe_allow_html=True,
        )


_TECH_LABEL_TO_ID = {
    "ISAC": "isac",
    "RIS": "ris",
    "THz": "thz",
    "THz Communication": "thz",
    "Sub-THz": "thz",
    "Cell-Free Massive MIMO": "cell_free",
    "AI-Native RAN": "ai_ran",
    "Ambient IoT": "ambient_iot",
    "NTN (satellite)": "ntn",
    "NTN": "ntn",
}


def _resolve_tech_id(label: str) -> str | None:
    if label in _TECH_LABEL_TO_ID:
        return _TECH_LABEL_TO_ID[label]
    low = label.lower()
    for key, tid in _TECH_LABEL_TO_ID.items():
        if key.lower() in low or low in key.lower():
            return tid
    return None


def _render_verified_bridge(recommended_tech: list[str]) -> None:
    st.divider()
    st.markdown(t("scenario.verified_bridge_heading"))
    surfaces = {}
    try:
        from data.beginner_surfaces import BEGINNER_SURFACES

        surfaces = BEGINNER_SURFACES
    except ImportError:
        pass

    techs = DataService.get_all_technologies()
    shown: set[str] = set()
    for label in recommended_tech:
        tid = _resolve_tech_id(label)
        if not tid or tid in shown:
            continue
        shown.add(tid)
        tech = techs.get(tid) or {}
        items = (surfaces.get(tid, {}).get("tt_scenarios") or tech.get("tt_scenarios") or [])[:2]
        if not items:
            st.caption(f"`{label}` — {t('scenario.verified_bridge_none')}")
            continue
        st.markdown(f"**{t('scenario.verified_bridge_open', title=tech.get('title', label))}**")
        for item in items:
            if isinstance(item, dict):
                st.markdown(f"- **{item.get('title', '')}** — {item.get('body', '')}")
            else:
                st.markdown(f"- {item}")
    try:
        st.page_link("views/tech.py", label=t("scenario.open_tech_explorer"), icon="📡")
    except Exception:
        pass
