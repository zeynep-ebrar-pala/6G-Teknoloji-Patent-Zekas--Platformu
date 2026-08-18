"""
İki kademeli içerik gösterimi: temel katman, formül kartları, karşılaştırma, kullanım/TRL.
"""

from __future__ import annotations

from html import escape

import streamlit as st

from data.glossary import GLOSSARY, localized_entry, trl_scale
from i18n.core import t

_TEACH_KEYS = (
    ("problem", "teach.problem"),
    ("why_needed", "teach.why_needed"),
    ("what", "teach.what"),
    ("tt_impact", "teach.tt_impact"),
)


def is_beginner(view_mode: str | None = None) -> bool:
    if view_mode is None:
        view_mode = st.session_state.get("view_mode", "beginner")
    text = str(view_mode or "beginner")
    if text in ("beginner", "expert"):
        return text == "beginner"
    if "Uzman" in text or "Expert" in text:
        return False
    return True


def render_foundation_layer(tech: dict, *, compact: bool = False) -> None:
    """Temel kavramsal katman — uzman modda da atlanmaz."""
    fnd = tech.get("foundation") or {}
    if not fnd:
        return
    heading = t("teach.heading_compact") if compact else t("teach.heading")
    st.markdown(
        f"""<div class="dual-card-beginner">
<h4 style="margin-top:0;margin-bottom:14px;">{heading}</h4>
</div>""",
        unsafe_allow_html=True,
    )
    items = []
    for key, label_key in _TEACH_KEYS:
        text = fnd.get(key)
        if text:
            items.append(
                "<div class='teach-item'>"
                f"<div class='teach-label'>{escape(t(label_key))}</div>"
                f"<p>{escape(str(text))}</p></div>"
            )
    if items:
        st.markdown(f"<div class='teach-grid'>{''.join(items)}</div>", unsafe_allow_html=True)

    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("teach.mental_model")}</div>
<p style="color:#E2E8F0;line-height:1.65;margin:8px 0 0 0;">{escape(str(fnd.get('mental_model') or ''))}</p>
</div>""",
        unsafe_allow_html=True,
    )
    analogy = fnd.get("analogy")
    tech_map = fnd.get("analogy_technical_map")
    if analogy:
        st.markdown(
            f"""<div class="glass-card">
<div class="teach-label">{t("teach.analogy")}</div>
<p style="color:#E2E8F0;line-height:1.65;margin:8px 0 12px 0;">{escape(str(analogy))}</p>
<div class="teach-label">{t("teach.analogy_map")}</div>
<p style="color:#CBD5E1;line-height:1.65;margin:8px 0 0 0;">{escape(str(tech_map or ''))}</p>
</div>""",
            unsafe_allow_html=True,
        )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #00C853;">
<div class="teach-label">{t("teach.when_used")}</div>
<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.6;margin:8px 0 0 0;">{escape(str(fnd.get('when_used') or ''))}</p>
</div>""",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #FF5252;">
<div class="teach-label">{t("teach.when_not")}</div>
<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.6;margin:8px 0 0 0;">{escape(str(fnd.get('when_not') or ''))}</p>
</div>""",
            unsafe_allow_html=True,
        )
    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("teach.not_to_confuse")}</div>
<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 12px 0;">{escape(str(fnd.get('not_to_confuse') or ''))}</p>
<div class="teach-label">{t("teach.real_world")}</div>
<p style="color:#CBD5E1;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">{escape(str(fnd.get('real_world') or ''))}</p>
</div>""",
        unsafe_allow_html=True,
    )

    steps = fnd.get("how_steps") or []
    if steps and not compact:
        lis = "".join(f"<li style='margin-bottom:8px;line-height:1.55;'>{escape(str(s))}</li>" for s in steps)
        st.markdown(
            f"""<div class="glass-card">
<div class="teach-label">{t("teach.how_steps")}</div>
<ol style="color:#E2E8F0;font-size:0.92rem;margin:10px 0 0 18px;padding:0;">{lis}</ol>
</div>""",
            unsafe_allow_html=True,
        )


