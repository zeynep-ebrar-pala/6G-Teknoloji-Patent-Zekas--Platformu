"""
Türk Telekom 6G Technology & Patent Intelligence Platform
Ana giriş — staj şartnamesi menü yapısı.
"""

import streamlit as st

st.set_page_config(
    page_title="Türk Telekom | 6G Teknoloji & Patent Zekası",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded",
)

from styles import inject_custom_styles
from backend.academic_service import AcademicService
from backend.data_service import DataService
from backend.patent_service import PatentService
from components.about_view import render_about_page
from components.academic_views import render_academic_publication_module
from components.ai_chat_view import render_ai_assistant_module
from components.charts import (
    render_academic_trends_chart,
    render_technology_record_counts_chart,
    render_trl_radar_chart,
)
from components.diagrams import render_technology_diagram
from components.patent_views import render_patent_intelligence_module
from components.tt_scenarios import render_tt_scenario_calculator
from components.ui_helpers import show_empty, show_error

inject_custom_styles()

TECHNOLOGIES = DataService.get_all_technologies()


def _first_text(*vals) -> str:
    """Kart/HTML alanlarında None veya boş string basılmasını önler."""
    for val in vals:
        if val is None:
            continue
        text = str(val).strip()
        if text and text.lower() != "none":
            return text
    return ""

NAV_HOME = "Ana Sayfa"
NAV_TECH = "6G Teknolojileri"
NAV_PATENT = "Patent Zekası"
NAV_PUB = "Yayın Trendleri"
NAV_TT = "Türk Telekom Görünümü"
NAV_AI = "AI Asistan"
NAV_ABOUT = "Hakkında"

with st.sidebar:
    st.markdown(
        """<div style="text-align: center; padding: 12px 0;">
<div style="background: linear-gradient(135deg, #0099FF 0%, #00C2FF 100%); width: 52px; height: 52px; border-radius: 14px; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-size: 24px; box-shadow: 0 0 20px rgba(0, 153, 255, 0.4);">
📡
</div>
<h3 style="color: #FFFFFF; margin-top: 10px; margin-bottom: 2px;">Türk Telekom</h3>
<p style="color: #00E5FF; font-size: 0.82rem; font-weight: 700; letter-spacing: 0.5px;">6G Ar-Ge Platformu</p>
</div>""",
        unsafe_allow_html=True,
    )

    st.divider()

    navigation = st.radio(
        "Platform Menüsü:",
        [NAV_HOME, NAV_TECH, NAV_PATENT, NAV_PUB, NAV_TT, NAV_AI, NAV_ABOUT],
    )

    st.divider()

    st.markdown(
        "<p style='color: #94A3B8; font-size: 0.8rem; font-weight: 600;'>Anlatım Derinliği (Dual-Depth):</p>",
        unsafe_allow_html=True,
    )
    view_mode = st.radio(
        "Derinlik Seviyesi:",
        [
            "Temel Seviye (Yönetici Özeti + Analojiler)",
            "Uzman Seviyesi (Derin Teknik + 3GPP/Formüller)",
        ],
        index=0,
    )

    st.divider()
    if st.session_state.get("api_key") or st.session_state.get("ai_ready"):
        if st.button("AI oturumunu kapat", use_container_width=True):
            for key in ("authenticated", "api_key", "ai_provider", "ai_ready", "chat_messages"):
                st.session_state.pop(key, None)
            st.rerun()

    provider_label = st.session_state.get("ai_provider", "kapalı")
    st.markdown(
        f"""<div style="margin-top: 20px; padding: 10px; background: rgba(255,255,255,0.03); border-radius: 8px; font-size: 0.75rem; color: #64748B;">
AI sağlayıcı: {provider_label}<br>
© 2026 Türk Telekom Ar-Ge
</div>""",
        unsafe_allow_html=True,
    )


st.markdown(
    """<div class="tt-header-container">
<span class="tt-badge">Türk Telekom 6G Ar-Ge Platformu</span>
<h1 class="tt-title">Türk Telekom 6G Teknoloji &amp; Patent Zekası Platformu</h1>
<p class="tt-subtitle">6G Teknolojileri, Patent Zekası ve Yayın Analitiği</p>
</div>""",
    unsafe_allow_html=True,
)


