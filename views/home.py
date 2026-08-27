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

rows = []
try:
    from components.charts import render_evidence_radar_pair

    rows = topic_evidence_rows(evidence_fingerprint())
    if rows and any(
        isinstance(r.get("patent"), int) or isinstance(r.get("pub"), int) for r in rows
    ):
        pat_fig, pub_fig = render_evidence_radar_pair(rows)
        c1, c2 = st.columns(2)
        with c1:
            show_plotly(pat_fig)
        with c2:
            show_plotly(pub_fig)
    else:
        st.caption(t("home.radar_empty"))
except Exception as exc:
    st.error(f"{t('home.radar_empty')} ({type(exc).__name__}: {exc})")

# Ham toplamlar — Plotly başarısız olsa bile görünür
_th_topic = t("home.radar_table_topic")
_th_pat = t("home.radar_table_patent")
_th_pub = t("home.radar_table_pub")
_cells = []
for r in rows or []:
    domain = str(r.get("domain") or "—")
    pat = f"{int(r['patent']):,}" if isinstance(r.get("patent"), int) else "—"
    pub = f"{int(r['pub']):,}" if isinstance(r.get("pub"), int) else "—"
    _cells.append(f"<tr><td>{domain}</td><td style='text-align:right'>{pat}</td><td style='text-align:right'>{pub}</td></tr>")
if _cells:
    st.markdown(
        f"""<div class="home-radar-table-wrap" style="margin:0.6rem 0 1rem;overflow-x:auto">
<table class="home-radar-table" style="width:100%;max-width:640px;border-collapse:collapse;font-size:0.85rem;color:#C8D1DC">
<thead><tr>
<th style="text-align:left;padding:4px 8px;border-bottom:1px solid rgba(200,209,220,0.25)">{_th_topic}</th>
<th style="text-align:right;padding:4px 8px;border-bottom:1px solid rgba(200,209,220,0.25)">{_th_pat}</th>
<th style="text-align:right;padding:4px 8px;border-bottom:1px solid rgba(200,209,220,0.25)">{_th_pub}</th>
</tr></thead>
<tbody>{''.join(_cells)}</tbody>
</table></div>""",
        unsafe_allow_html=True,
    )

render_trl_explainer()

if beginner:
    _radar_caption = (
        "Each spider matches one table column. Rings and vertex labels are absolute Lens/Springer "
        "totals — the same numbers as the table. Cyan = Lens patents, green = Springer publications. "
        "This is activity intensity, not TRL — readiness levels stay on the cards."
        if get_lang() == "en"
        else "Her örümcek bir tablo sütununa aittir. Halkalar ve köşe etiketleri mutlak Lens/Springer "
        "toplamlarıdır — tablodaki sayılarla aynıdır. Camgöbeği = Lens patent, yeşil = Springer yayın. "
        "Bu grafik etkinlik yoğunluğudur, TRL değildir — hazırlık seviyeleri kartlardaki sayılardır."
    )
else:
    _radar_caption = (
        "Two spiders: Lens patent topic totals and Springer Meta topic totals. "
        "Radial axis = absolute totals matching the table (not percent). "
        "Corpus intensity ≠ NASA/EU TRL (card pills)."
        if get_lang() == "en"
        else "İki örümcek: Lens patent konu total’leri ve Springer Meta konu total’leri. "
        "Radyal eksen = tablodaki mutlak toplamlar (yüzde değil). "
        "Külliyat yoğunluğu ≠ NASA/AB TRL (kartlardaki haplar)."
    )
st.markdown(
    f'<div class="home-radar-note">{_radar_caption}</div>',
    unsafe_allow_html=True,
)
