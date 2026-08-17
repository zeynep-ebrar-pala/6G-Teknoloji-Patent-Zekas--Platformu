"""
Modül 4 — Türk Telekom 6G AI Asistanı arayüzü.
API anahtarı isteğe bağlıdır; yoksa TF-IDF yerel yanıt kullanılır.
"""

import streamlit as st

from backend.ai_assistant_service import AIAssistantService
from components.auth_view import render_auth_gate
from i18n.core import get_lang, t


def render_ai_assistant_module(view_mode: str = ""):
    if not st.session_state.get("ai_ready") and not st.session_state.get("api_key"):
        render_auth_gate()
        if not st.session_state.get("ai_ready"):
            return

    provider = st.session_state.get("ai_provider", "groq")
    api_key = st.session_state.get("api_key", "")
    mode = t("ai.mode_llm") if api_key else t("ai.mode_local")

    st.markdown(
        f"""
        <div class="glass-card" style="border-left: 6px solid #00E5FF;">
            <h2 style="margin: 0; color: #FFF; overflow-wrap:anywhere;">{t("ai.title")}</h2>
            <p style="color: #C8D1DC; font-size: 0.95rem; margin-top: 6px; overflow-wrap:anywhere;">
                {t("ai.lead", mode=mode, provider=str(provider).upper())}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(t("ai.caption"))

    c1, c2, c3 = st.columns(3)
    prompt_clicked = None
    with c1:
        if st.button(t("ai.chip_ris"), width="stretch"):
            prompt_clicked = t("ai.chip_ris")
    with c2:
        if st.button(t("ai.chip_diff"), width="stretch"):
            prompt_clicked = t("ai.chip_diff")
    with c3:
        if st.button(t("ai.chip_patents"), width="stretch"):
            prompt_clicked = t("ai.chip_patents_q")

    st.divider()

    lang = get_lang()
    welcome = t("ai.welcome")
    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = [{"role": "assistant", "content": welcome}]
        st.session_state["chat_lang"] = lang
    elif st.session_state.get("chat_lang") != lang:
        msgs = st.session_state["chat_messages"]
        if len(msgs) == 1 and msgs[0].get("role") == "assistant":
            msgs[0]["content"] = welcome
        st.session_state["chat_lang"] = lang

    for msg in st.session_state["chat_messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input(t("ai.placeholder"))
    query = user_input or prompt_clicked

    if query:
        st.session_state["chat_messages"].append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.spinner(t("ai.spinner")):
            res = AIAssistantService.answer_question(
                query,
                provider=provider,
                api_key=api_key,
                view_mode=view_mode,
            )

        st.session_state["chat_messages"].append(
            {"role": "assistant", "content": res["response"]}
        )
        with st.chat_message("assistant"):
            st.markdown(res["response"])
