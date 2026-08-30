"""
İki kademeli içerik gösterimi: temel katman, formül kartları, karşılaştırma, kullanım/TRL.

Modül seviyesinde i18n/glossary import etmez: Streamlit Cloud (Python 3.14)
sayfa yüklemesinde ImportError üretmesin.
"""

from __future__ import annotations

from html import escape

import streamlit as st


def t(key: str, **kwargs):
    from i18n.core import t as translate

    return translate(key, **kwargs)


def _plain_label(key: str) -> str:
    return t(key).lstrip("#").strip()


def render_teach_note(text: str) -> None:
    """st.caption CSS ile gizlenir; öğretim notu HTML olarak kalır."""
    if not text:
        return
    st.markdown(f'<p class="teach-note">{escape(str(text))}</p>', unsafe_allow_html=True)


def render_section_label(key: str) -> None:
    st.markdown(f'<div class="section-label">{escape(_plain_label(key))}</div>', unsafe_allow_html=True)


def is_beginner(view_mode: str | None = None) -> bool:
    if view_mode is None:
        view_mode = st.session_state.get("view_mode", "beginner")
    text = str(view_mode or "beginner")
    if text in ("beginner", "expert"):
        return text == "beginner"
    if "Uzman" in text or "Expert" in text:
        return False
    return True


def _teach_item(label_key: str, body, n: int | None = None) -> str:
    if not body:
        return ""
    label = t(label_key)
    if n is not None:
        label = f"{n:02d}  ·  {label}"
    return (
        "<div class='teach-item'>"
        f"<div class='teach-label'>{escape(label)}</div>"
        f"<p>{escape(str(body))}</p></div>"
    )


def _teach_card(label_key: str, body, extra_class: str = "", muted: bool = False, n: int | None = None) -> str:
    if not body:
        return ""
    cls = "teach-muted" if muted else "teach-body"
    extra = f" {extra_class}" if extra_class else ""
    label = t(label_key)
    if n is not None:
        label = f"{n:02d}  ·  {label}"
    return (
        f"<div class='glass-card teach-card{extra}'>"
        f"<div class='teach-label'>{escape(label)}</div>"
        f"<p class='{cls}'>{escape(str(body))}</p>"
        "</div>"
    )


def _emit_stack(depth_cls: str, inner: str) -> None:
    if not inner.strip():
        return
    st.markdown(f'<div class="teach-stack {depth_cls}">{inner}</div>', unsafe_allow_html=True)


def render_foundation_layer(tech: dict, *, compact: bool = False) -> None:
    """Sıra: problem → ihtiyaç → yöntem → mekanizma → sınır → uygulama.

    Tek dev HTML yerine sahnelere bölünür: Streamlit kırpmasın, okuyucu sırayı kaçırmasın.
    """
    fnd = tech.get("foundation") or {}
    if not fnd:
        return
    beginner = not compact
    depth_cls = "depth-beginner" if beginner else "depth-expert"
    kicker = tech.get("beginner_kicker") if beginner else ""
    kicker_html = f'<div class="card-kicker">{escape(str(kicker))}</div>' if kicker else ""
    chips = t("teach.rail_beginner") if beginner else t("teach.rail_expert")
    chip_html = "".join(
        f"<span>{escape(part.strip())}</span>" for part in chips.split("·") if part.strip()
    )
    st.markdown(
        f"""<div class="teach-wrap {depth_cls}">
{kicker_html}
<p class="teach-note">{escape(t("teach.heading_expert") if compact else t("teach.heading"))}</p>
<div class="depth-rail">{chip_html}</div>
</div>""",
        unsafe_allow_html=True,
    )
    _emit_stack(
        depth_cls,
        f'<div class="teach-grid">{_teach_item("teach.problem", fnd.get("problem"), 1)}'
        f'{_teach_item("teach.why_needed", fnd.get("why_needed"), 2)}</div>',
    )
    _emit_stack(depth_cls, _teach_card("teach.what", fnd.get("what"), n=3))
    _emit_stack(depth_cls, _teach_card("teach.mental_model", fnd.get("mental_model"), n=4))
    steps = fnd.get("how_steps") or []
    if steps:
        lis = "".join(f"<li>{escape(str(s))}</li>" for s in steps)
        _emit_stack(
            depth_cls,
            "<div class='glass-card teach-card'>"
            f"<div class='teach-label'>05  ·  {escape(t('teach.how_steps'))}</div>"
            f"<ol class='teach-steps'>{lis}</ol></div>",
        )
    analogy = fnd.get("analogy")
    tech_map = fnd.get("analogy_technical_map")
    if analogy:
        tech_block = ""
        if not beginner and tech_map:
            tech_block = (
                f"<div class='teach-label'>{escape(t('teach.analogy_map'))}</div>"
                f"<p class='teach-muted'>{escape(str(tech_map))}</p>"
            )
        _emit_stack(
            depth_cls,
            "<div class='glass-card teach-card'>"
            f"<div class='teach-label'>06  ·  {escape(t('teach.analogy'))}</div>"
            f"<p class='teach-body'>{escape(str(analogy))}</p>"
            f"{tech_block}</div>",
        )
    _emit_stack(
        depth_cls,
        '<div class="teach-pair">'
        f'{_teach_card("teach.when_used", fnd.get("when_used"), "teach-used", n=7)}'
        f'{_teach_card("teach.when_not", fnd.get("when_not"), "teach-not", n=8)}'
        "</div>",
    )
    _emit_stack(depth_cls, _teach_card("teach.not_to_confuse", fnd.get("not_to_confuse"), n=9))
    _emit_stack(depth_cls, _teach_card("teach.real_world", fnd.get("real_world"), muted=True, n=10))
    _emit_stack(depth_cls, _teach_card("teach.tt_impact", fnd.get("tt_impact"), n=11))


