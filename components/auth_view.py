"""Kurumsal AI asistan anahtar doğrulaması — uygulamayı kilitlemez."""

from __future__ import annotations

import streamlit as st

from backend.auth_service import Provider, resolve_stored_key, validate_api_key


def render_auth_gate() -> None:
    """Yalnızca AI Asistan için Groq / Gemini anahtarı ister."""
    st.markdown(
        """<div class="glass-card" style="border-left: 6px solid #00E5FF; margin-bottom: 16px;">
<h3 style="color:#FFFFFF; margin-top:0;">AI Asistan için API anahtarı</h3>
<p style="color:#C8D1DC; font-size:0.92rem; margin-bottom:0;">
Anahtar yalnızca bu oturumda tutulur. Modül 1–3 ve Türk Telekom görünümü anahtarsız çalışır.
</p>
</div>""",
        unsafe_allow_html=True,
    )

    col_a, col_b, col_c = st.columns([1, 1.6, 1])
    with col_b:
        provider_label = st.radio(
            "AI Sağlayıcı Seçimi:",
            ["Groq (gsk_...)", "Google Gemini (AIza...)"],
            horizontal=True,
            key="ai_auth_provider_radio",
        )
        provider: Provider = "gemini" if "Gemini" in provider_label else "groq"

        placeholder = "gsk_..." if provider == "groq" else "AIza..."
        api_key_input = st.text_input(
            "API Anahtarı:",
            type="password",
            placeholder=placeholder,
            key="auth_api_key_input",
        )

        st.caption(
            "Anahtar almak için: "
            "[Groq Console](https://console.groq.com/keys) · "
            "[Google AI Studio](https://aistudio.google.com/apikey)"
        )

        env_key = resolve_stored_key(provider)
        if env_key:
            st.info(
                f"`.env` dosyasında `{provider.upper()}_API_KEY` tanımlı. "
                "Aşağıdaki butonla ortam anahtarını kullanabilirsiniz."
            )
            if st.button("`.env` anahtarı ile AI'yı aç", use_container_width=True):
                ok, msg = validate_api_key(provider, env_key)
                if ok:
                    _set_session(provider, env_key)
                    st.rerun()
                else:
                    st.error(msg)

        if st.button("AI Asistanı aç", use_container_width=True, type="primary"):
            key = api_key_input.strip()
            if not key:
                st.error("Lütfen geçerli bir API anahtarı girin.")
                return
            with st.spinner("API anahtarı doğrulanıyor..."):
                ok, msg = validate_api_key(provider, key)
            if ok:
                _set_session(provider, key)
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)

        st.caption("Anahtar yoksa asistan yine de TF-IDF ile doğrulanmış kayıtlardan kısa yanıt üretir.")
        if st.button("Anahtarsız devam et (yalnızca yerel geri getirme)", use_container_width=True):
            st.session_state["ai_ready"] = True
            st.session_state["ai_provider"] = provider
            st.session_state["api_key"] = ""
            st.rerun()


def _set_session(provider: Provider, api_key: str) -> None:
    st.session_state["authenticated"] = True
    st.session_state["ai_ready"] = True
    st.session_state["ai_provider"] = provider
    st.session_state["api_key"] = api_key
