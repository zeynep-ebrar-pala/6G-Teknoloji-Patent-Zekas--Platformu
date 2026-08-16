"""
Modül 2 — Patent Zekası ve Rakip Analizi arayüzü.
Tüm patent kayıtları Google Patents üzerinden doğrulanabilir.
"""

import streamlit as st

from backend.patent_service import PatentService
from components.charts import (
    render_company_counts_chart,
    render_company_patent_domain_chart,
    render_patent_density_heatmap,
    render_patent_keywords_chart,
    render_patent_network_graph,
    render_patent_sunburst,
    render_patent_tfidf_map,
    render_patent_trends_chart,
    render_patent_wordcloud,
)
from components.ui_helpers import render_module_header, render_patent_card, render_source_button, show_empty


def render_patent_intelligence_module():
    spec = PatentService.get_spec_companies()
    filter_options = ["Tümü"] + spec
    company = st.selectbox(
        "Firma (şartname listesi: Nokia, Ericsson, Huawei, Samsung, Qualcomm):",
        options=filter_options,
        index=0,
    )
    company_arg = None if company == "Tümü" else company

    summary = PatentService.get_summary(company_arg)
    patents = PatentService.get_top_patents(company_arg)

    render_module_header(
        "Patent Zekası",
        "Küresel telekom firmalarının 6G patent kayıtları — tüm kayıtlar "
        "Google Patents üzerinden doğrulanabilir. Bu küme tam portföy değildir; "
        f"yalnızca doğrulanmış örnek kayıtlardır. Kaynak: {summary['source']}",
    )

    st.markdown(
        """<div class="glass-card">
<div class="teach-label">Bu sayfa ne işe yarar?</div>
<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>Patent</strong>, bir buluşun kamuya açıklanması karşılığında sınırlı süre tekel hakkıdır.
Burada baktığımız şey hukuki tavsiye değil; hangi firmanın hangi 6G konusunda koruma talebinde
bulunduğunun <em>örnek</em> haritasıdır. <strong>Assignee</strong> (hak sahibi) kaydı kimin
başvurduğunu söyler; o firmanın sahada ürünü olduğu anlamına gelmez.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
<strong>TF-IDF (Term Frequency–Inverse Document Frequency — terim sıklığı–ters belge sıklığı):</strong>
özet metindeki sözcükleri, derlemede ne kadar ayırt edici olduklarına göre puanlar.
Harita anlam çıkarmaz; hangi kaydın hangi sözcüklere yakın durduğunu gösterir.
Özetler kaynakta kilitlidir — yeniden yazılmaz, uydurulmaz.
</p>
<p style="color:#94A3B8;font-size:0.84rem;margin:10px 0 0 0;">
Ne zaman yorumlanmaz: tek patent = pazar liderliği değildir. Yıl çubuğu başvuru/yayın yılıdır,
ticarileşme tarihi değildir.
</p>
</div>""",
        unsafe_allow_html=True,
    )

    if not patents:
        show_empty(
            f"«{company}» için doğrulanmış patent kaydı yok. "
            "Sayı uydurulmaz; Google Patents’te teyitli kayıt eklenene kadar grafik gizlenir."
        )
        return

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Doğrulanmış Patent Kaydı", str(summary["total"]))
    with col2:
        st.metric("En Fazla Kayıt (Assignee)", summary["leader_company"], f"{summary['leader_count']} patent")
    with col3:
        st.metric("Öne Çıkan Teknoloji Alanı", summary["top_domain"], f"{summary['top_domain_count']} kayıt")
    with col4:
        st.metric("Kaynak", "Google Patents")
    render_source_button("https://patents.google.com", "Google Patents ana sayfasını aç ↗")

    st.divider()

    tab_trends, tab_topics, tab_tree, tab_map, tab_feed = st.tabs([
        "Patent Sayısı / Yıl",
        "Konu Dağılımı & Kelime Bulutu",
        "Patent Ağacı & Yoğunluk",
        "Teknoloji Haritası & Ağ",
        "Patent Başlıkları",
    ])

    with tab_trends:
        st.markdown("### Yıllara Göre Dağılım")
        st.caption(
            "Her çubuk bir takvim yılıdır (ör. 2024, 2025). "
            "Kayıtlarda ay bilgisi olmadığı için 2024.2 gibi ara değer veya uydurma «2. Ay» dilimi yok."
        )
        df_trends = PatentService.get_patent_trends_df(company_arg)
        if df_trends.empty:
            show_empty("Trend grafiği için yeterli patent verisi yok.")
        else:
            fig_trends = render_patent_trends_chart(df_trends)
            st.plotly_chart(fig_trends, use_container_width=True)

        st.markdown("### En Çok Kayıtlı Firmalar")
        counts = PatentService.get_company_counts(company_arg)
        if not counts:
            show_empty("Firma sayımı için veri yok.")
        else:
            st.plotly_chart(render_company_counts_chart(counts), use_container_width=True)

    with tab_topics:
        col_radar, col_kw = st.columns([1.2, 1])
        with col_radar:
            df_domains = PatentService.get_all_companies_domain_df(company_arg)
            if df_domains.empty:
                show_empty("Domain dağılımı hesaplanamadı.")
            else:
                fig_domains = render_company_patent_domain_chart(df_domains)
                st.plotly_chart(fig_domains, use_container_width=True)

        with col_kw:
            kw_dict = PatentService.get_patent_keywords(company_arg)
            if not kw_dict:
                show_empty("Anahtar kelime analizi için veri yok.")
            else:
                fig_kw = render_patent_keywords_chart(kw_dict)
                st.plotly_chart(fig_kw, use_container_width=True)

        st.markdown("### Kelime Bulutu")
        st.caption("Yalnızca doğrulanmış patent başlıklarındaki kelime sıklığı.")
        kw_dict = PatentService.get_patent_keywords(company_arg)
        wc_fig = render_patent_wordcloud(kw_dict) if kw_dict else None
        if wc_fig is None:
            show_empty("Kelime bulutu için wordcloud/matplotlib yüklü değil veya kelime yok.")
        else:
            st.pyplot(wc_fig, clear_figure=True)

    with tab_tree:
        st.markdown("### Patent Yoğunluk Grafiği")
        df_density = PatentService.get_density_df(company_arg)
        if df_density.empty:
            show_empty("Yoğunluk haritası için veri yok.")
        else:
            st.plotly_chart(render_patent_density_heatmap(df_density), use_container_width=True)

        st.markdown("### Patent Ağacı")
        df_tree = PatentService.get_sunburst_df(company_arg)
        if df_tree.empty:
            show_empty("Ağaç grafiği için veri yok.")
        else:
            st.plotly_chart(render_patent_sunburst(df_tree), use_container_width=True)

    with tab_map:
        st.markdown("### Patent Teknoloji Haritası")
        st.caption("Koordinatlar patent başlıklarının TF-IDF vektörlerinin PCA ile 2 boyuta indirgenmesidir; uydurma konum yoktur.")
        df_map = PatentService.get_tfidf_map_df(company_arg)
        if df_map.empty:
            show_empty("Harita için en az 2 patent ve scikit-learn gerekir.")
        else:
            st.plotly_chart(render_patent_tfidf_map(df_map), use_container_width=True)

        st.markdown("### Assignee ↔ Alan Ağ Analizi")
        edges = PatentService.get_network_edges(company_arg)
        if not edges:
            show_empty("Ağ grafiği için bağlantı verisi yok.")
        else:
            fig_net = render_patent_network_graph(edges)
            st.plotly_chart(fig_net, use_container_width=True)

    with tab_feed:
        st.markdown("### Doğrulanmış 6G Patent Listesi")
        st.caption("Her kartta publication number, başlık, assignee, yıl ve Google Patents kaynak bağlantısı bulunur.")
        for pat in patents:
            render_patent_card(pat)
