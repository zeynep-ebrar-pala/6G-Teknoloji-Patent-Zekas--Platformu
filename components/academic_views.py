"""
Modül 3 — Akademik Yayın Analizi arayüzü.
Makaleler DOI üzerinden tarayıcıda açılabilir; trend/kurum/ülke OpenAlex'ten canlı alınır.
"""

import streamlit as st

from backend.academic_service import AcademicService
from components.charts import (
    render_academic_bar_chart,
    render_academic_database_chart,
    render_academic_trends_chart,
)
from components.ui_helpers import render_module_header, render_paper_card, show_empty, show_error


def render_academic_publication_module():
    summary = AcademicService.get_summary()
    papers = AcademicService.get_most_cited_papers()

    render_module_header(
        "Yayın Trendleri",
        "6G konularındaki yayın trendleri, kurum ve ülke dağılımı — "
        "OpenAlex canlı sayım (IEEE / Springer / Elsevier / Google Scholar indeksli literatürü kapsar). "
        "Makale kartları DOI ile doğrulanır. "
        f"Veri kaynağı: {summary['source']}",
        accent="#00C2FF",
    )

    if not papers:
        show_empty("Doğrulanmış makale kaydı bulunamadı.")
        return

    year_label = summary.get("latest_year") or "—"
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        val = f"{summary['total_latest_year']:,}" if summary.get("total_latest_year") is not None else "—"
        st.metric(f"{year_label} Toplam (6 konu, OpenAlex)", val)
    with c2:
        topic_delta = f"{summary['top_topic_count']:,}" if summary.get("top_topic_count") else None
        st.metric(f"En Aktif Konu ({year_label})", summary["top_topic"], topic_delta)
    with c3:
        st.metric("Doğrulanmış Makale", summary["verified_paper_count"], "DOI ile")
    with c4:
        cites = summary.get("top_paper_citations")
        st.metric("En Yüksek Atıf (OpenAlex)", f"{cites:,}" if isinstance(cites, int) else "—")

    st.divider()

    tab_pub_trends, tab_inst, tab_country, tab_sources, tab_cited = st.tabs([
        "Yıllara Göre Yayın",
        "En Çok Yayın Yapan Kurumlar",
        "En Çok Yayın Yapan Ülkeler",
        "Kaynak Dağılımı",
        "En Çok Atıf Alan Makaleler",
    ])

    with tab_pub_trends:
        st.markdown("### 6G Konularına Göre Yayın Sayıları")
        st.caption(
            "Sayılar OpenAlex tam metin aramasından canlı alınır. "
            "Arama terimleri backend/openalex_client.py içinde belgelenmiştir. "
            "Google Scholar ayrı bir API sunmaz; OpenAlex GS indeksli literatürü de kapsar."
        )
        df_acad = AcademicService.get_tech_publication_trends_df()
        if df_acad is None or df_acad.empty:
            show_error(
                "OpenAlex API şu an yanıt vermiyor veya rate limit uygulandı. "
                "Trend grafiği gösterilmiyor — statik sayı kullanılmaz."
            )
        else:
            fig_acad = render_academic_trends_chart(df_acad)
            st.plotly_chart(fig_acad, use_container_width=True)

    with tab_inst:
        st.markdown("### En Çok Yayın Yapan Kurumlar")
        st.caption("OpenAlex group_by=authorships.institutions.id — 2020–2025, 6G konu araması.")
        institutions = AcademicService.get_top_institutions()
        if not institutions:
            show_error("Kurum listesi alınamadı. OpenAlex yanıt vermiyor; statik tablo gösterilmez.")
        else:
            st.plotly_chart(
                render_academic_bar_chart(institutions, "Kurumlara Göre Yayın Sayısı (OpenAlex)"),
                use_container_width=True,
            )

    with tab_country:
        st.markdown("### En Çok Yayın Yapan Ülkeler")
        st.caption("OpenAlex group_by=authorships.institutions.country_code — 2020–2025, 6G konu araması.")
        countries = AcademicService.get_top_countries()
        if not countries:
            show_error("Ülke listesi alınamadı. OpenAlex yanıt vermiyor; statik tablo gösterilmez.")
        else:
            st.plotly_chart(
                render_academic_bar_chart(countries, "Ülkelere Göre Yayın Sayısı (OpenAlex)"),
                use_container_width=True,
            )

    with tab_sources:
        st.markdown("### Doğrulanmış Makale Seti — Yayıncı Dağılımı")
        st.caption(
            f"Grafik yalnızca modülde listelenen {summary['verified_paper_count']} "
            "DOI-doğrulamalı makalenin kaynak dağılımını gösterir (IEEE Xplore, Springer, Elsevier)."
        )
        db_dist = AcademicService.get_database_distribution()
        if not db_dist:
            show_empty("Kaynak dağılımı hesaplanamadı.")
        else:
            fig_db = render_academic_database_chart(db_dist)
            st.plotly_chart(fig_db, use_container_width=True)

    with tab_cited:
        st.markdown("### En Çok Atıf Alan Doğrulanmış 6G Makaleleri")
        st.caption("Atıf sayıları OpenAlex cited_by_count alanındandır. API yoksa «—» gösterilir; yerel sayı uydurulmaz.")
        for paper in papers:
            render_paper_card(paper)
