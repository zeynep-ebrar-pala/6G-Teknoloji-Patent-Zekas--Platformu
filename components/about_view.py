"""Hakkında — şartname teslim özeti ve sunum iskeleti."""

import streamlit as st


def render_about_page() -> None:
    st.markdown("### Hakkında")
    st.markdown(
        """<div class="glass-card" style="border-left: 5px solid #00E5FF;">
<h4 style="color:#00E5FF; margin-top:0;">6G Technology &amp; Patent Intelligence Platform</h4>
<p style="color:#E2E8F0; font-size:0.95rem; line-height:1.6; margin-bottom:0;">
Türk Telekom 6G Ar-Ge ekibinde kullanılmak üzere 6G teknolojileri, akademik yayınlar
ve patent trendlerini tek portalda sunan Streamlit uygulaması.
Geliştirici: <strong>Zeynep Ebrar Pala</strong>.
</p>
</div>""",
        unsafe_allow_html=True,
    )

    st.markdown("#### Modüller")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
- **Ana Sayfa** — 7 teknolojinin TRL radar haritası
- **6G Teknolojileri** — tanım, prensip, mimari, kullanım, avantaj/dezavantaj, dünya çalışmaları, TT senaryoları, TRL, blok diyagram
- **Patent Zekası** — Nokia, Ericsson, Huawei, Samsung, Qualcomm; yıl, konu, kelime bulutu, ağaç, yoğunluk, harita
- **Yayın Trendleri** — OpenAlex yıl / kurum / ülke; DOI doğrulamalı makaleler
            """
        )
    with c2:
        st.markdown(
            """
- **Türk Telekom Görünümü** — saha senaryo çözümleyici
- **AI Asistan** — TF-IDF yerel geri getirme; isteğe bağlı Groq / Gemini
- **Hakkında** — bu sayfa (teslim / 15 dk sunum iskeleti)
            """
        )

    st.markdown("#### Kullanılan teknolojiler")
    st.markdown(
        "Python, Streamlit, Pandas, Plotly, Matplotlib, NetworkX, WordCloud, scikit-learn. "
        "Opsiyonel: Groq API, Google Gemini API. Patent kaynağı: Google Patents. "
        "Akademik: OpenAlex + DOI (IEEE Xplore, Springer, Elsevier)."
    )

    st.markdown("#### 15 dakikalık sunum iskeleti")
    st.markdown(
        """
1. Amaç ve kapsam (1 dk)
2. Ana Sayfa TRL radar (2 dk)
3. Bir teknoloji (ör. RIS) — prensip + diyagram + TT senaryosu (3 dk)
4. Patent Zekası — firma filtresi, yıl grafiği, kelime bulutu (3 dk)
5. Yayın Trendleri — OpenAlex yıl + kurum/ülke + DOI kartı (3 dk)
6. AI Asistan — «RIS nedir?» ve «NTN ile ISAC arasındaki fark» (2 dk)
7. Kaynak doğrulama kuralı: uydurma ID/sayı yok (1 dk)
        """
    )

    st.caption("Kullanım adımları için depodaki USAGE_GUIDE.md dosyasına bakın.")