if navigation == NAV_HOME:
    beginner = "Temel Seviye" in view_mode
    if beginner:
        st.markdown(
            """<div class="dual-card-beginner">
<h4 style="margin-top:0;">6G nedir? — sıfır teknik bilgiyle</h4>
<p style="color:#E2E8F0; font-size:1.02rem; line-height:1.7; margin:0 0 10px 0;">
Telefonunuz bugün <strong>5G</strong> ile bağlanır. <strong>6G</strong> bir sonraki nesildir: daha hızlı internet
değil yalnızca; kulelerin yeni işler yapmasıdır. Yedi yapı taşı şunu çözer:
<strong>kör noktayı kapatmak</strong>, <strong>kopmayı bitirmek</strong>, <strong>dağı ve denizi kapsamak</strong>,
<strong>kuleyi radar yapmak</strong>, <strong>şebekeyi kendi kendine ayarlamak</strong>,
<strong>pilsiz nesne izlemek</strong> ve (ileride) <strong>çok kalın kablosuz boru</strong> açmak.
</p>
<p style="color:#CBD5E1; font-size:0.92rem; line-height:1.6; margin:0;">
Her kartta sıra aynıdır: <em>bugünün sorunu → 6G çözümü → günlük analoji → Türk Telekom’da ne işe yarar</em>.
Soldan <strong>Uzman Seviyesi</strong> açılırsa formül, 3GPP ve mimari gelir; temel seviyede jargon yok.
</p>
</div>""",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """<div class="dual-card-expert">
<h4 style="margin-top:0;">6G yapı taşları — uzman okuma</h4>
<p style="color:#E2E8F0; font-size:0.95rem; line-height:1.65; margin:0;">
Yedi enabler: ISAC (ortak dalga şekli), RIS (pasif faz yüzeyi), Cell-Free Massive MIMO,
Sub-THz/THz, AI-native RAN (O-RAN RIC), NTN (3GPP Rel-17+ Direct-to-Cell), Ambient IoT.
TRL 1–9 radar haritası saha olgunluğunu özetler. Mimari, CRB/Shannon ve protokol için
<strong>6G Teknolojileri</strong> sekmelerine geçin — uydurma metrik yok, referans DOI/3GPP’dir.
</p>
</div>""",
            unsafe_allow_html=True,
        )

    st.markdown("### 6G Teknolojileri Olgunluk Seviyesi (TRL Radar Haritası)")

    col_radar, col_info = st.columns([1.2, 1])

    with col_radar:
        fig_radar = render_trl_radar_chart(TECHNOLOGIES)
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_info:
        st.markdown(
            """<div class="glass-card">
<h4 style="color: #00E5FF; margin-top:0;">TRL nedir? (olgunluk notu)</h4>
<p style="font-size: 0.92rem; color: #C8D1DC; line-height:1.65;">
TRL, “bu teknoloji ne kadar hazır?” sorusunun 1’den 9’a notudur.
<strong style="color:#FFFFFF;">1 = fikir</strong>, <strong style="color:#FFFFFF;">9 = sahada satışa yakın</strong>.
6G’nin hepsi aynı anda gelmez: uydu kapsama (NTN) diğerlerinden öndedir; THz hâlâ laboratuvardır.
Bu notlar pazarlama vaadi değil, saha/standart olgunluğuna göre okunmalıdır.
</p>
<ul style="font-size: 0.88rem; color: #CBD5E1; padding-left: 20px; line-height: 1.7;">
<li><strong style="color: #00C853;">TRL 6 — sahaya en yakın:</strong> NTN — dağ, deniz, afet yedek hattı</li>
<li><strong style="color: #FFB020;">TRL 5 — pilot:</strong> RIS (akıllı ayna) ve AI-RAN (öğrenen şebeke)</li>
<li><strong style="color: #FF5252;">TRL 4 — erken deneme:</strong> ISAC, Hücresiz MIMO, Pilsiz IoT</li>
<li><strong style="color: #FF7043;">TRL 3 — laboratuvar:</strong> THz — rekor hız, kısa menzil, sokakta değil</li>
</ul>
</div>""",
            unsafe_allow_html=True,
        )

    st.markdown("### Yedi yapı taşı — her biri bir sorunu çözer")
    st.caption(
        "Kartta önce sorun, sonra çözüm vardır. Ayrıntı, analoji ve Türk Telekom senaryosu için "
        "soldan «6G Teknolojileri» menüsüne geçin."
    )

    cols = st.columns(3)
    for idx, (t_id, tech) in enumerate(TECHNOLOGIES.items()):
        col = cols[idx % 3]
        with col:
            trl_class = "trl-low" if tech["trl"] <= 4 else ("trl-mid" if tech["trl"] == 5 else "trl-high")
            blurb = _first_text(
                tech.get("beginner_card"),
                tech.get("card_summary"),
                tech.get("beginner_one_liner"),
            )
            kicker = _first_text(tech.get("beginner_kicker"))
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


