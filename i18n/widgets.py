"""Dil seçici ve dil-sabit bölüm hapları — app.py kenar çubuğunda, ağır backend import etmez."""

from __future__ import annotations

VIEW_BEGINNER_LEGACY = "Temel Seviye (Kavramsal temel + analoji → teknik karşılık)"
VIEW_EXPERT_LEGACY = "Uzman Seviyesi (Temel katman + denklem / 3GPP / varsayım)"


def render_language_selector() -> str:
    import streamlit as st

    from i18n.core import SESSION_KEY, bootstrap_lang, t

    lang = bootstrap_lang()
    st.markdown(
        f"<p class='tt-sidebar-label'>{t('settings.language')}</p>",
        unsafe_allow_html=True,
    )
    clicked = None
    col_tr, col_en = st.columns(2)
    with col_tr:
        if st.button(
            "TR",
            key="lang_btn_tr",
            type="primary" if lang == "tr" else "secondary",
            width="stretch",
        ):
            clicked = "tr"
    with col_en:
        if st.button(
            "EN",
            key="lang_btn_en",
            type="primary" if lang == "en" else "secondary",
            width="stretch",
        ):
            clicked = "en"
    if clicked and clicked != lang:
        st.session_state[SESSION_KEY] = clicked
        st.query_params["lang"] = clicked
        st.rerun()
    return lang


def migrate_view_mode() -> None:
    import streamlit as st

    mode = st.session_state.get("view_mode", "beginner")
    if mode in ("beginner", "expert"):
        return
    text = str(mode)
    st.session_state["view_mode"] = "expert" if "Uzman" in text or text == VIEW_EXPERT_LEGACY else "beginner"
