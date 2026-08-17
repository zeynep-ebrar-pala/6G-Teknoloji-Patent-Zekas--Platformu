"""
Türk Telekom 6G Technology & Patent Intelligence Platform
Giriş yalnızca streamlit + i18n/styles import eder — Cloud KeyError/ImportError olmasın.
"""

import streamlit as st

st.set_page_config(
    page_title="Türk Telekom | 6G",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

from i18n.core import bootstrap_lang, t  # noqa: E402
from i18n.widgets import migrate_view_mode, render_language_selector  # noqa: E402

try:
    from styles import inject_custom_styles

    inject_custom_styles()
except Exception:
    pass

bootstrap_lang()
migrate_view_mode()

with st.sidebar:
    st.markdown(
        f"""<div style="text-align: center; padding: 12px 0;">
<div style="background: linear-gradient(135deg, #0099FF 0%, #00C2FF 100%); width: 52px; height: 52px; border-radius: 14px; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 0 20px rgba(0, 153, 255, 0.4);">
📡
</div>
<h3 style="color: #FFFFFF; margin-top: 10px; margin-bottom: 2px; overflow-wrap: anywhere;">{t("app.brand")}</h3>
<p style="color: #00E5FF; font-size: 0.82rem; font-weight: 700; letter-spacing: 0.5px; overflow-wrap: anywhere;">{t("app.product")}</p>
</div>""",
        unsafe_allow_html=True,
    )

    st.divider()
    render_language_selector()
    st.divider()

    st.markdown(
        f"<p style='color: #94A3B8; font-size: 0.8rem; font-weight: 600;'>{t('depth.label')}</p>",
        unsafe_allow_html=True,
    )
    st.radio(
        t("depth.radio"),
        ["beginner", "expert"],
        index=0,
        key="view_mode",
        format_func=lambda x: t(f"depth.{x}"),
    )

    st.divider()
    if st.session_state.get("api_key") or st.session_state.get("ai_ready"):
        if st.button(t("app.ai_logout"), width="stretch"):
            for key in ("authenticated", "api_key", "ai_provider", "ai_ready", "chat_messages", "chat_lang"):
                st.session_state.pop(key, None)
            st.rerun()

    provider_label = st.session_state.get("ai_provider") or t("ai.mode_local")
    st.markdown(
        f"""<div style="margin-top: 20px; padding: 10px; background: rgba(255,255,255,0.03); border-radius: 8px; font-size: 0.75rem; color: #64748B; overflow-wrap: anywhere;">
{t("app.ai_provider", provider=provider_label)}<br>
{t("app.footer")}
</div>""",
        unsafe_allow_html=True,
    )

st.markdown(
    f"""<div class="tt-header-container">
<span class="tt-badge">{t("app.badge")}</span>
<h1 class="tt-title">{t("app.title")}</h1>
<p class="tt-subtitle">{t("app.subtitle")}</p>
</div>""",
    unsafe_allow_html=True,
)

_nav = st.navigation(
    [
        st.Page("views/home.py", title=t("nav.home"), icon="🏠", default=True),
        st.Page("views/tech.py", title=t("nav.tech"), icon="📡"),
        st.Page("views/patent.py", title=t("nav.patent"), icon="📜"),
        st.Page("views/publications.py", title=t("nav.publications"), icon="📈"),
        st.Page("views/tt.py", title=t("nav.tt"), icon="🏢"),
        st.Page("views/ai.py", title=t("nav.ai"), icon="🤖"),
        st.Page("views/about.py", title=t("nav.about"), icon="ℹ️"),
    ],
    position="sidebar",
    expanded=True,
)
_nav.run()
