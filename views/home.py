"""Ana Sayfa — önce kartlar, Plotly radar sonra (ilk boyama hızlı)."""

import streamlit as st

from backend.data_service import DataService
from components.content_views import is_beginner, render_trl_explainer
from components.ui_helpers import current_view_mode, first_text, show_plotly

TECHNOLOGIES = DataService.get_all_technologies()
beginner = is_beginner(current_view_mode())

if beginner:
    st.markdown(
        """<div class="dual-card-beginner">
<h4 style="margin-top:0;">6G nedir — kavramsal temel</h4>
<p style="color:#E2E8F0; font-size:1.02rem; line-height:1.7; margin:0 0 10px 0;">
Telefonunuz bugün <strong>5G</strong> ile bağlanır. <strong>6G</strong> yalnızca daha kalın bir boru değil;
kulelerin yeni işler yapmasıdır. Yedi yapı taşı yedi problemi hedefler:
kör noktayı kapatmak (RIS), hücre kenarı kopmasını bitirmek (hücresiz MIMO),
dağı ve denizi kapsamak (NTN), kuleyi radar yapmak (ISAC), şebekeyi ölçüme göre ayarlamak (AI-RAN),
pilsiz nesne izlemek (Ambient IoT) ve ileride çok geniş kablosuz bant açmak (THz).
</p>
<p style="color:#CBD5E1; font-size:0.92rem; line-height:1.6; margin:0;">
Anlatım iki kademelidir. <strong>Temel</strong>: nedir, neden var, nasıl çalışır, ne zaman kullanılır/kullanılmaz.
Kısaltmalar ilk geçişte açılır; jargonsuzlaştırılmaz. <strong>Uzman</strong> aynı temeli atlamaz;
üstüne denklem, varsayım ve 3GPP bağlamı ekler. Uydurma metrik yoktur.
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

st.markdown("### Yedi yapı taşı — her biri bir sorunu çözer")
st.caption(
    "Kartta önce sorun, sonra çözüm vardır. Kavramsal temel, formül ve Türk Telekom senaryosu için "
    "soldan «6G Teknolojileri» menüsüne geçin."
)

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
                f"<span style='background: rgba(0, 153, 255, 0.12); color: #00C2FF; border: 1px solid rgba(0, 153, 255, 0.3); font-size: 0.73rem; padding: 2px 8px; border-radius: 6px; font-weight: 600; display: inline-block; margin: 2px 2px 2px 0;'>{h}</span>"
                for h in tech.get("highlights", [])
            ]
        )
        st.markdown(
            f"""<div class="glass-card" style="min-height: 340px; display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 16px;">
<div>
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
<span style="font-size: 2.2rem;">{tech['icon']}</span>
<span class="trl-pill {trl_class}">TRL {tech['trl']}</span>
</div>
<h4 style="color: #FFFFFF; margin: 4px 0 2px 0; font-size: 1.15rem;">{tech['acronym']}</h4>
<div style="color: #00C2FF; font-size: 0.8rem; font-weight: 600; margin-bottom: 8px;">{tech['title']}</div>
{kicker_html}
<p style="color: #E2E8F0; font-size: 0.9rem; line-height: 1.6; margin: 0 0 12px 0;">
{blurb}
</p>
</div>
<div>
<div style="margin-bottom: 10px;">{highlights_html}</div>
<div style="padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.76rem; color: #94A3B8;">
Adım adım anlatım: 6G Teknolojileri → bu kartı seçin
</div>
</div>
</div>""",
            unsafe_allow_html=True,
        )

st.markdown("### 6G Teknolojileri Olgunluk Seviyesi (TRL Radar Haritası)")
col_radar, col_info = st.columns([1.2, 1])
with col_radar:
    from components.charts import render_trl_radar_chart

    show_plotly(render_trl_radar_chart(TECHNOLOGIES))
with col_info:
    render_trl_explainer()