def render_formula_cards(tech: dict) -> None:
    formulas = tech.get("formulas") or []
    if not formulas:
        legacy = tech.get("mathematical_foundation")
        if legacy:
            st.markdown(f"<div class='formula-box'>{legacy}</div>", unsafe_allow_html=True)
        return
    st.markdown(t("teach.formula_heading"))
    st.caption(t("teach.formula_caption"))
    for formula in formulas:
        st.markdown(
            f"""<div class="formula-card">
<div class="teach-label">{t("teach.equation")}</div>
<h4 style="color:#00E5FF;margin:6px 0 10px 0;">{escape(formula.get('name', t('teach.formula_fallback')))}</h4>
</div>""",
            unsafe_allow_html=True,
        )
        latex = formula.get("latex") or ""
        if latex:
            st.latex(latex)
        symbols = formula.get("symbols") or []
        if symbols:
            rows = "".join(
                "<tr>"
                f"<td class='sym'>{escape(s.get('symbol', ''))}</td>"
                f"<td>{escape(s.get('meaning', ''))}</td>"
                f"<td>{escape(s.get('unit', ''))}</td>"
                "</tr>"
                for s in symbols
            )
            st.markdown(
                f"""<table class="symbol-table">
<thead><tr><th>{t("teach.symbol")}</th><th>{t("teach.meaning")}</th><th>{t("teach.unit")}</th></tr></thead>
<tbody>{rows}</tbody>
</table>""",
                unsafe_allow_html=True,
            )
        blocks = (
            (t("teach.tells_us"), formula.get("tells_us")),
            (t("teach.why_this_form"), formula.get("why_this_form")),
            (t("teach.when_valid"), formula.get("when_valid")),
            (t("teach.if_variable_changes"), formula.get("if_variable_changes")),
            (t("teach.assumptions"), formula.get("assumptions")),
            (t("teach.simple_example"), formula.get("simple_example")),
        )
        body = "".join(
            f"<p style='margin:0 0 10px 0;line-height:1.6;'><strong>{escape(title)}:</strong> {escape(str(text))}</p>"
            for title, text in blocks
            if text
        )
        if body:
            st.markdown(f"<div class='glass-card'>{body}</div>", unsafe_allow_html=True)


def render_comparison_table(tech: dict) -> None:
    cmp_ = tech.get("comparison") or {}
    rows = cmp_.get("rows") or []
    headers = cmp_.get("headers") or []
    if not rows or not headers:
        return
    st.markdown(f"#### {cmp_.get('title', t('teach.use_cases'))}")
    head = "".join(f"<th>{escape(h)}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{escape(str(c))}</td>" for c in row) + "</tr>" for row in rows
    )
    st.markdown(
        f"""<div style="overflow-x:auto;">
<table class="compare-table">
<thead><tr>{head}</tr></thead>
<tbody>{body}</tbody>
</table>
</div>""",
        unsafe_allow_html=True,
    )


