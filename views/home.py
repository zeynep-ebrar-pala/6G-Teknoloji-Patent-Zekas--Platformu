"""Ana Sayfa — kart metni data/home_cards.py (eski DataService katmanına bağlı değil)."""

import streamlit as st

from backend.data_service import DataService
from components.content_views import is_beginner, render_trl_explainer
from components.ui_helpers import current_view_mode, show_plotly
from data.home_cards import home_card
from i18n.core import get_lang, t

TECHNOLOGIES = DataService.get_all_technologies()
beginner = is_beginner(current_view_mode())

st.markdown(
    t("home.intro_beginner") if beginner else t("home.intro_expert"),
    unsafe_allow_html=True,
)
st.markdown(
    f"""<div class="glass-card" style="border-left: 5px solid #E20074; margin-bottom: 12px;">
<div class="teach-label">{t("home.tt_eu_teaser_title")}</div>
<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.6;margin:8px 0 0 0;">{t("home.tt_eu_teaser")}</p>
</div>""",
    unsafe_allow_html=True,
)

heading = t("home.cards_heading") if beginner else t("home.cards_heading_expert")
st.markdown(
    f"""<div class="home-cards-head">
<h3>{heading}</h3>
</div>""",
    unsafe_allow_html=True,
)

cols = st.columns(3, gap="large")
for idx, (tech_id, tech) in enumerate(TECHNOLOGIES.items()):
    col = cols[idx % 3]
    with col:
        card = home_card(tech_id)
        trl_class = "trl-low" if tech["trl"] <= 4 else ("trl-mid" if tech["trl"] == 5 else "trl-high")
        blurb = card.get("blurb") or ""
        kicker = card.get("kicker") or ""
        st.markdown(
            f"""<div class="glass-card home-tech-card">
<div class="home-tech-top">
<span class="home-tech-icon">{tech['icon']}</span>
<span class="trl-pill {trl_class}">{t("trl.pill", n=tech["trl"])}</span>
</div>
<h4 class="home-tech-acronym">{tech['acronym']}</h4>
<div class="home-tech-title">{tech['title']}</div>
<div class="card-kicker">{kicker}</div>
<p class="home-tech-blurb">{blurb}</p>
</div>""",
            unsafe_allow_html=True,
        )

st.markdown(t("home.radar_heading"))
col_radar, col_info = st.columns([1.2, 1])
with col_radar:
    try:
        from components.charts import render_trl_radar_chart

        show_plotly(render_trl_radar_chart(TECHNOLOGIES))
    except Exception:
        pass
with col_info:
    render_trl_explainer()

_radar_caption = (
    "Slices use the NASA/EU TRL 1–9 scale; each integer is mapped from a 3GPP technical report or a public trial class."
    if get_lang() == "en"
    else "Dilimler NASA/AB TRL 1–9 ölçeğidir; her tam sayı, 3GPP teknik raporu veya kamuya açık deneme sınıfına göre eşlenir."
)
st.markdown(
    f'<div class="home-radar-note">{_radar_caption}</div>',
    unsafe_allow_html=True,
)
