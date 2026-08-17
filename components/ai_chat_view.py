"""
Modül 4 — Türk Telekom 6G AI Asistanı arayüzü.
API anahtarı isteğe bağlıdır; yoksa TF-IDF yerel yanıt kullanılır.
"""

import streamlit as st

from backend.ai_assistant_service import AIAssistantService
from components.auth_view import render_auth_gate


def render_ai_assistant_module(view_mode: str = ""):
    if not st.session_state.get("ai_ready") and not st.session_state.get("api_key"):
        render_auth_gate()
        if not st.session_state.get("ai_ready"):
            return

    provider = st.session_state.get("ai_provider", "groq")
    api_key = st.session_state.get("api_key", "")
    mode = "LLM + TF-IDF" if api_key else "yalnızca TF-IDF (yerel)"

    st.markdown(
        f"""
        <div class="glass-card" style="border-left: 6px solid #00E5FF;">
            <h2 style="margin: 0; color: #FFF;">AI Asistan</h2>
            <p style="color: #C8D1DC; font-size: 0.95rem; margin-top: 6px;">
                Yanıtlar sklearn TF-IDF ile seçilen teknoloji, patent, makale ve sözlük kayıtlarındandır.
                Dual-Depth kenar çubuğu anlatım kademesini belirler (Temel: zihinsel model; Uzman: denklem + varsayım).
                Mod: <strong style="color:#00E5FF;">{mode}</strong>
                · Sağlayıcı: <strong style="color:#00E5FF;">{provider.upper()}</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption("Bağlamda olmayan patent numarası, DOI veya atıf sayısı üretilmez.")

    c1, c2, c3 = st.columns(3)
    prompt_clicked = None
    with c1:
        if st.button("RIS nedir?", width="stretch"):
            prompt_clicked = "RIS nedir?"
    with c2:
        if st.button("NTN ile ISAC arasındaki fark", width="stretch"):
            prompt_clicked = "NTN ile ISAC arasındaki fark"
    with c3:
        if st.button("Patent veri özeti", width="stretch"):
            prompt_clicked = "Platformdaki doğrulanmış patent verilerini özetle."

    st.divider()

    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = [
            {
                "role": "assistant",
                "content": (
                    "Merhaba! Ben Türk Telekom 6G AI Asistanıyım. "
                    "Yanıtlarım Modül 1–3'teki doğrulanmış kayıtlara dayanır; "
                    "platformda olmayan bilgi uydurmam."
                ),
            }
        ]

    for msg in st.session_state["chat_messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("6G teknolojisi, patent veya makale hakkında sorun...")
    query = user_input or prompt_clicked

    if query:
        st.session_state["chat_messages"].append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.spinner("Doğrulanmış kayıtlar üzerinden yanıt üretiliyor..."):
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