def render_formula_cards(tech: dict) -> None:
    formulas = tech.get("formulas") or []
    if not formulas:
        legacy = tech.get("mathematical_foundation")
        if legacy:
            st.markdown(f"<div class='formula-box'>{legacy}</div>", unsafe_allow_html=True)
        return
    render_section_label("teach.formula_heading")
    render_teach_note(t("teach.formula_caption"))
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
    st.markdown(
        f'<div class="section-label">{escape(str(cmp_.get("title") or _plain_label("teach.use_cases")))}</div>',
        unsafe_allow_html=True,
    )
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
    render_section_label("teach.use_cases")
    render_teach_note(t("teach.use_cases_caption"))
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
        render_section_label("teach.advantages")
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
        render_section_label("teach.disadvantages")
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
        render_section_label("teach.global")
        if beginner:
            render_teach_note(t("teach.global_caption"))
        items = []
        for i, gr in enumerate(tech.get("global_research") or []):
            why = global_why[i] if (not beginner and i < len(global_why)) else ""
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
        render_section_label("teach.tt_scenarios")
        render_teach_note(t("teach.tt_caption"))
        chunks = []
        for i, tt_sc in enumerate(tech.get("tt_scenarios") or []):
            why = tt_why[i] if (not beginner and i < len(tt_why)) else ""
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
        from data.glossary import trl_scale

        render_section_label("teach.trl_assess")
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
    from data.glossary import GLOSSARY, localized_entry

    beginner = is_beginner()
    suf = "" if beginner else "_expert"
    body_key = "trl.explainer_body" if beginner else "trl.explainer_body_expert"
    trl = localized_entry("TRL") or GLOSSARY["TRL"]
    st.markdown(
        f"""<div class="glass-card">
<h4 style="color:#00E5FF;margin-top:0;">{t("trl.explainer_title")}</h4>
<p style="font-size:1rem;color:#C8D1DC;line-height:1.65;">
<strong>{escape(t("trl.explainer_lead", abbr=trl["abbr"], en=trl["en"], tr=trl["tr"], definition=trl["definition"], why=trl["why"]))}</strong>
</p>
<p style="font-size:0.96rem;color:#94A3B8;line-height:1.6;">
{escape(t(body_key))}
</p>
<ul style="font-size:0.96rem;color:#CBD5E1;padding-left:20px;line-height:1.7;">
<li><strong style="color:#00C853;">{escape(t(f"trl.explainer_ntn{suf}"))}</strong></li>
<li><strong style="color:#FFB020;">{escape(t(f"trl.explainer_ris{suf}"))}</strong></li>
<li><strong style="color:#FF5252;">{escape(t(f"trl.explainer_lab{suf}"))}</strong></li>
<li><strong style="color:#FF7043;">{escape(t(f"trl.explainer_thz{suf}"))}</strong></li>
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
