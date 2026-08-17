"""Ana Sayfa — önce kartlar, Plotly radar sonra (ilk boyama hızlı)."""

import streamlit as st

from backend.data_service import DataService
from components.content_views import is_beginner, render_trl_explainer
from components.ui_helpers import current_view_mode, first_text, show_plotly
from i18n.core import get_lang, t

TECHNOLOGIES = DataService.get_all_technologies()
beginner = is_beginner(current_view_mode())

if get_lang() == "en":
    st.markdown(
        t("home.intro_beginner") if beginner else t("home.intro_expert"),
        unsafe_allow_html=True,
    )
elif beginner:
    st.markdown(
        """<div class="dual-card-beginner" style="background:rgba(0,200,83,0.10);border:1px solid rgba(0,200,83,0.45);border-radius:14px;padding:22px;margin-bottom:20px;">
<h4 style="margin-top:0;color:#00C853;">6G nedir</h4>
<p style="color:#E2E8F0; font-size:1.02rem; line-height:1.7; margin:0 0 12px 0;">
Telefonunuz bugün bir <strong>5G</strong> kulesine tutunur: kule konuşur, cihaz dinler, bitler akar.
<strong>6G</strong> bu boruyu biraz daha kalınlaştırmak değildir. Aynı kuleye — ve kule olmayan yerlere —
yeni işler vermektir; çünkü bugünkü şebeke birkaç sahada kör kalır.
</p>
<p style="color:#E2E8F0; font-size:1.02rem; line-height:1.7; margin:0 0 12px 0;">
Şehirde yüksek frekanslı dalga köşeyi dönemez, asansör boşluğunda ölür. Hücre kenarına yaklaşınca
sinyal düşer; kule değişince kopma riski doğar. Dağ, açık deniz ve enkaz karasal kuleye yetişmez.
Sis ve gecede kule konuşur ama bakmaz. Şebeke gece-gündüz aynı ezber tarife ile kaynak ayırır.
Depodaki her etikete pil takmak ölçeklenmez. İleride kablosuz boru da dar gelir.
</p>
<p style="color:#E2E8F0; font-size:1.02rem; line-height:1.7; margin:0 0 12px 0;">
Aşağıdaki yedi kart bu yedi boşluğa birer cevap verir.
<strong>RIS</strong> kör noktayı yansıtır; <strong>hücresiz MIMO</strong> kenarı kaldırır;
<strong>NTN</strong> telefonu göğe düşürür; <strong>ISAC</strong> aynı dalgayı yankı gibi dinler;
<strong>AI-RAN</strong> kuleyi ölçüme göre ayarlar; <strong>Ambient IoT</strong> pilsiz «buradayım» der;
<strong>THz</strong> ileride daha geniş bant açar. Hepsi birden «hazır 6G» diye satılmaz;
her biri kendi <strong>TRL</strong> (Technology Readiness Level — Teknoloji Hazırlık Seviyesi)
basamağında durur.
</p>
<p style="color:#CBD5E1; font-size:0.92rem; line-height:1.65; margin:0;">
<strong>Temel</strong> kademe şunu öğretir: nedir, neden var, nasıl çalışır, ne zaman kullanılır
ve ne zaman kullanılmaz. Kısaltmalar ilk geçişte açılır. <strong>Uzman</strong> kademe aynı sahneyi
atlamaz; üstüne denklem, varsayım ve 3GPP bağlamını ekler. Uydurma tepe hız yoktur.
</p>
</div>""",
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """<div class="dual-card-expert">
<h4 style="margin-top:0;">6G yapı taşları — uzman okuma (temel katman atlanmaz)</h4>
<p style="color:#E2E8F0; font-size:0.95rem; line-height:1.65; margin:0;">
Yedi enabler: <strong>ISAC</strong> (Integrated Sensing and Communication — ortak dalga şekli),
<strong>RIS</strong> (pasif faz yüzeyi), hücresiz Massive MIMO, Sub-THz/THz,
AI-native RAN (<strong>O-RAN RIC</strong>), <strong>NTN</strong> (3GPP Rel-17+ Direct-to-Cell),
Ambient IoT. TRL 1–9 radar haritası saha olgunluğunu özetler.
Mimari, CRB/Shannon ve protokol için <strong>6G Teknolojileri</strong> sekmelerine geçin —
referans DOI/3GPP’dir; tepe hız pazarlama cümlesi saha ölçümü sayılmaz.
</p>
</div>""",
        unsafe_allow_html=True,
    )

st.markdown(t("home.cards_heading"))
st.caption(t("home.cards_caption"))

cols = st.columns(3)
for idx, (_t_id, tech) in enumerate(TECHNOLOGIES.items()):
    col = cols[idx % 3]
    with col:
        trl_class = "trl-low" if tech["trl"] <= 4 else ("trl-mid" if tech["trl"] == 5 else "trl-high")
        blurb = first_text(
            tech.get("beginner_card"),
            tech.get("card_summary"),
            tech.get("beginner_one_liner"),
        )
        kicker = first_text(tech.get("beginner_kicker"))
        kicker_html = f"<div class='card-kicker'>{kicker}</div>" if kicker else ""
        highlights_html = " ".join(
            [
                f"<span style='background: rgba(0, 153, 255, 0.12); color: #00C2FF; border: 1px solid rgba(0, 153, 255, 0.3); font-size: 0.73rem; padding: 2px 8px; border-radius: 6px; font-weight: 600; display: inline-block; margin: 2px 2px 2px 0; overflow-wrap: anywhere;'>{h}</span>"
                for h in tech.get("highlights", [])
            ]
        )
        st.markdown(
            f"""<div class="glass-card" style="min-height: 340px; display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 16px;">
<div>
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; flex-wrap: wrap; gap: 8px;">
<span style="font-size: 2.2rem;">{tech['icon']}</span>
<span class="trl-pill {trl_class}">{t("trl.pill", n=tech["trl"])}</span>
</div>
<h4 style="color: #FFFFFF; margin: 4px 0 2px 0; font-size: 1.15rem; overflow-wrap: anywhere;">{tech['acronym']}</h4>
<div style="color: #00C2FF; font-size: 0.8rem; font-weight: 600; margin-bottom: 8px; overflow-wrap: anywhere;">{tech['title']}</div>
{kicker_html}
<p style="color: #E2E8F0; font-size: 0.9rem; line-height: 1.6; margin: 0 0 12px 0; overflow-wrap: anywhere;">
{blurb}
</p>
</div>
<div>
<div style="margin-bottom: 10px;">{highlights_html}</div>
<div style="padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.76rem; color: #94A3B8; overflow-wrap: anywhere;">
{t("home.card_cta")}
</div>
</div>
</div>""",
            unsafe_allow_html=True,
        )

st.markdown(t("home.radar_heading"))
col_radar, col_info = st.columns([1.2, 1])
with col_radar:
    from components.charts import render_trl_radar_chart

    show_plotly(render_trl_radar_chart(TECHNOLOGIES))
with col_info:
    render_trl_explainer()
