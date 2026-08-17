"""Hakkında — şartname teslim özeti ve sunum iskeleti."""

import streamlit as st

from i18n.core import t


def render_about_page() -> None:
    st.markdown(t("about.heading"))
    st.markdown(t("about.card"), unsafe_allow_html=True)

    st.markdown(t("about.modules"))
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(t("about.mod_left"))
    with c2:
        st.markdown(t("about.mod_right"))

    st.markdown(t("about.stack"))
    st.markdown(t("about.stack_body"))

    st.markdown(t("about.standard"))
    st.markdown(t("about.standard_body"))

    st.markdown(t("about.talk"))
    st.markdown(t("about.talk_body"))

    st.caption(t("about.usage"))
