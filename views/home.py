"""Ana Sayfa — kart metni data/home_cards.py (eski DataService katmanına bağlı değil)."""

import streamlit as st

from backend.data_service import DataService
from backend.evidence_radar import evidence_fingerprint, topic_evidence_rows
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
        card = home_card(tech_id, beginner=beginner)
        trl_class = "trl-low" if tech["trl"] <= 4 else ("trl-mid" if tech["trl"] == 5 else "trl-high")
        blurb = card.get("blurb") or ""
        kicker = card.get("kicker") or ""
        pill = t("trl.pill", n=tech["trl"]) if beginner else t("trl.pill_expert", n=tech["trl"])
        st.markdown(
            f"""<div class="glass-card home-tech-card">
<div class="home-tech-top">
<span class="home-tech-icon">{tech['icon']}</span>
<span class="trl-pill {trl_class}">{pill}</span>
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
        from components.charts import render_evidence_radar_chart

        rows = topic_evidence_rows(evidence_fingerprint())
        if rows and any(
            isinstance(r.get("patent"), int) or isinstance(r.get("pub"), int) for r in rows
        ):
            show_plotly(render_evidence_radar_chart(rows))
        else:
            st.caption(t("home.radar_empty"))
    except Exception:
        st.caption(t("home.radar_empty"))
with col_info:
    render_trl_explainer()

if beginner:
    _radar_caption = (
        "Each axis is one of the seven 6G topics. The cyan ring is Lens.org patent totals; "
        "the green ring is Springer Nature publication totals. Values are relative within each ring "
        "(100 = the strongest topic in that source). Hover shows the raw count. This is activity "
        "intensity, not TRL — readiness levels stay on the cards."
        if get_lang() == "en"
        else "Her eksen yedi 6G konusundan biridir. Camgöbeği halka Lens.org patent toplamı, "
        "yeşil halka Springer Nature yayın toplamıdır. Sayılar her halka içinde görelidir "
        "(100 = o kaynaktaki en yüksek konu). Üzerine gelince ham toplam görünür. Bu grafik "
        "etkinlik yoğunluğudur, TRL değildir — hazırlık seviyeleri kartlardaki sayılardır."
    )
else:
    _radar_caption = (
        "Dual spider: Lens patent/search topic totals vs Springer Meta API topic totals. "
        "Each series is max-normalized to 100 for a shared radial axis; hover keeps absolute totals. "
        "Corpus intensity ≠ NASA/EU TRL (card pills)."
        if get_lang() == "en"
        else "Çift halka: Lens patent/search konu total’leri × Springer Meta API konu total’leri. "
        "Her seri kendi maksimumuna göre 100’e ölçeklenir (ortak radyal eksen); hover ham total’i korur. "
        "Külliyat yoğunluğu ≠ NASA/AB TRL (kartlardaki haplar)."
    )
st.markdown(
    f'<div class="home-radar-note">{_radar_caption}</div>',
    unsafe_allow_html=True,
)
