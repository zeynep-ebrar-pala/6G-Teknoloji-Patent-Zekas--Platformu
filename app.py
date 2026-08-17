"""
Türk Telekom 6G Technology & Patent Intelligence Platform
Giriş yalnızca streamlit + i18n/styles import eder — Cloud KeyError/ImportError olmasın.
"""

import streamlit as st

st.set_page_config(
    page_title="Türk Telekom | 6G Teknoloji & Patent Zekası",
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
        f"""<div class="tt-sidebar-brand">
<div class="tt-sidebar-logo">📡</div>
<h3>{t("app.brand")}</h3>
<p>{t("app.product")}</p>
</div>""",
        unsafe_allow_html=True,
    )
    render_language_selector()
    st.markdown(
        f"<p class='tt-sidebar-label'>{t('depth.label')}</p>",
        unsafe_allow_html=True,
    )
    st.radio(
        t("depth.radio"),
        ["beginner", "expert"],
        index=0,
        key="view_mode",
        format_func=lambda x: t(f"depth.{x}"),
        label_visibility="collapsed",
    )

    if st.session_state.get("api_key") or st.session_state.get("ai_ready"):
        if st.button(t("app.ai_logout"), width="stretch"):
            for key in ("authenticated", "api_key", "ai_provider", "ai_ready", "chat_messages", "chat_lang"):
                st.session_state.pop(key, None)
            st.rerun()

    st.markdown(
        f"""<div class="tt-sidebar-foot">
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
