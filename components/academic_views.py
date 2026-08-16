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
from components.ui_helpers import render_module_header, render_paper_card, render_source_button, show_empty


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

    tab_verified, tab_openalex, tab_inst, tab_country, tab_cited = st.tabs([
        "Doğrulanmış set (DOI)",
        "OpenAlex yıl trendi",
        "Kurumlar",
        "Ülkeler",
        "Makaleler",
    ])

    with tab_verified:
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
                st.plotly_chart(
                    render_academic_database_chart(year_counts, "Doğrulanmış set — yayın yılı", "Takvim yılı"),
                    use_container_width=True,
                )
            else:
                show_empty("Yıl dağılımı yok.")
        with col_t:
            if topic_counts:
                st.plotly_chart(
                    render_academic_bar_chart(
                        [{"name": k, "count": v} for k, v in topic_counts.items()],
                        "Doğrulanmış set — konu",
                    ),
                    use_container_width=True,
                )
        if db_dist:
            st.plotly_chart(render_academic_database_chart(db_dist, "Doğrulanmış set — yayıncı"), use_container_width=True)

    with tab_openalex:
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
            st.plotly_chart(render_academic_trends_chart(df_acad), use_container_width=True)
            render_source_button("https://openalex.org/works", "Bu sayıları OpenAlex’te aç ↗")

    with tab_inst:
        st.markdown("### En çok yayın yapan kurumlar")
        institutions = AcademicService.get_top_institutions()
        if institutions:
            st.caption("OpenAlex group_by — 2020–2025, 6G konu araması.")
            st.plotly_chart(
                render_academic_bar_chart(institutions, "Kurumlara göre yayın (OpenAlex)"),
                use_container_width=True,
            )
            render_source_button("https://openalex.org/works", "OpenAlex kurum filtresini aç ↗")
        else:
            verified_inst = AcademicService.get_verified_institutions()
            if verified_inst:
                st.caption("Canlı küresel sayım yok. Aşağıdaki liste yalnızca DOI setindeki OpenAlex yazar kurumlarıdır.")
                st.plotly_chart(
                    render_academic_bar_chart(verified_inst, "Doğrulanmış 8 makale — yazar kurumları"),
                    use_container_width=True,
                )
            else:
                show_empty("Kurum listesi için OpenAlex yanıtı yok. Makale kartlarındaki DOI butonunu kullanın.")

    with tab_country:
        st.markdown("### En çok yayın yapan ülkeler")
        countries = AcademicService.get_top_countries()
        if countries:
            st.caption("OpenAlex group_by — 2020–2025, 6G konu araması.")
            st.plotly_chart(
                render_academic_bar_chart(countries, "Ülkelere göre yayın (OpenAlex)"),
                use_container_width=True,
            )
            render_source_button("https://openalex.org/works", "OpenAlex ülke filtresini aç ↗")
        else:
            verified_cc = AcademicService.get_verified_countries()
            if verified_cc:
                st.caption("Canlı küresel sayım yok. Aşağıdaki liste yalnızca DOI setindeki OpenAlex ülke kodlarıdır.")
                st.plotly_chart(
                    render_academic_bar_chart(verified_cc, "Doğrulanmış 8 makale — ülke kodları"),
                    use_container_width=True,
                )
            else:
                show_empty("Ülke listesi için OpenAlex yanıtı yok. Makale kartlarındaki DOI butonunu kullanın.")

    with tab_cited:
        st.markdown("### Doğrulanmış 6G makaleleri")
        st.caption("Atıf sayısı OpenAlex’ten gelirse gösterilir; gelmezse «—». Her kayıt DOI ile açılır.")
        for paper in papers:
            render_paper_card(paper)