def render_use_cases(tech: dict, *, beginner: bool) -> None:
    st.markdown(t("teach.use_cases"))
    st.caption(t("teach.use_cases_caption"))
    cols = st.columns(2)
    for idx, uc in enumerate(tech.get("use_cases") or []):
        if isinstance(uc, dict):
            title = uc.get("title", t("teach.scenario_n", n=idx + 1))
            desc = uc.get("description", "")
            how = uc.get("how", "")
            when_not = uc.get("when_not", "")
        else:
            title, desc, how, when_not = t("teach.scenario_n", n=idx + 1), str(uc), "", ""
        extra = ""
        if not beginner and (how or when_not):
            extra = (
                f"<p style='color:#94A3B8;font-size:0.84rem;margin:10px 0 0 0;line-height:1.5;'>"
                f"<strong style='color:#00E5FF;'>{t('teach.how')}</strong> {escape(how)}</p>"
                if how
                else ""
            )
            if when_not:
                extra += (
                    f"<p style='color:#94A3B8;font-size:0.84rem;margin:8px 0 0 0;line-height:1.5;'>"
                    f"<strong style='color:#FFB020;'>{t('teach.when_not_short')}</strong> {escape(when_not)}</p>"
                )
        with cols[idx % 2]:
            st.markdown(
                f"""<div class="glass-card" style="margin-bottom:12px;border-left:4px solid #00E5FF;">
<h4 style="color:#00E5FF;margin:0 0 8px 0;">{escape(title)}</h4>
<p style="color:#E2E8F0;font-size:0.9rem;margin:0;line-height:1.55;">{escape(desc)}</p>
{extra}
</div>""",
                unsafe_allow_html=True,
            )


def render_adv_dis(tech: dict, *, beginner: bool) -> None:
    c_adv, c_dis = st.columns(2)
    adv_why = tech.get("adv_why") or []
    dis_why = tech.get("dis_why") or []
    with c_adv:
        st.markdown(t("teach.advantages"))
        items = []
        for i, adv in enumerate(tech.get("advantages") or []):
            why = adv_why[i] if (not beginner and i < len(adv_why)) else ""
            why_html = (
                f"<div style='color:#94A3B8;font-size:0.84rem;margin-top:4px;line-height:1.5;'>{escape(why)}</div>"
                if why
                else ""
            )
            items.append(
                f"<li style='margin-bottom:12px;line-height:1.5;'>"
                f"<strong style='color:#00C853;'>✓</strong> {escape(str(adv))}{why_html}</li>"
            )
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #00C853;">
<ul style="list-style:none;padding-left:0;margin:0;color:#E2E8F0;font-size:0.92rem;">
{''.join(items)}
</ul></div>""",
            unsafe_allow_html=True,
        )
    with c_dis:
        st.markdown(t("teach.disadvantages"))
        items = []
        for i, dis in enumerate(tech.get("disadvantages") or []):
            why = dis_why[i] if (not beginner and i < len(dis_why)) else ""
            why_html = (
                f"<div style='color:#94A3B8;font-size:0.84rem;margin-top:4px;line-height:1.5;'>{escape(why)}</div>"
                if why
                else ""
            )
            items.append(
                f"<li style='margin-bottom:12px;line-height:1.5;'>"
                f"<strong style='color:#FF5252;'>✗</strong> {escape(str(dis))}{why_html}</li>"
            )
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #FF5252;">
<ul style="list-style:none;padding-left:0;margin:0;color:#E2E8F0;font-size:0.92rem;">
{''.join(items)}
</ul></div>""",
            unsafe_allow_html=True,
        )


