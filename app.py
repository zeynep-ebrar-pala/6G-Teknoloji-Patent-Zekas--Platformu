"""
Türk Telekom 6G Technology & Patent Intelligence Platform
Giriş yalnızca streamlit import eder — Cloud KeyError/ImportError olmasın.
"""

import streamlit as st

st.set_page_config(
    page_title="Türk Telekom | 6G Teknoloji & Patent Zekası",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

VIEW_BEGINNER = "Temel Seviye (Kavramsal temel + analoji → teknik karşılık)"
VIEW_EXPERT = "Uzman Seviyesi (Temel katman + denklem / 3GPP / varsayım)"

try:
    from styles import inject_custom_styles

    inject_custom_styles()
except Exception:
    pass

with st.sidebar:
    st.markdown(
        """<div style="text-align: center; padding: 12px 0;">
<div style="background: linear-gradient(135deg, #0099FF 0%, #00C2FF 100%); width: 52px; height: 52px; border-radius: 14px; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 0 20px rgba(0, 153, 255, 0.4);">
📡
</div>
<h3 style="color: #FFFFFF; margin-top: 10px; margin-bottom: 2px;">Türk Telekom</h3>
<p style="color: #00E5FF; font-size: 0.82rem; font-weight: 700; letter-spacing: 0.5px;">6G Ar-Ge Platformu</p>
</div>""",
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown(
        "<p style='color: #94A3B8; font-size: 0.8rem; font-weight: 600;'>Anlatım Derinliği (Dual-Depth):</p>",
        unsafe_allow_html=True,
    )
    st.radio(
        "Derinlik Seviyesi:",
        [VIEW_BEGINNER, VIEW_EXPERT],
        index=0,
        key="view_mode",
    )

    st.divider()
    if st.session_state.get("api_key") or st.session_state.get("ai_ready"):
        if st.button("AI oturumunu kapat", width="stretch"):
            for key in ("authenticated", "api_key", "ai_provider", "ai_ready", "chat_messages"):
                st.session_state.pop(key, None)
            st.rerun()

    provider_label = st.session_state.get("ai_provider", "kapalı")
    st.markdown(
        f"""<div style="margin-top: 20px; padding: 10px; background: rgba(255,255,255,0.03); border-radius: 8px; font-size: 0.75rem; color: #64748B;">
AI sağlayıcı: {provider_label}<br>
© 2026 Türk Telekom Ar-Ge
</div>""",
        unsafe_allow_html=True,
    )

st.markdown(
    """<div class="tt-header-container">
<span class="tt-badge">Türk Telekom 6G Ar-Ge Platformu</span>
<h1 class="tt-title">Türk Telekom 6G Teknoloji &amp; Patent Zekası Platformu</h1>
<p class="tt-subtitle">6G Teknolojileri, Patent Zekası ve Yayın Analitiği</p>
</div>""",
    unsafe_allow_html=True,
)

_nav = st.navigation(
    [
        st.Page("views/home.py", title="Ana Sayfa", icon="🏠", default=True),
        st.Page("views/tech.py", title="6G Teknolojileri", icon="📡"),
        st.Page("views/patent.py", title="Patent Zekası", icon="📜"),
        st.Page("views/publications.py", title="Yayın Trendleri", icon="📈"),
        st.Page("views/tt.py", title="Türk Telekom Görünümü", icon="🏢"),
        st.Page("views/ai.py", title="AI Asistan", icon="🤖"),
        st.Page("views/about.py", title="Hakkında", icon="ℹ️"),
    ],
    position="sidebar",
    expanded=True,
)
_nav.run()
