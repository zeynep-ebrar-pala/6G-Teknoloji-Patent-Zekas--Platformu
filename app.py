"""
Türk Telekom 6G Technology & Patent Intelligence Platform
Giriş yalnızca streamlit + i18n.core/styles — Cloud ImportError olmasın.
Dil seçici burada sabit TR / EN. Cloud eski paket önbelleği bu dosyayı etkilemesin.
"""

import streamlit as st

st.set_page_config(
    page_title="Türk Telekom | 6G Teknoloji & Patent Zekası",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

from i18n.core import SESSION_KEY, bootstrap_lang, t  # noqa: E402

try:
    from styles import inject_custom_styles

    inject_custom_styles()
except Exception:
    pass

bootstrap_lang()
st.markdown(
    f"<style>:root {{ --tt-sidebar-footer: \"{t('app.footer')}\"; }}</style>",
    unsafe_allow_html=True,
)

_mode = st.session_state.get("view_mode", "beginner")
if _mode not in ("beginner", "expert"):
    _text = str(_mode)
    st.session_state["view_mode"] = (
        "expert" if ("Uzman" in _text or "Expert" in _text) else "beginner"
    )

with st.sidebar:
    st.markdown(
        f"""<div class="tt-sidebar-brand">
<div class="tt-sidebar-logo">📡</div>
<h3>{t("app.brand")}</h3>
<p>{t("app.product")}</p>
</div>""",
        unsafe_allow_html=True,
    )
    lang = st.session_state.get(SESSION_KEY, "tr")
    st.markdown(
        f"<p class='tt-sidebar-label'>{t('settings.language')}</p>",
        unsafe_allow_html=True,
    )
    col_tr, col_en = st.columns(2)
    with col_tr:
        if st.button(
            "TR",
            key="lang_btn_tr",
            type="primary" if lang == "tr" else "secondary",
            width="stretch",
        ):
            if lang != "tr":
                st.session_state[SESSION_KEY] = "tr"
                st.query_params["lang"] = "tr"
                st.rerun()
    with col_en:
        if st.button(
            "EN",
            key="lang_btn_en",
            type="primary" if lang == "en" else "secondary",
            width="stretch",
        ):
            if lang != "en":
                st.session_state[SESSION_KEY] = "en"
                st.query_params["lang"] = "en"
                st.rerun()

    depth = st.session_state.get("view_mode", "beginner")
    st.markdown(
        f"<p class='tt-sidebar-label'>{t('depth.label')}</p>",
        unsafe_allow_html=True,
    )
    col_b, col_e = st.columns(2)
    with col_b:
        if st.button(
            t("depth.beginner"),
            key="depth_btn_beginner",
            type="primary" if depth == "beginner" else "secondary",
            width="stretch",
        ):
            if depth != "beginner":
                st.session_state["view_mode"] = "beginner"
                st.rerun()
    with col_e:
        if st.button(
            t("depth.expert"),
            key="depth_btn_expert",
            type="primary" if depth == "expert" else "secondary",
            width="stretch",
        ):
            if depth != "expert":
                st.session_state["view_mode"] = "expert"
                st.rerun()

    if st.session_state.get("api_key") or st.session_state.get("ai_ready"):
        if st.button(t("app.ai_logout"), key="ai_logout_btn", width="stretch"):
            for key in ("authenticated", "api_key", "ai_provider", "ai_ready", "chat_messages", "chat_lang"):
                st.session_state.pop(key, None)
            st.rerun()

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