def render_global_tt_trl(tech: dict, *, beginner: bool, trl_class: str) -> None:
    c_g, c_tt_box, c_t_level = st.columns([1, 1, 0.9])
    global_why = tech.get("global_why") or []
    tt_why = tech.get("tt_why") or []
    with c_g:
        st.markdown(t("teach.global"))
        if beginner:
            st.caption(t("teach.global_caption"))
        items = []
        for i, gr in enumerate(tech.get("global_research") or []):
            why = global_why[i] if i < len(global_why) else ""
            why_html = (
                f"<div style='color:#94A3B8;font-size:0.82rem;margin-top:4px;line-height:1.45;'>{escape(why)}</div>"
                if why
                else ""
            )
            items.append(
                f"<li style='margin-bottom:10px;line-height:1.5;'>"
                f"<span style='color:#00C2FF;'>🔹</span> <strong style='color:#FFFFFF;'>{escape(str(gr))}</strong>"
                f"{why_html}</li>"
            )
        st.markdown(
            f"""<div class="glass-card"><ul style="list-style:none;padding-left:0;margin:0;color:#E2E8F0;font-size:0.9rem;">
{''.join(items)}</ul></div>""",
            unsafe_allow_html=True,
        )
    with c_tt_box:
        st.markdown(t("teach.tt_scenarios"))
        st.caption(t("teach.tt_caption"))
        chunks = []
        for i, tt_sc in enumerate(tech.get("tt_scenarios") or []):
            why = tt_why[i] if i < len(tt_why) else ""
            why_html = (
                f"<span style='display:block;color:#94A3B8;font-size:0.82rem;margin-top:4px;'>{escape(why)}</span>"
                if why
                else ""
            )
            chunks.append(
                f"<p style='margin-bottom:12px;line-height:1.5;font-size:0.9rem;color:#E2E8F0;'>{tt_sc}{why_html}</p>"
            )
        st.markdown(
            f"""<div class="glass-card" style="border-left:4px solid #FFB020;">{''.join(chunks)}</div>""",
            unsafe_allow_html=True,
        )
    with c_t_level:
        st.markdown(t("teach.trl_assess"))
        st.markdown(
            f"""<div class="glass-card" style="text-align:center;">
<span class="trl-pill {trl_class}" style="font-size:1.3rem;padding:10px 24px;">{t("trl.pill", n=tech["trl"])}</span>
<p style="color:#CBD5E1;font-size:0.88rem;margin-top:14px;line-height:1.5;text-align:left;">{escape(str(tech.get('trl_desc') or ''))}</p>
</div>""",
            unsafe_allow_html=True,
        )
        scale_rows = "".join(
            f"<tr><td style='white-space:nowrap;color:#00E5FF;font-weight:700;'>{escape(r['level'])}</td>"
            f"<td><strong>{escape(r['title'])}</strong> — {escape(r['meaning'])}</td></tr>"
            for r in trl_scale()
        )
        st.markdown(
            f"""<table class="symbol-table">
<thead><tr><th>{escape(t('trl.scale_header'))}</th><th>{escape(t('trl.scale_title'))}</th></tr></thead>
<tbody>{scale_rows}</tbody>
</table>""",
            unsafe_allow_html=True,
        )


def render_trl_explainer() -> None:
    trl = localized_entry("TRL") or GLOSSARY["TRL"]
    st.markdown(
        f"""<div class="glass-card">
<h4 style="color:#00E5FF;margin-top:0;">{t("trl.explainer_title")}</h4>
<p style="font-size:1rem;color:#C8D1DC;line-height:1.65;">
<strong>{escape(t("trl.explainer_lead", abbr=trl["abbr"], en=trl["en"], tr=trl["tr"], definition=trl["definition"], why=trl["why"]))}</strong>
</p>
<p style="font-size:0.96rem;color:#94A3B8;line-height:1.6;">
{escape(t("trl.explainer_body"))}
</p>
<ul style="font-size:0.96rem;color:#CBD5E1;padding-left:20px;line-height:1.7;">
<li><strong style="color:#00C853;">{escape(t("trl.explainer_ntn"))}</strong></li>
<li><strong style="color:#FFB020;">{escape(t("trl.explainer_ris"))}</strong></li>
<li><strong style="color:#FF5252;">{escape(t("trl.explainer_lab"))}</strong></li>
<li><strong style="color:#FF7043;">{escape(t("trl.explainer_thz"))}</strong></li>
</ul>
</div>""",
        unsafe_allow_html=True,
    )


def render_diagram_legend(tech_id: str) -> None:
    text = t(f"diagram.legend_{tech_id}")
    if not text or text == f"diagram.legend_{tech_id}":
        return
    st.markdown(
        f"""<div class="glass-card" style="margin-top:8px;">
<div class="teach-label">{t("teach.diagram_terms")}</div>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:8px 0 0 0;">{text}</p>
</div>""",
        unsafe_allow_html=True,
    )
