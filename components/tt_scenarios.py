"""
 Türk Telekom 6G Platform - Türk Telekom Specific Scenarios Frontend Component
 Renders interactive Turkish telecom deployment scenario UI using Backend ScenarioEngine.
"""

import streamlit as st
from backend.scenario_engine import ScenarioEngine

def render_tt_scenario_calculator():
    """Interactive deployment scenario UI component for Türk Telekom Ar-Ge."""
    
    st.markdown("""<div class="glass-card" style="border-left: 5px solid #0099FF; margin-bottom: 20px;">
<div style="display: flex; align-items: center; gap: 14px;">
<span style="font-size: 2.2rem;">🇹🇷</span>
<div>
<h3 style="color: #FFFFFF; margin: 0;">Türk Telekom 6G Saha Dağıtım ve Senaryo Çözümleyici</h3>
<p style="color: #CBD5E1; font-size: 0.92rem; margin-top: 4px; margin-bottom: 0;">
Türkiye coğrafyası, Türk Telekom altyapısı ve stratejik Ar-Ge hedeflerine göre 6G teknoloji eşleştirme motoru.
</p>
</div>
</div>
</div>""", unsafe_allow_html=True)

    col_inputs, col_results = st.columns([1, 1.15])

    with col_inputs:
        with st.container(border=True):
            st.markdown("### ⚙️ Senaryo Parametreleri")
            
            region = st.selectbox(
                "📍 1. Uygulama Bölgesi / Senaryo Alanı:",
                [
                    "İstanbul Boğazı & Marmara Deniz Sahili (ISAC + THz)",
                    "RAMS Park / Stadyum & Yoğun Etkinlik Alanları (Cell-Free MIMO)",
                    "Marmara Sanayi Bölgesi / Otonom Fabrikalar (Ambient IoT + AI-RAN)",
                    "AFAD Entegre Deprem & Afet Bölgesi (NTN + ISAC)",
                    "Tarihi Yarımada / Dar Sokak Kentsel Alan (RIS + Sub-THz)",
                    "Türk Telekom Ankara & İstanbul Data Center (THz Mesh)"
                ],
                help="Eşleştirilecek Türk Telekom saha veya altyapı bölgesi"
            )

            user_density = st.select_slider(
                "👥 2. Hedef Kullanıcı / Sensör Yoğunluğu:",
                options=[
                    "Düşük (Kırsal/Açık)",
                    "Orta (Şehir İçi)",
                    "Yüksek (Stadyum/Meydan)",
                    "Aşırı Yoğun (Trilyon Sensör)"
                ],
                help="Bölgedeki kilometrekare başına düşen cihaz ve sensör yoğunluğu"
            )

            priority = st.radio(
                "🎯 3. Öncelikli Stratejik Hedef:",
                [
                    "Kesintisiz Kapsama (Zero Gap)",
                    "Ultra Yüksek Hız (Terabit/s)",
                    "Düşük Enerji / Yeşil Şebeke",
                    "Afet Dayanıklılığı"
                ],
                help="Bu dağıtımda hedeflenen birincil performans veya iş hedefi"
            )

        # Compute Backend Evaluation
        eval_res = ScenarioEngine.evaluate_scenario(region, user_density, priority)

        # 📊 Detaylı Performans & Metrik Özeti in left column
        st.write("")
        with st.expander("📊 Detaylı Performans & Metrik Özeti", expanded=True):
            st.markdown(eval_res['impact_summary'])
            st.caption(f"💰 Tahmini CAPEX Ölçeği: **{eval_res['capex_estimate']}**")

    with col_results:
        with st.container(border=True):
            st.markdown("### 🎯 Önerilen Türk Telekom Mimarisi ve KPI Analizi")
            
            c_header_1, c_header_2 = st.columns([2.2, 1])
            with c_header_1:
                st.markdown(f"#### 📍 {eval_res['region_title']}")
            with c_header_2:
                st.info(f"🗓️ {eval_res['target_year']}")

            # Tech badges formatted in clean native Markdown pills
            tech_str = "  ".join([f"`{t}`" for t in eval_res['recommended_tech']])
            st.markdown(f"**Önerilen 6G Teknolojileri:** {tech_str}")
            
            st.divider()
            
            st.markdown(f"📡 **Saha Çözüm Mimarisi:**\n{eval_res['solution']}")
            st.write("")
            
            st.success(
                f"📌 **Stratejik Hedef Etkisi:**\n{eval_res['priority_kpi']}\n\n"
                f"📊 **Yoğunluk Profili:** {eval_res['density_kpi']}"
            )

            st.divider()

            # Dynamic KPI Gauges / Metrics
            kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
            with kpi_col1:
                st.metric(label="⚡ Hız Kapasitesi", value=f"{eval_res['capacity_gbps']} Gbps")
            with kpi_col2:
                st.metric(label="⏱️ Gecikme (Latency)", value=f"{eval_res['latency_ms']} ms")
            with kpi_col3:
                st.metric(label="🌿 Enerji Skoru", value=f"%{eval_res['energy_score']}")

            st.write("")
            st.markdown(f"**Uygulanabilirlik & Saha Uyumluluk Skoru:** `%{eval_res['feasibility_score']}`")
            st.progress(eval_res['feasibility_score'] / 100.0)
