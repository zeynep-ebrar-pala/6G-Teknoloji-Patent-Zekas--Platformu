"""
Modül 3 — Akademik Yayın Analizi arayüzü.
DOI doğrulamalı set her zaman doludur; OpenAlex canlı/önbellek varsa eklenir.
"""

import streamlit as st

from backend.academic_service import AcademicService
from components.charts import (
    render_academic_bar_chart,
    render_academic_database_chart,
    render_academic_trends_chart,
)
from components.ui_helpers import render_module_header, render_paper_card, render_source_button, show_empty, select_section, show_plotly


def render_academic_publication_module():
    summary = AcademicService.get_summary()
    papers = AcademicService.get_most_cited_papers()

    render_module_header(
        "Yayın Trendleri",
        "Bu sayfa önce DOI ile doğrulanmış makale setini gösterir. "
        "OpenAlex canlı sayımı gelirse küresel trend eklenir; gelmezse uydurma sayı yazılmaz. "
        f"Kaynak: {summary['source']}",
        accent="#00C2FF",
    )

    st.markdown(
        """<div class="glass-card">
<div class="teach-label">DOI, OpenAlex ve atıf ne anlama gelir?</div>
<p style="color:#E2E8F0;font-size:0.92rem;line-height:1.65;margin:8px 0 0 0;">
<strong>DOI (Digital Object Identifier — dijital nesne tanımlayıcı):</strong>
makaleye kalıcı kimlik verir; karttaki «Kaynakta Aç» bu kimliği çözümler.
Uydurma DOI üretmek bu platformda yasaktır.
</p>
<p style="color:#CBD5E1;font-size:0.88rem;line-height:1.6;margin:10px 0 0 0;">
<strong>OpenAlex:</strong> açık akademik graf API’sidir. Yıl/kurum/ülke sayıları bu API’den gelir;
erişilemezse grafik gizlenir, statik tablo uydurulmaz.
<strong>Atıf sayısı</strong> (<em>cited_by_count</em>) bir makalenin kaç kez referans verildiğidir —
kalite notu değildir; yeni makale düşük, tarama makalesi yüksek olabilir.
Google Scholar ayrı bir API sunmaz; sayılar OpenAlex’tendir.
</p>
</div>""",
        unsafe_allow_html=True,
    )

    if not papers:
        show_empty("Doğrulanmış makale kaydı bulunamadı.")
        return

    year_label = summary.get("latest_year") or "—"
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Doğrulanmış makale (DOI)", str(summary["verified_paper_count"]))
    with c2:
        val = f"{summary['total_latest_year']:,}" if summary.get("total_latest_year") is not None else "—"
        st.metric(f"OpenAlex {year_label} (6 konu)", val)
    with c3:
        topic_delta = f"{summary['top_topic_count']:,}" if summary.get("top_topic_count") else None
        st.metric("En aktif OpenAlex konusu", summary["top_topic"], topic_delta)
    with c4:
        cites = summary.get("top_paper_citations")
        st.metric("En yüksek atıf (OpenAlex)", f"{cites:,}" if isinstance(cites, int) else "—")

    render_source_button(summary.get("openalex_url") or "https://openalex.org/works", "OpenAlex kaynak sayfasını aç ↗")
    if summary.get("snapshot_at"):
        st.caption(f"Son başarılı OpenAlex önbelleği: {summary['snapshot_at']}")

    st.divider()

    pub_sections = [
        "Doğrulanmış set (DOI)",
        "OpenAlex yıl trendi",
        "Kurumlar",
        "Ülkeler",
        "Makaleler",
    ]
    section = select_section("Yayın görünümü", pub_sections, key="academic_section")

    if section == "Doğrulanmış set (DOI)":
        st.markdown("### DOI ile doğrulanmış 6G makaleleri")
        st.caption(
            "Çubuklar yalnızca platformda listelenen makalelerin yayın yılı ve konusudur. "
            "Her karttaki buton makaleyi DOI üzerinden açar."
        )
        year_counts = AcademicService.get_verified_year_counts()
        topic_counts = AcademicService.get_verified_topic_counts()
        db_dist = AcademicService.get_database_distribution()
        col_y, col_t = st.columns(2)
        with col_y:
            if year_counts:
                show_plotly(
                    render_academic_database_chart(year_counts, "Doğrulanmış set — yayın yılı", "Takvim yılı")
                )
            else:
                show_empty("Yıl dağılımı yok.")
        with col_t:
            if topic_counts:
                show_plotly(
                    render_academic_bar_chart(
                        [{"name": k, "count": v} for k, v in topic_counts.items()],
                        "Doğrulanmış set — konu",
                    )
                )
        if db_dist:
            show_plotly(render_academic_database_chart(db_dist, "Doğrulanmış set — yayıncı"))

    elif section == "OpenAlex yıl trendi":
        st.markdown("### 6G konularına göre yayın sayıları (OpenAlex)")
        st.caption(
            "Sayılar OpenAlex aramasındandır. API veya önbellek yoksa grafik çizilmez; "
            "statik küresel sayı uydurulmaz."
        )
        df_acad = AcademicService.get_tech_publication_trends_df()
        if df_acad is None or df_acad.empty:
            show_empty(
                "OpenAlex şu an canlı yanıt vermedi ve disk önbelleği de boş. "
                "Yukarıdaki DOI doğrulamalı set kullanılabilir. "
                "OpenAlex düzelince trend otomatik dolar."
            )
            render_source_button("https://openalex.org/works", "OpenAlex’i tarayıcıda dene ↗")
        else:
            show_plotly(render_academic_trends_chart(df_acad))
            render_source_button("https://openalex.org/works", "Bu sayıları OpenAlex’te aç ↗")

    elif section == "Kurumlar":
        st.markdown("### En çok yayın yapan kurumlar")
        institutions = AcademicService.get_top_institutions()
        if institutions:
            st.caption("OpenAlex group_by — 2020–2025, 6G konu araması.")
            show_plotly(render_academic_bar_chart(institutions, "Kurumlara göre yayın (OpenAlex)"))
            render_source_button("https://openalex.org/works", "OpenAlex kurum filtresini aç ↗")
        else:
            verified_inst = AcademicService.get_verified_institutions()
            if verified_inst:
                st.caption("Canlı küresel sayım yok. Aşağıdaki liste yalnızca DOI setindeki OpenAlex yazar kurumlarıdır.")
                show_plotly(render_academic_bar_chart(verified_inst, "Doğrulanmış 8 makale — yazar kurumları"))
            else:
                show_empty("Kurum listesi için OpenAlex yanıtı yok. Makale kartlarındaki DOI butonunu kullanın.")

    elif section == "Ülkeler":
        st.markdown("### En çok yayın yapan ülkeler")
        countries = AcademicService.get_top_countries()
        if countries:
            st.caption("OpenAlex group_by — 2020–2025, 6G konu araması.")
            show_plotly(render_academic_bar_chart(countries, "Ülkelere göre yayın (OpenAlex)"))
            render_source_button("https://openalex.org/works", "OpenAlex ülke filtresini aç ↗")
        else:
            verified_cc = AcademicService.get_verified_countries()
            if verified_cc:
                st.caption("Canlı küresel sayım yok. Aşağıdaki liste yalnızca DOI setindeki OpenAlex ülke kodlarıdır.")
                show_plotly(render_academic_bar_chart(verified_cc, "Doğrulanmış 8 makale — ülke kodları"))
            else:
                show_empty("Ülke listesi için OpenAlex yanıtı yok. Makale kartlarındaki DOI butonunu kullanın.")

    else:
        st.markdown("### Doğrulanmış 6G makaleleri")
        st.caption("Atıf sayısı OpenAlex’ten gelirse gösterilir; gelmezse «—». Her kayıt DOI ile açılır.")
        for paper in papers:
            render_paper_card(paper)
