"""
Türk Telekom 6G Academic Publication Views Component (Module 3)
Provides UI analytics for academic literature trends, index databases, research institutes, and top cited papers.
"""

import streamlit as st
import pandas as pd
from backend.academic_service import AcademicService
from components.charts import (
    render_academic_trends_chart,
    render_academic_database_chart
)

def render_academic_publication_module():
    """Renders Module 3: Academic Publication Trends UI layout."""
    st.markdown("""
        <div class="glass-card" style="border-left: 6px solid #00C2FF;">
            <h2 style="margin: 0; color: #FFF;">📚 Modül 3 — Akademik Yayın Analizi</h2>
            <p style="color: #C8D1DC; font-size: 0.95rem; margin-top: 6px;">
                IEEE Xplore, Google Scholar, Springer ve Elsevier veritabanlarında 6G konularındaki bilimsel makale sayıları, 
                kurumsal araştırmalar ve atıf liderleri.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Top KPI Metrics
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Toplam Akademik Yayın", "32,800+", "2020-2026")
    with c2:
        st.metric("En Çok Makale Basılan Konu", "RIS & ISAC", "14,300 Makale")
    with c3:
        st.metric("Lider Veritabanı", "IEEE Xplore", "%45 Pay")
    with c4:
        st.metric("En Çok Atıf Alan Makale", "2,350 Atıf", "IEEE Wireless Comm")

    st.divider()

    tab_pub_trends, tab_sources, tab_institutions, tab_cited = st.tabs([
        "📈 Yıllara Göre Yayın Trendi",
        "🌐 Yayın Veritabanları Dağılımı",
        "🏛️ Lider Kurumlar & Ülkeler",
        "⭐ En Çok Atıf Alan Makaleler"
    ])

    with tab_pub_trends:
        st.markdown("### 📊 6G Teknolojilerine Göre Akademik Yayın Artış Hızı")
        df_acad = AcademicService.get_tech_publication_trends_df()
        fig_acad = render_academic_trends_chart(df_acad)
        st.plotly_chart(fig_acad, use_container_width=True)

    with tab_sources:
        col_db, col_info = st.columns([1.2, 1])
        with col_db:
            db_dist = AcademicService.get_database_distribution()
            fig_db = render_academic_database_chart(db_dist)
            st.plotly_chart(fig_db, use_container_width=True)

        with col_info:
            st.markdown("""
                <div class="glass-card">
                    <h4 style="color: #00E5FF; margin-top: 0;">📌 Veritabanı Metrik Açıklaması</h4>
                    <p style="font-size: 0.9rem; color: #C8D1DC;">
                        <strong>IEEE Xplore:</strong> Elektrik ve Haberleşme mühendisliği alanındaki standart belirleyici makalelerin %45'ine ev sahipliği yapmaktadır.
                    </p>
                    <p style="font-size: 0.9rem; color: #C8D1DC;">
                        <strong>Google Scholar:</strong> Disiplinlerarası ve henüz hakem sürecindeki makalelerin en geniş kümesidir.
                    </p>
                </div>
            """, unsafe_allow_html=True)

    with tab_institutions:
        st.markdown("### 🏛️ Küresel 6G Araştırma Lideri Kurumlar")
        insts = AcademicService.get_top_institutions()
        df_insts = pd.DataFrame(insts)
        st.dataframe(
            df_insts,
            column_config={
                "name": "Kurum / Üniversite Adı",
                "country": "Ülke",
                "papers": "Yayın Sayısı",
                "citations": "Toplam Atıf Sayısı"
            },
            use_container_width=True,
            hide_index=True
        )

    with tab_cited:
        st.markdown("### ⭐ Literatürü Şekillendiren En Çok Atıf Alan 6G Makaleleri")
        papers = AcademicService.get_most_cited_papers()
        for paper in papers:
            st.markdown(f"""
                <div class="glass-card" style="margin-bottom: 12px; padding: 16px;">
                    <div style="display: flex; justify-content: space-between;">
                        <h4 style="color: #00E5FF; margin: 0;">{paper['title']}</h4>
                        <span class="trl-pill trl-high">⭐ {paper['citations']} Atıf</span>
                    </div>
                    <p style="color: #C8D1DC; font-size: 0.88rem; margin-top: 6px; margin-bottom: 4px;">
                        ✍️ <strong>Yazarlar:</strong> {paper['authors']} | 📖 <strong>Dergi:</strong> {paper['journal']} ({paper['year']})
                    </p>
                </div>
            """, unsafe_allow_html=True)
