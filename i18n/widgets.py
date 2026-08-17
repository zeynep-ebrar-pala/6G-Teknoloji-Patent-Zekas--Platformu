"""Dil seçici — app.py kenar çubuğunda, ağır backend import etmez."""

from __future__ import annotations

VIEW_BEGINNER_LEGACY = "Temel Seviye (Kavramsal temel + analoji → teknik karşılık)"
VIEW_EXPERT_LEGACY = "Uzman Seviyesi (Temel katman + denklem / 3GPP / varsayım)"


def render_language_selector() -> str:
    import streamlit as st

    from i18n.core import SESSION_KEY, SUPPORTED_LANGS, bootstrap_lang, t

    lang = bootstrap_lang()
    st.markdown(
        f"<p style='color:#94A3B8;font-size:0.8rem;font-weight:600;margin-bottom:6px;'>{t('settings.language')}</p>",
        unsafe_allow_html=True,
    )
    picked = st.segmented_control(
        t("settings.language"),
        options=list(SUPPORTED_LANGS),
        format_func=lambda x: t(f"lang.{x}"),
        key=SESSION_KEY,
        help=t("settings.language_help"),
        label_visibility="collapsed",
        width="stretch",
    )
    if picked in SUPPORTED_LANGS:
        lang = picked
        if st.query_params.get("lang") != lang:
            st.query_params["lang"] = lang
    return lang


def migrate_view_mode() -> None:
    import streamlit as st

    mode = st.session_state.get("view_mode", "beginner")
    if mode in ("beginner", "expert"):
        return
    text = str(mode)
    st.session_state["view_mode"] = "expert" if "Uzman" in text or text == VIEW_EXPERT_LEGACY else "beginner"
