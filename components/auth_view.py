"""Kurumsal AI asistan anahtar doğrulaması — uygulamayı kilitlemez."""

from __future__ import annotations

import streamlit as st

from backend.auth_service import Provider, resolve_stored_key, validate_api_key
from i18n.core import t


def render_auth_gate() -> None:
    """Yalnızca AI Asistan için Groq / Gemini anahtarı ister."""
    st.markdown(
        f"""<div class="glass-card" style="border-left: 6px solid #00E5FF; margin-bottom: 16px;">
<h3 style="color:#FFFFFF; margin-top:0; overflow-wrap:anywhere;">{t("auth.title")}</h3>
<p style="color:#C8D1DC; font-size:0.92rem; margin-bottom:0;">
{t("auth.lead")}
</p>
</div>""",
        unsafe_allow_html=True,
    )

    col_a, col_b, col_c = st.columns([1, 1.6, 1])
    with col_b:
        provider_label = st.radio(
            t("auth.provider"),
            ["groq", "gemini"],
            format_func=lambda x: t("auth.groq") if x == "groq" else t("auth.gemini"),
            horizontal=True,
            key="ai_auth_provider_radio",
        )
        provider: Provider = "gemini" if provider_label == "gemini" else "groq"

        placeholder = "gsk_..." if provider == "groq" else "AIza..."
        api_key_input = st.text_input(
            t("auth.key"),
            type="password",
            placeholder=placeholder,
            key="auth_api_key_input",
        )

        st.caption(t("auth.keys_help"))

        env_key = resolve_stored_key(provider)
        if env_key:
            st.info(t("auth.env_info", provider=provider.upper()))
            if st.button(t("auth.open_env"), width="stretch"):
                ok, msg = validate_api_key(provider, env_key)
                if ok:
                    _set_session(provider, env_key)
                    st.rerun()
                else:
                    st.error(msg)

        if st.button(t("auth.open"), width="stretch", type="primary"):
            key = api_key_input.strip()
            if not key:
                st.error(t("auth.empty_key"))
                return
            with st.spinner(t("auth.spinner")):
                ok, msg = validate_api_key(provider, key)
            if ok:
                _set_session(provider, key)
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)

        st.caption(t("auth.no_key_caption"))
        if st.button(t("auth.continue"), width="stretch"):
            st.session_state["ai_ready"] = True
            st.session_state["ai_provider"] = provider
            st.session_state["api_key"] = ""
            st.rerun()


def _set_session(provider: Provider, api_key: str) -> None:
    st.session_state["authenticated"] = True
    st.session_state["ai_ready"] = True
    st.session_state["ai_provider"] = provider
    st.session_state["api_key"] = api_key
