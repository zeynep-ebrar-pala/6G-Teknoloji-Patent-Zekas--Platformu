"""Konu taraması — ui_helpers döngüsünden ayrı (Python 3.14 from-import)."""

from __future__ import annotations

from typing import Optional, Tuple

import streamlit as st


def render_patent_topic_panel(key_suffix: str = "pat") -> Optional[str]:
    """Konu seçimi kilitli patent kümesini, ofis çubuklarını ve ofis aramasını birlikte değiştirir."""
    from backend.patent_service import PatentService
    from backend.source_links import SPEC_PUB_TOPICS, topic_patent_searches
    from backend.tt_europe_service import TTEuropeService
    from components.ui_helpers import render_link_row, render_source_totals
    from i18n.core import format_int, get_lang, t

    st.markdown(t("sources.topic_pat_heading"))
    st.caption(t("sources.topic_pat_caption"))
    options = ["all"] + list(SPEC_PUB_TOPICS.keys())
    topic = st.selectbox(
        t("sources.topic_search"),
        options,
        format_func=lambda x: t("sources.topic_all") if x == "all" else x,
        key=f"spec_pat_topic_{key_suffix}_{get_lang()}",
    )
    picked = None if topic == "all" else topic
    n = PatentService.get_summary(None, picked)["total"]
    offices = TTEuropeService.office_counts(picked)
    live_kwargs = {
        "n": format_int(n),
        "ep": format_int(offices.get("EP") or 0),
        "us": format_int(offices.get("US") or 0),
        "tr": format_int(offices.get("TR") or 0),
    }
    if picked is None:
        st.info(t("sources.topic_live_all", **live_kwargs))
        st.caption(t("sources.topic_buttons_hint"))
        render_link_row(topic_patent_searches("6G"), key_suffix=f"{key_suffix}_all")
        render_source_totals("patent", None, f"{key_suffix}_all")
        return None
    st.info(
        t(
            "sources.topic_live_one",
            topic=picked,
            q=SPEC_PUB_TOPICS[picked],
            **live_kwargs,
        )
    )
    st.caption(t("sources.topic_buttons_hint"))
    render_link_row(topic_patent_searches(picked), key_suffix=f"{key_suffix}_{picked}")
    render_source_totals("patent", picked, f"{key_suffix}_{picked}")
    return picked


def render_pub_topic_panel(key_suffix: str = "pub") -> Tuple[Optional[str], str]:
    """Konu + bölge: Türkiye / Avrupa 6G yayın taraması. Kilitli örnek yok."""
    from backend.academic_service import AcademicService
    from backend.source_links import SPEC_PUB_TOPICS, topic_pub_searches
    from components.ui_helpers import render_link_row, render_source_totals
    from i18n.core import format_int, get_lang, t

    st.markdown(t("sources.topic_pub_heading"))
    st.caption(t("sources.topic_pub_caption"))
    region_labels = {
        t("pub.region.both"): "both",
        t("pub.region.tr"): "tr",
        t("pub.region.eu"): "eu",
    }
    region_ui = st.radio(
        t("pub.region_label"),
        list(region_labels.keys()),
        horizontal=True,
        key=f"spec_pub_region_{key_suffix}_{get_lang()}",
    )
    region = region_labels.get(region_ui, "both")
    options = ["all"] + list(SPEC_PUB_TOPICS.keys())
    topic = st.selectbox(
        t("sources.topic_search"),
        options,
        format_func=lambda x: t("sources.topic_all") if x == "all" else x,
        key=f"spec_pub_topic_{key_suffix}_{get_lang()}",
    )
    picked = None if topic == "all" else topic
    bundle = AcademicService.get_bundle(region, picked)
    tr_n = bundle.get("total_tr")
    tr = format_int(tr_n) if isinstance(tr_n, int) else "—"
    wos_n = bundle.get("wos_total")
    if picked is None:
        st.info(t("sources.topic_live_all_pub", n=tr))
    else:
        n = format_int(wos_n) if isinstance(wos_n, int) else "—"
        st.info(
            t(
                "sources.topic_live_one_pub",
                n=n,
                tr=tr,
                topic=picked,
                q=bundle.get("wos_query") or SPEC_PUB_TOPICS[picked],
            )
        )
    st.caption(t("sources.topic_buttons_hint_pub"))
    render_link_row(topic_pub_searches(picked or "6G", region), key_suffix=f"{key_suffix}_{picked or 'all'}_{region}")
    render_source_totals("pub", picked, f"{key_suffix}_{picked or 'all'}")
    return picked, region
