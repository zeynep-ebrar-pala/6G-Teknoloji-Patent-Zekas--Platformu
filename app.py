"""
Türk Telekom 6G Technology & Patent Intelligence Platform
Main Application Entry Point - Staj Projesi Şartnamesine %100 Uyumlu Modüller
"""

import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Türk Telekom | 6G Teknoloji & Patent Zekası",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Imports
from styles import inject_custom_styles
from backend.data_service import DataService
from components.diagrams import render_technology_diagram
from components.charts import (
    render_trl_radar_chart,
    render_technology_performance_chart
)
from components.tt_scenarios import render_tt_scenario_calculator
from components.patent_views import render_patent_intelligence_module
from components.academic_views import render_academic_publication_module
from components.ai_chat_view import render_ai_assistant_module

# 3. Inject Corporate Theme & Styles
inject_custom_styles()

# 4. Load Data Services
TECHNOLOGIES = DataService.get_all_technologies()

# 5. API Key Security & Authentication Guard
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.markdown("""<div class="tt-header-container" style="text-align: center; max-width: 650px; margin: 60px auto 30px auto;">
<div style="background: linear-gradient(135deg, #0099FF 0%, #00C2FF 100%); width: 64px; height: 64px; border-radius: 16px; margin: 0 auto 16px auto; display: flex; align-items: center; justify-content: center; font-size: 32px; box-shadow: 0 0 24px rgba(0, 153, 255, 0.5);">
🔒
</div>
<span class="tt-badge">Kurumsal Güvenlik Kapısı</span>
<h2 class="tt-title" style="font-size: 1.8rem;">Türk Telekom 6G Ar-Ge Platformu</h2>
<p class="tt-subtitle" style="font-size: 0.92rem;">Lütfen devam etmek için geçerli 6G Ar-Ge Platformu API Key giriniz.</p>
</div>""", unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns([1, 1.5, 1])
    with col_b:
        api_key_input = st.text_input("🔑 Platform API Key:", type="password", placeholder="API Key giriniz (Örn: TT-6G-2026-KEY)")
        st.caption("💡 Test/Varsayılan Giriş Anahtarı: `TT-6G-2026-KEY` veya kendi OpenAI/Ar-Ge API Key'inizi kullanabilirsiniz.")
        
        if st.button("🚀 Platforma Güvenli Giriş Yap", use_container_width=True):
            if api_key_input.strip() != "":
                st.session_state["authenticated"] = True
                st.session_state["api_key"] = api_key_input
                st.rerun()
            else:
                st.error("❌ Lütfen geçerli bir API Key giriniz!")
    st.stop()


# 6. Authenticated Application Header & Sidebar
with st.sidebar:
    st.markdown("""<div style="text-align: center; padding: 12px 0;">
<div style="background: linear-gradient(135deg, #0099FF 0%, #00C2FF 100%); width: 52px; height: 52px; border-radius: 14px; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 0 20px rgba(0, 153, 255, 0.4);">
🇹🇷
</div>
<h3 style="color: #FFFFFF; margin-top: 10px; margin-bottom: 2px;">Türk Telekom</h3>
<p style="color: #00E5FF; font-size: 0.82rem; font-weight: 700; letter-spacing: 0.5px;">6G Ar-Ge Platformu</p>
</div>""", unsafe_allow_html=True)
    
    st.divider()

    navigation = st.radio(
        "Platform Menüsü:",
        [
            "🏠 Ana Sayfa & TRL Radar Haritası",
            "📡 Modül 1 — 6G Teknoloji Keşfi",
            "📜 Modül 2 — Patent Zekası ve Rakip Analizi",
            "📊 Modül 3 — Akademik Yayın Analizi",
            "🇹🇷 Türk Telekom Senaryo Çözümleyici",
            "🧠 Modül 4 — Türk Telekom 6G AI Asistanı",
            "💡 Proje Analizi & Gelecek Vizyonu"
        ]
    )

    st.divider()

    st.markdown("<p style='color: #94A3B8; font-size: 0.8rem; font-weight: 600;'>Anlatım Derinliği (Dual-Depth):</p>", unsafe_allow_html=True)
    view_mode = st.radio(
        "Derinlik Seviyesi:",
        ["🌱 Temel Seviye (Yönetici Özeti + Analojiler)", "⚡ Uzman Seviyesi (Derin Teknik + 3GPP/Formüller)"],
        index=0
    )

    st.divider()
    if st.button("🔒 Oturumu Kapat / API Key Temizle", use_container_width=True):
        st.session_state["authenticated"] = False
        st.rerun()

    st.markdown("""<div style="margin-top: 20px; padding: 10px; background: rgba(255,255,255,0.03); border-radius: 8px; font-size: 0.75rem; color: #64748B;">
🟢 Güvenli Oturum Açıldı<br>
© 2026 Türk Telekom Ar-Ge
</div>""", unsafe_allow_html=True)


# Main Header Banner (Title without "30 Günlük Staj Projesi —")
st.markdown("""<div class="tt-header-container">
<span class="tt-badge">Türk Telekom 6G Ar-Ge Platformu</span>
<h1 class="tt-title">Türk Telekom 6G Teknoloji & Patent Zekası Platformu</h1>
<p class="tt-subtitle">6G Teknolojileri, Patent Zekası ve Yayın Analitiği</p>
</div>""", unsafe_allow_html=True)


# =========================================================
# PAGE 1: Ana Sayfa & TRL Radar Haritası
# =========================================================
if navigation == "🏠 Ana Sayfa & TRL Radar Haritası":
    st.markdown("### 🌐 6G Teknolojileri Olgunluk Seviyesi (TRL Radar Haritası)")
    
    col_radar, col_info = st.columns([1.2, 1])

    with col_radar:
        fig_radar = render_trl_radar_chart(TECHNOLOGIES)
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_info:
        st.markdown("""<div class="glass-card">
<h4 style="color: #00E5FF; margin-top:0;">📌 6G Teknoloji Olgunluk Değerlendirmesi</h4>
<p style="font-size: 0.92rem; color: #C8D1DC;">
Bu radar haritası, 6G'yi şekillendirecek 7 temel öncü teknolojinin günümüzdeki 
<strong style="color: #FFFFFF;">TRL (Teknoloji Hazırlık Seviyesi)</strong> durumunu ve 3GPP standartlaşma takvimini göstermektedir.
</p>
<ul style="font-size: 0.88rem; color: #CBD5E1; padding-left: 20px; line-height: 1.6;">
<li><strong style="color: #00C853;">TRL 6 (İleri Düzey Saha Testi):</strong> NTN (Doğrudan Cihaza Uydu İletişimi - Rel-17/18)</li>
<li><strong style="color: #FFB020;">TRL 5 (Saha Pilotu & PoC):</strong> RIS & AI-Native RAN (O-RAN RIC Denemeleri)</li>
<li><strong style="color: #FF5252;">TRL 3-4 (Laboratuvar Testi):</strong> ISAC, Cell-Free MIMO, Ambient IoT, THz</li>
</ul>
</div>""", unsafe_allow_html=True)

    st.markdown("### 🛠️ 7 Temel 6G Teknolojisi Genel Bakış")
    
    cols = st.columns(3)
    for idx, (t_id, tech) in enumerate(TECHNOLOGIES.items()):
        col = cols[idx % 3]
        with col:
            trl_class = "trl-low" if tech["trl"] <= 4 else ("trl-mid" if tech["trl"] == 5 else "trl-high")
            
            # Render clean badge highlights
            highlights_html = " ".join([
                f"<span style='background: rgba(0, 153, 255, 0.12); color: #00C2FF; border: 1px solid rgba(0, 153, 255, 0.3); font-size: 0.73rem; padding: 2px 8px; border-radius: 6px; font-weight: 600; display: inline-block; margin: 2px 2px 2px 0;'>{h}</span>"
                for h in tech.get('highlights', [])
            ])

            st.markdown(f"""<div class="glass-card" style="min-height: 290px; display: flex; flex-direction: column; justify-content: space-between; margin-bottom: 16px;">
<div>
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
<span style="font-size: 2.2rem;">{tech['icon']}</span>
<span class="trl-pill {trl_class}">TRL {tech['trl']}</span>
</div>
<h4 style="color: #FFFFFF; margin: 4px 0 2px 0; font-size: 1.15rem;">{tech['acronym']}</h4>
<div style="color: #00C2FF; font-size: 0.8rem; font-weight: 600; margin-bottom: 10px;">{tech['title']}</div>
<p style="color: #E2E8F0; font-size: 0.86rem; line-height: 1.5; margin: 0 0 12px 0;">
{tech.get('card_summary', tech['executive_summary'][:120])}
</p>
</div>
<div>
<div style="margin-bottom: 10px;">{highlights_html}</div>
<div style="padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.08); font-size: 0.76rem; color: #94A3B8;">
🇹🇷 <strong>TT Senaryosu:</strong> {tech['tt_scenarios'][0][:45]}...
</div>
</div>
</div>""", unsafe_allow_html=True)


# =========================================================
# PAGE 2: Modül 1 — 6G Teknoloji Keşfi
# =========================================================
elif navigation == "📡 Modül 1 — 6G Teknoloji Keşfi":
    
    selected_tech_id = st.selectbox(
        "İncelemek İstediğiniz 6G Teknolojisini Seçin:",
        options=list(TECHNOLOGIES.keys()),
        format_func=lambda x: f"{TECHNOLOGIES[x]['icon']} {TECHNOLOGIES[x]['title']} (TRL {TECHNOLOGIES[x]['trl']})"
    )

    tech = DataService.get_technology_by_id(selected_tech_id)
    trl_class = "trl-low" if tech["trl"] <= 4 else ("trl-mid" if tech["trl"] == 5 else "trl-high")

    # Header Banner for Selected Tech
    st.markdown(f"""<div class="glass-card" style="border-left: 6px solid #0099FF;">
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
<div>
<span class="tt-badge">MODÜL 1 — 6G TEKNOLOJİ KEŞFİ</span>
<h2 style="color: #FFF; margin: 4px 0 0 0;">{tech['icon']} {tech['title']}</h2>
</div>
<span class="trl-pill {trl_class}">TRL {tech['trl']} Olgunluk Seviyesi</span>
</div>
</div>""", unsafe_allow_html=True)

    # Clean Turkish Tabs
    tab_overview, tab_principle, tab_arch, tab_usecase, tab_adv_dis, tab_global_tt, tab_media_refs = st.tabs([
        "📌 1. Teknoloji Tanımı",
        "⚙️ 2. Çalışma Prensibi & Blok Diyagram",
        "🏗️ 3. Sistem Mimarisi",
        "💡 4. Kullanım Alanları",
        "⚖️ 5. Avantajlar & Dezavantajlar",
        "🌐 6. Dünyadaki Çalışmalar & TT Senaryoları",
        "🎬 7. Grafikler, Video & Referanslar"
    ])

    # TAB 1: Teknoloji Tanımı
    with tab_overview:
        st.markdown("### 📌 Teknoloji Tanımı & Temel Kavramlar")
        if "Temel Seviye" in view_mode:
            st.markdown(f"""<div class="dual-card-beginner">
<h4 style="color: #00C853; margin-top:0; margin-bottom: 12px;">🌱 Temel Seviye (Yönetici Özeti + Analojiler)</h4>
<div style="color: #E2E8F0; font-size: 0.98rem; line-height: 1.6;">
{tech['executive_summary']}
</div>
</div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="dual-card-expert">
<h4 style="color: #00C2FF; margin-top:0; margin-bottom: 12px;">⚡ Uzman Seviyesi: Teknik Tanım & 3GPP Spesifikasyonları</h4>
<div style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
Bu teknoloji 3GPP Release 18/19/20 standartlaşma hedeflerinde 6G temel katmanı olarak tanımlanmıştır. 
Aşağıda PHY/MAC katman davranışları, kanal modelleri ve mimari gereksinimler özetlenmiştir.
</div>
</div>""", unsafe_allow_html=True)
            st.markdown(f"""<div class="glass-card">
<h4 style="color:#00E5FF; margin-top:0;">🔬 3GPP Mimarisi & Fiziksel Katman Özeti</h4>
<div style="color:#CBD5E1; font-size: 0.92rem; line-height: 1.6;">{tech['system_architecture']}</div>
</div>""", unsafe_allow_html=True)

    # TAB 2: Çalışma Prensibi & Blok Diyagram Animasyonu
    with tab_principle:
        col_p_text, col_p_diag = st.columns([1, 1.1])
        with col_p_text:
            st.markdown("### ⚙️ Çalışma Prensibi Detayı")
            st.markdown(f"""<div class="glass-card">
<div style="color: #E2E8F0; font-size: 0.92rem; line-height: 1.6;">
{tech['working_principle']}
</div>
</div>""", unsafe_allow_html=True)
        with col_p_diag:
            st.markdown("### 🎨 İnteraktif Blok Diyagram Animasyonu")
            render_technology_diagram(tech['id'])

    # TAB 3: Sistem Mimarisi & Donanım Katmanları
    with tab_arch:
        st.markdown("### 🏗️ Sistem Mimarisi & Donanım Katmanları")
        formula_html = f"<div class='formula-box'><strong>📐 Matematiksel/Fiziksel Formül Modeli (Uzman Modu):</strong><br><br>{tech.get('mathematical_foundation', '')}</div>" if "Uzman" in view_mode and tech.get('mathematical_foundation') else ""
        st.markdown(f"""<div class="glass-card">
<div style="color: #E2E8F0; font-size: 0.92rem; line-height: 1.6;">
{tech['system_architecture']}
</div>
{formula_html}
</div>""", unsafe_allow_html=True)

    # TAB 4: Kullanım Alanları
    with tab_usecase:
        st.markdown("### 💡 Kullanım Alanları & Uygulama Senaryoları")
        cols_uc = st.columns(2)
        for idx, uc in enumerate(tech['use_cases']):
            col = cols_uc[idx % 2]
            with col:
                st.markdown(f"""<div class="glass-card" style="margin-bottom: 12px; border-left: 4px solid #00E5FF;">
<h4 style="color: #00E5FF; margin: 0 0 6px 0;">Senaryo #{idx+1}</h4>
<p style="color: #E2E8F0; font-size: 0.9rem; margin: 0;">{uc}</p>
</div>""", unsafe_allow_html=True)

    # TAB 5: Avantajlar & Dezavantajlar (Fixed single HTML render per column)
    with tab_adv_dis:
        c_adv, c_dis = st.columns(2)
        with c_adv:
            st.markdown("### ✅ Avantajlar")
            adv_items = "".join([f"<li style='margin-bottom:10px; line-height:1.5;'><strong style='color:#00C853;'>✓</strong> {adv}</li>" for adv in tech['advantages']])
            adv_html = f"""<div class="glass-card" style="border-left: 4px solid #00C853;">
<ul style="list-style: none; padding-left: 0; margin: 0; color: #E2E8F0; font-size: 0.92rem;">
{adv_items}
</ul>
</div>"""
            st.markdown(adv_html, unsafe_allow_html=True)

        with c_dis:
            st.markdown("### ⚠️ Dezavantajlar / Zorluklar")
            dis_items = "".join([f"<li style='margin-bottom:10px; line-height:1.5;'><strong style='color:#FF5252;'>✗</strong> {dis}</li>" for dis in tech['disadvantages']])
            dis_html = f"""<div class="glass-card" style="border-left: 4px solid #FF5252;">
<ul style="list-style: none; padding-left: 0; margin: 0; color: #E2E8F0; font-size: 0.92rem;">
{dis_items}
</ul>
</div>"""
            st.markdown(dis_html, unsafe_allow_html=True)

    # TAB 6: Dünyadaki Çalışmalar, Türk Telekom Senaryoları & TRL (Fixed single HTML render)
    with tab_global_tt:
        c_g, c_tt_box, c_t_level = st.columns([1, 1, 0.9])
        with c_g:
            st.markdown("### 🌐 Dünyadaki Çalışmalar")
            gr_items = "".join([f"<li style='margin-bottom:10px; line-height:1.5;'><span style='color:#00C2FF;'>🔹</span> <strong style='color:#FFFFFF;'>{gr}</strong></li>" for gr in tech['global_research']])
            gr_html = f"""<div class="glass-card">
<ul style="list-style: none; padding-left: 0; margin: 0; color: #E2E8F0; font-size: 0.9rem;">
{gr_items}
</ul>
</div>"""
            st.markdown(gr_html, unsafe_allow_html=True)

        with c_tt_box:
            st.markdown("### 🇹🇷 Türk Telekom Senaryoları")
            tt_items = "".join([f"<p style='margin-bottom:12px; line-height:1.5; font-size:0.9rem; color:#E2E8F0;'><span style='font-size:1.1rem;'>🇹🇷</span> {tt_sc}</p>" for tt_sc in tech['tt_scenarios']])
            tt_html = f"""<div class="glass-card" style="border-left: 4px solid #FFB020;">
{tt_items}
</div>"""
            st.markdown(tt_html, unsafe_allow_html=True)

        with c_t_level:
            st.markdown("### 📊 TRL Değerlendirmesi")
            st.markdown(f"""<div class="glass-card" style="text-align: center;">
<span class="trl-pill {trl_class}" style="font-size: 1.3rem; padding: 10px 24px;">TRL {tech['trl']}</span>
<p style="color: #CBD5E1; font-size: 0.88rem; margin-top: 14px; line-height: 1.5;">{tech['trl_desc']}</p>
</div>""", unsafe_allow_html=True)

    # TAB 7: Performans Grafikleri, Kısa Video & Referans Makaleler
    with tab_media_refs:
        st.markdown("### 📈 Performans Grafikleri")
        fig_p = render_technology_performance_chart(tech['id'])
        st.plotly_chart(fig_p, use_container_width=True)

        st.divider()

        col_v, col_r = st.columns([1, 1])
        with col_v:
            st.markdown("### 🎬 Kısa Video (Demonstrasyon / Simülasyon)")
            st.markdown(f"""<div class="glass-card" style="text-align: center;">
<div style="background: #090C12; border-radius: 10px; padding: 30px; border: 1px dashed #00E5FF;">
<span style="font-size: 3rem;">🎥</span>
<h4 style="color: #00E5FF; margin-top: 10px;">6G {tech['acronym']} Simülasyon Videosu</h4>
<p style="color: #94A3B8; font-size: 0.85rem;">Laboratuvar PoC & Saha Deneyi İnteraktif Demo Video Oynatıcı</p>
</div>
</div>""", unsafe_allow_html=True)

        with col_r:
            st.markdown("### 📚 Referans Makaleler & Yayınlar")
            ref_items = "".join([f"<p style='margin-bottom:8px; font-size:0.88rem; color:#CBD5E1; line-height:1.5;'>📖 {ref}</p>" for ref in tech['references']])
            st.markdown(f"""<div class="glass-card">
{ref_items}
</div>""", unsafe_allow_html=True)


# =========================================================
# PAGE 3: Modül 2 — Patent Zekası ve Rakip Analizi
# =========================================================
elif navigation == "📜 Modül 2 — Patent Zekası ve Rakip Analizi":
    render_patent_intelligence_module()


# =========================================================
# PAGE 4: Modül 3 — Akademik Yayın Analizi
# =========================================================
elif navigation == "📊 Modül 3 — Akademik Yayın Analizi":
    render_academic_publication_module()


# =========================================================
# PAGE 5: Türk Telekom Senaryo Çözümleyici
# =========================================================
elif navigation == "🇹🇷 Türk Telekom Senaryo Çözümleyici":
    render_tt_scenario_calculator()


# =========================================================
# PAGE 6: Modül 4 — Türk Telekom 6G AI Asistanı
# =========================================================
elif navigation == "🧠 Modül 4 — Türk Telekom 6G AI Asistanı":
    render_ai_assistant_module()


# =========================================================
# PAGE 7: Proje Analizi & Gelecek Vizyonu
# =========================================================
elif navigation == "💡 Proje Analizi & Gelecek Vizyonu":
    st.markdown("### 💡 Proje Analizi, Mimari Değerlendirme & Gelecek Yol Haritası")
    st.markdown("""<div class="glass-card" style="border-left: 5px solid #00E5FF;">
<h4 style="color:#00E5FF; margin-top:0;">🚀 Türk Telekom 6G Intelligence Platformu Gelecek Vizyonu</h4>
<p style="color:#E2E8F0; font-size:0.95rem; line-height: 1.6;">
Bu proje, Türk Telekom Ar-Ge ekibinin 6G teknoloji trendlerini, patent peyzajını ve akademik yayın hareketliliğini 
tek bir kurumsal portal üzerinden izlemesi amacıyla geliştirilmiştir. Aşağıda mevcut mimarinin <strong>geliştirilebilir 5 temel stratejik yönü</strong> özetlenmiştir:
</p>
</div>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="glass-card">
<h4 style="color:#00C2FF;">1. 🌐 Canlı Web Service & API Bağlantıları</h4>
<p style="color:#CBD5E1; font-size:0.88rem; line-height:1.5;">
• <strong>Mevcut Durum:</strong> Patent ve yayın verileri simüle edilmiş ve önceden yüklenmiş veri kümeleridir.<br>
• <strong>Geliştirme:</strong> Google Patents API, WIPO PATENTSCOPE, OpenAlex ve IEEE Xplore canlı REST API entegrasyonu ile haftalık otomatik veri çekme hattı (ETL Pipeline) kurulabilir.
</p>
</div>
            
<div class="glass-card">
<h4 style="color:#00C853;">2. 🧠 Gerçek RAG & Vektör Veritabanı (FAISS / ChromaDB)</h4>
<p style="color:#CBD5E1; font-size:0.88rem; line-height:1.5;">
• <strong>Mevcut Durum:</strong> AI Asistanı kural tabanlı akıllı sorgu motoru kullanmaktadır.<br>
• <strong>Geliştirme:</strong> LangChain / LlamaIndex altyapısı ve FAISS vektör veritabanı ile 6G PDF makaleleri ve 3GPP standart belgeleri gerçek zamanlı semantik olarak indekslenebilir.
</p>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="glass-card">
<h4 style="color:#FFB020;">3. 📐 Canlı 3GPP RF Link Budget & Simülasyon Motoru</h4>
<p style="color:#CBD5E1; font-size:0.88rem; line-height:1.5;">
• <strong>Mevcut Durum:</strong> Sinyal yayılımı ve kapsama hesaplamaları kural tabanlıdır.<br>
• <strong>Geliştirme:</strong> Kullanıcının frekans (GHz/THz), mesafe (m), anten sayısı ve hava durumu girmesine olanak tanıyan canlı Python RF kapsama ve SNR simülatörü eklenebilir.
</p>
</div>

<div class="glass-card">
<h4 style="color:#FF5252;">4. 📊 Otomatik Yönetici PDF / PPTX Sunum Export</h4>
<p style="color:#CBD5E1; font-size:0.88rem; line-height:1.5;">
• <strong>Mevcut Durum:</strong> Analizler web arayüzünde görüntülenebilir.<br>
• <strong>Geliştirme:</strong> Türk Telekom Yönetim Kurulu ve Ar-Ge direktörleri için tek tıkla özelleştirilmiş 6G Teknoloji ve Patent Yönetici Raporu (PDF / PowerPoint) üretme özelliği eklenebilir.
</p>
</div>""", unsafe_allow_html=True)
