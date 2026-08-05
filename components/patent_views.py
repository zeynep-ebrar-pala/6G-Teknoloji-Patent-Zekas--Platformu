"""
Türk Telekom 6G Patent Intelligence View Component (Module 2)
Provides interactive analytics, patent tree visualization, top patents feed, and keyword frequency.
"""

import streamlit as st
import pandas as pd
from backend.patent_service import PatentService
from components.charts import (
    render_patent_trends_chart,
    render_company_patent_domain_chart,
    render_patent_keywords_chart,
    render_patent_network_graph
)

def render_patent_intelligence_module():
    """Renders Module 2: Patent Intelligence UI layout."""
    st.markdown("""
        <div class="glass-card" style="border-left: 6px solid #0099FF;">
            <h2 style="margin: 0; color: #FFF;">📜 Modül 2 — Patent Zekası ve Rakip Analizi</h2>
            <p style="color: #C8D1DC; font-size: 0.95rem; margin-top: 6px;">
                Küresel telekomünikasyon devlerinin (Huawei, Qualcomm, Samsung, Ericsson, Nokia, ZTE) 6G patent portföyleri, 
                teknoloji dağılımları ve stratejik lisanslama haritası.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Top KPI Metrics Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Toplam İncelemeye Alınan Patent", "18,450+", "+28% YoY")
    with col2:
        st.metric("Pazar Lideri Firma", "Huawei Technologies", "3,800 Patent")
    with col3:
        st.metric("En Çok Patent Alınan Alan", "ISAC & RIS", "%48 Pay")
    with col4:
        st.metric("Türk Telekom Hedef TRL", "TRL 4-5", "2026 PoC")

    st.divider()

    # Tabbed Patent View
    tab_trends, tab_domains, tab_network, tab_feed = st.tabs([
        "📈 Patent Sayısı / Yıl Trendi",
        "🎯 Konu Dağılımı & Radar Kıyas",
        "🌐 Patent Ağacı & Ağ Analizi",
        "📰 Öne Çıkan 6G Patentleri"
    ])

    with tab_trends:
        st.markdown("### 📊 Şirket Bazında Yıllık Patent Başvuruları")
        df_trends = PatentService.get_patent_trends_df()
        fig_trends = render_patent_trends_chart(df_trends)
        st.plotly_chart(fig_trends, use_container_width=True)

    with tab_domains:
        col_radar, col_kw = st.columns([1.2, 1])
        with col_radar:
            df_domains = PatentService.get_all_companies_domain_df()
            fig_domains = render_company_patent_domain_chart(df_domains)
            st.plotly_chart(fig_domains, use_container_width=True)

        with col_kw:
            kw_dict = PatentService.get_patent_keywords()
            fig_kw = render_patent_keywords_chart(kw_dict)
            st.plotly_chart(fig_kw, use_container_width=True)

    with tab_network:
        st.markdown("### 🕸️ Patent Atıf & Teknoloji Lisanslama Bağlantı Haritası")
        fig_net = render_patent_network_graph()
        st.plotly_chart(fig_net, use_container_width=True)

    with tab_feed:
        st.markdown("### 🔍 Yüksek Etkili 6G Patent Listesi")
        top_patents = PatentService.get_top_patents()
        
        for pat in top_patents:
            st.markdown(f"""
                <div class="glass-card" style="margin-bottom: 14px; padding: 18px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #00E5FF; font-weight: 700; font-family: 'JetBrains Mono';">{pat['id']}</span>
                        <span class="trl-pill trl-mid">{pat['domain']}</span>
                    </div>
                    <h4 style="color: #FFFFFF; margin-top: 8px; margin-bottom: 6px;">{pat['title']}</h4>
                    <p style="color: #C8D1DC; font-size: 0.88rem; margin-bottom: 8px;">{pat['abstract']}</p>
                    <div style="font-size: 0.8rem; color: #94A3B8;">
                        🏢 <strong>Atanan (Assignee):</strong> {pat['assignee']} | 
                        📅 <strong>Yıl:</strong> {pat['year']} | 
                        ⭐ <strong>Atıf Sayısı:</strong> {pat['citations']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
