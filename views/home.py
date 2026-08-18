"""Ana Sayfa — kart metni data/home_cards.py (eski DataService katmanına bağlı değil)."""

from html import escape

import streamlit as st

from backend.data_service import DataService
from components.content_views import is_beginner, render_trl_explainer
from components.ui_helpers import current_view_mode, show_plotly
from data.home_cards import home_card
from i18n.core import t

TECHNOLOGIES = DataService.get_all_technologies()
beginner = is_beginner(current_view_mode())

st.markdown(
    t("home.intro_beginner") if beginner else t("home.intro_expert"),
    unsafe_allow_html=True,
)

heading = t("home.cards_heading") if beginner else t("home.cards_heading_expert")
caption = t("home.cards_caption") if beginner else t("home.cards_caption_expert")
st.markdown(
    f"""<div class="home-cards-head">
<h3>{heading}</h3>
<p>{caption}</p>
</div>""",
    unsafe_allow_html=True,
)

cols = st.columns(3, gap="small")
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

st.markdown(
    f'<p class="home-radar-note">{t("home.radar_caption")}</p>',
    unsafe_allow_html=True,
)
rows = []
for tech in TECHNOLOGIES.values():
    rows.append(
        "<tr>"
        f"<td>{escape(str(tech.get('acronym') or ''))}</td>"
        f"<td>TRL {int(tech['trl'])}</td>"
        f"<td>{escape(str(tech.get('trl_desc') or ''))}</td>"
        "</tr>"
    )
st.markdown(
    f"""<table class="home-trl-table">
<thead><tr>
<th>{escape(t("home.radar_table_tech"))}</th>
<th>{escape(t("home.radar_table_trl"))}</th>
<th>{escape(t("home.radar_table_basis"))}</th>
</tr></thead>
<tbody>{''.join(rows)}</tbody>
</table>""",
    unsafe_allow_html=True,
)