elif navigation == NAV_TECH:
    selected_tech_id = st.selectbox(
        "İncelemek İstediğiniz 6G Teknolojisini Seçin:",
        options=list(TECHNOLOGIES.keys()),
        format_func=lambda x: f"{TECHNOLOGIES[x]['icon']} {TECHNOLOGIES[x]['title']} (TRL {TECHNOLOGIES[x]['trl']})",
    )

    tech = DataService.get_technology_by_id(selected_tech_id)
    trl_class = "trl-low" if tech["trl"] <= 4 else ("trl-mid" if tech["trl"] == 5 else "trl-high")

    st.markdown(
        f"""<div class="glass-card" style="border-left: 6px solid #0099FF;">
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
<div>
<span class="tt-badge">6G TEKNOLOJİLERİ</span>
<h2 style="color: #FFF; margin: 4px 0 0 0;">{tech['icon']} {tech['title']}</h2>
</div>
<span class="trl-pill {trl_class}">TRL {tech['trl']} Olgunluk Seviyesi</span>
</div>
</div>""",
        unsafe_allow_html=True,
    )

    tab_overview, tab_principle, tab_arch, tab_usecase, tab_adv_dis, tab_global_tt, tab_media_refs = st.tabs(
        [
            "1. Teknoloji Tanımı",
            "2. Çalışma Prensibi & Blok Diyagram",
            "3. Sistem Mimarisi",
            "4. Kullanım Alanları",
            "5. Avantajlar & Dezavantajlar",
            "6. Dünyadaki Çalışmalar & TT Senaryoları",
            "7. Performans Grafikleri & Referanslar",
        ]
    )

    with tab_overview:
        st.markdown("### Teknoloji Tanımı & Temel Kavramlar")
        if "Temel Seviye" in view_mode:
            teach = _first_text(tech.get("beginner_teach"))
            if teach:
                st.markdown(
                    f"""<div class="dual-card-beginner">
<h4 style="color: #00C853; margin-top:0; margin-bottom: 14px;">Sıfırdan anlatım — sorun, çözüm, analoji</h4>
<div class="teach-grid">{teach}</div>
</div>""",
                    unsafe_allow_html=True,
                )
            st.markdown(
                f"""<div class="glass-card">
<h4 style="color: #00E5FF; margin-top:0; margin-bottom: 12px;">Yönetici özeti (1 cümle + analoji)</h4>
<div style="color: #E2E8F0; font-size: 0.98rem; line-height: 1.65;">
{tech['executive_summary']}
</div>
</div>""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""<div class="dual-card-expert">
<h4 style="color: #00C2FF; margin-top:0; margin-bottom: 12px;">Uzman Seviyesi: Teknik Tanım & 3GPP</h4>
<div style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.6;">
{tech['system_architecture']}
</div>
</div>""",
                unsafe_allow_html=True,
            )

    with tab_principle:
        col_p_text, col_p_diag = st.columns([1, 1.1])
        with col_p_text:
            principle = _first_text(
                tech.get("beginner_principle") if "Temel Seviye" in view_mode else None,
                tech.get("working_principle"),
            )
            heading = (
                "Çalışma prensibi — üç adımda"
                if "Temel Seviye" in view_mode
                else "Çalışma Prensibi (teknik)"
            )
            st.markdown(f"### {heading}")
            st.markdown(
                f"""<div class="glass-card">
<div style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.65;">
{principle}
</div>
</div>""",
                unsafe_allow_html=True,
            )
        with col_p_diag:
            st.markdown("### İnteraktif Blok Diyagram Animasyonu")
            render_technology_diagram(tech["id"])

    with tab_arch:
        st.markdown("### Sistem Mimarisi & Donanım Katmanları")
        if "Temel Seviye" in view_mode:
            arch = _first_text(tech.get("beginner_arch"))
            st.markdown(
                f"""<div class="dual-card-beginner">
<h4 style="color:#00C853; margin-top:0;">Üç katman — jargon yok</h4>
<div style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.65;">
{arch}
</div>
</div>""",
                unsafe_allow_html=True,
            )
        else:
            formula_html = (
                f"<div class='formula-box'><strong>Matematiksel/Fiziksel Formül Modeli (Uzman Modu):</strong><br><br>{tech.get('mathematical_foundation', '')}</div>"
                if tech.get("mathematical_foundation")
                else ""
            )
            st.markdown(
                f"""<div class="glass-card">
<div style="color: #E2E8F0; font-size: 0.92rem; line-height: 1.6;">
{tech['system_architecture']}
</div>
{formula_html}
</div>""",
                unsafe_allow_html=True,
            )

    with tab_usecase:
        st.markdown("### Kullanım Alanları & Uygulama Senaryoları")
        st.caption("Her senaryo, teknolojinin gerçek dünyada nerede ve nasıl kullanıldığını açıklar.")
        cols_uc = st.columns(2)
        for idx, uc in enumerate(tech["use_cases"]):
            col = cols_uc[idx % 2]
            with col:
                if isinstance(uc, dict):
                    title = uc.get("title", f"Senaryo #{idx+1}")
                    desc = uc.get("description", "")
                else:
                    title = f"Senaryo #{idx+1}"
                    desc = uc
                st.markdown(
                    f"""<div class="glass-card" style="margin-bottom: 12px; border-left: 4px solid #00E5FF;">
<h4 style="color: #00E5FF; margin: 0 0 8px 0;">{title}</h4>
<p style="color: #E2E8F0; font-size: 0.9rem; margin: 0; line-height: 1.55;">{desc}</p>
</div>""",
                    unsafe_allow_html=True,
                )

    with tab_adv_dis:
        c_adv, c_dis = st.columns(2)
        with c_adv:
            st.markdown("### Avantajlar")
            adv_items = "".join(
                [f"<li style='margin-bottom:10px; line-height:1.5;'><strong style='color:#00C853;'>✓</strong> {adv}</li>" for adv in tech["advantages"]]
            )
            st.markdown(
                f"""<div class="glass-card" style="border-left: 4px solid #00C853;">
<ul style="list-style: none; padding-left: 0; margin: 0; color: #E2E8F0; font-size: 0.92rem;">
{adv_items}
</ul>
</div>""",
                unsafe_allow_html=True,
            )
        with c_dis:
            st.markdown("### Dezavantajlar / Zorluklar")
            dis_items = "".join(
                [f"<li style='margin-bottom:10px; line-height:1.5;'><strong style='color:#FF5252;'>✗</strong> {dis}</li>" for dis in tech["disadvantages"]]
            )
            st.markdown(
                f"""<div class="glass-card" style="border-left: 4px solid #FF5252;">
<ul style="list-style: none; padding-left: 0; margin: 0; color: #E2E8F0; font-size: 0.92rem;">
{dis_items}
</ul>
</div>""",
                unsafe_allow_html=True,
            )

    with tab_global_tt:
        c_g, c_tt_box, c_t_level = st.columns([1, 1, 0.9])
        with c_g:
            st.markdown("### Dünyadaki Çalışmalar")
            gr_items = "".join(
                [f"<li style='margin-bottom:10px; line-height:1.5;'><span style='color:#00C2FF;'>🔹</span> <strong style='color:#FFFFFF;'>{gr}</strong></li>" for gr in tech["global_research"]]
            )
            st.markdown(
                f"""<div class="glass-card">
<ul style="list-style: none; padding-left: 0; margin: 0; color: #E2E8F0; font-size: 0.9rem;">
{gr_items}
</ul>
</div>""",
                unsafe_allow_html=True,
            )
        with c_tt_box:
            st.markdown("### Türk Telekom Senaryoları")
            tt_items = "".join(
                [f"<p style='margin-bottom:12px; line-height:1.5; font-size:0.9rem; color:#E2E8F0;'>{tt_sc}</p>" for tt_sc in tech["tt_scenarios"]]
            )
            st.markdown(
                f"""<div class="glass-card" style="border-left: 4px solid #FFB020;">
{tt_items}
</div>""",
                unsafe_allow_html=True,
            )
        with c_t_level:
            st.markdown("### TRL Değerlendirmesi")
            st.markdown(
                f"""<div class="glass-card" style="text-align: center;">
<span class="trl-pill {trl_class}" style="font-size: 1.3rem; padding: 10px 24px;">TRL {tech['trl']}</span>
<p style="color: #CBD5E1; font-size: 0.88rem; margin-top: 14px; line-height: 1.5;">{tech['trl_desc']}</p>
</div>""",
                unsafe_allow_html=True,
            )

    with tab_media_refs:
        st.markdown("### Performans — doğrulanmış kayıt sayımı")
        st.caption(
            "Temsili 5G/6G hedef barı yok. Aşağıdaki grafikler bu teknolojinin "
            "doğrulanmış patent kayıt sayısı ve (varsa) OpenAlex yayın trendidir."
        )
        domain = PatentService.domain_for_tech(tech["id"])
        df_pat = PatentService.get_domain_yearly_df(tech["id"])
        if df_pat.empty:
            show_empty(f"«{domain or tech['acronym']}» için doğrulanmış patent kaydı yok.")
        else:
            st.plotly_chart(
                render_technology_record_counts_chart(df_pat, domain or tech["acronym"]),
                use_container_width=True,
            )

        openalex_topic = {
            "isac": "ISAC",
            "ris": "RIS",
            "thz": "THz",
            "ai_ran": "AI-RAN",
            "ntn": "NTN",
            "ambient_iot": "Ambient IoT",
        }.get(tech["id"])
        if openalex_topic:
            df_pub = AcademicService.get_topic_yearly_df(openalex_topic)
            if df_pub is None or df_pub.empty:
                show_error("OpenAlex bu konu için yanıt vermedi; yayın trendi gizlendi.")
            else:
                st.plotly_chart(render_academic_trends_chart(df_pub), use_container_width=True)
        else:
            st.caption("Cell-Free, şartnamedeki akademik konu listesinde yoktur; OpenAlex serisi gösterilmez.")

        st.divider()
        st.markdown("### Referans Makaleler & Yayınlar")
        st.caption("Bağlantılar DOI veya resmi 3GPP / proje sayfalarına gider.")
        ref_items = "".join(
            [
                f"""<p style='margin-bottom:8px; font-size:0.88rem; line-height:1.5;'>
            📖 <a href="{ref['url']}" target="_blank" rel="noopener noreferrer"
            style="color:#00E5FF; text-decoration:none; border-bottom:1px solid rgba(0,229,255,0.35);">
            {ref['text']}</a></p>"""
                for ref in tech["references"]
            ]
        )
        st.markdown(f"""<div class="glass-card">{ref_items}</div>""", unsafe_allow_html=True)


elif navigation == NAV_PATENT:
    render_patent_intelligence_module()

elif navigation == NAV_PUB:
    render_academic_publication_module()

elif navigation == NAV_TT:
    render_tt_scenario_calculator()

elif navigation == NAV_AI:
    render_ai_assistant_module()

elif navigation == NAV_ABOUT:
    render_about_page()
