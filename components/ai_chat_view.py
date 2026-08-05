"""
Türk Telekom 6G AI Assistant View Component (Module 4)
Provides an interactive natural language chat interface answering 6G research questions using AIAssistantService.
"""

import streamlit as st
from backend.ai_assistant_service import AIAssistantService

def render_ai_assistant_module():
    """Renders Module 4: AI Assistant (Chatbot & RAG) UI layout."""
    st.markdown("""
        <div class="glass-card" style="border-left: 6px solid #00E5FF;">
            <h2 style="margin: 0; color: #FFF;">🧠 Modül 4 — Türk Telekom 6G AI Asistanı</h2>
            <p style="color: #C8D1DC; font-size: 0.95rem; margin-top: 6px;">
                6G mimarisi, standartlar, patent durumları ve Türk Telekom stratejik kullanım senaryoları hakkında sorularınızı doğal dilde sorun.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Sample Quick Prompts
    st.markdown("<p style='font-size: 0.85rem; color: #94A3B8; margin-bottom: 8px;'>💡 Örnek Hızlı Sorular:</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    prompt_clicked = None
    with c1:
        if st.button("📡 RIS nedir ve Türk Telekom nerede kullanabilir?", use_container_width=True):
            prompt_clicked = "RIS nedir ve Türk Telekom nerede kullanabilir?"
    with c2:
        if st.button("⚖️ NTN ile ISAC arasındaki farklar nelerdir?", use_container_width=True):
            prompt_clicked = "NTN ile ISAC arasındaki farklar nelerdir?"
    with c3:
        if st.button("📊 6G Patent Liderliği durum analizi", use_container_width=True):
            prompt_clicked = "6G Patent Liderliği durum analizi"

    st.divider()

    # Chat Memory Session State Initialization
    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = [
            {"role": "assistant", "content": "Merhaba! Ben Türk Telekom 6G Ar-Ge AI Asistanıyım. 6G teknolojileri (ISAC, RIS, NTN, Cell-Free), patent trendleri ve Türk Telekom şebeke senaryoları hakkında bana soru sorabilirsiniz."}
        ]

    # Render Existing Chat History
    for msg in st.session_state["chat_messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat Input Box or Quick Prompt Execution
    user_input = st.chat_input("Sorunuzu buraya yazın (Örn: Ambient IoT çalışma prensibi nedir?)...")
    
    query = user_input or prompt_clicked

    if query:
        # User Message
        st.session_state["chat_messages"].append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # Generate Assistant Response
        res_data = AIAssistantService.answer_question(query)
        assistant_response = res_data["response"]

        st.session_state["chat_messages"].append({"role": "assistant", "content": assistant_response})
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
