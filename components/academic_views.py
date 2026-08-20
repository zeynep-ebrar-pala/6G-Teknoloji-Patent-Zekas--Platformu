"""
Modül 3 — Akademik Yayın Analizi.
Türkiye ve Avrupa 6G literatürü: yıl, kurum, ülke, atıf, trend.
Kilitli örnek liste yok. WoS / Springer sayısı uydurulmaz.
"""

from __future__ import annotations

import streamlit as st

from backend.academic_service import AcademicService
from i18n.core import format_int, get_lang, t
from components.charts import (
    render_academic_bar_chart,
    render_academic_database_chart,
    render_academic_trends_chart,
    render_wos_springer_totals_chart,
)

PUB_SECTION_KEYS = ["year", "inst", "country", "cited", "trend", "tt_eu"]


def _fmt(n) -> str:
    return format_int(n) if isinstance(n, int) else "—"


def _cc_name(cc: str) -> str:
    key = f"pub.cc.{cc}"
    label = t(key)
    return cc if label == key else label


def _with_source(paper: dict) -> dict:
    out = dict(paper)
    prefix = str(out.get("prefix") or "")
    src = str(out.get("source") or "")
    if src in ("IEEE Xplore", "Elsevier", "Google Scholar"):
        out["source"] = ""
    if prefix.startswith("10.1007") or "springer" in src.lower():
        out["source"] = "Springer"
    elif not out.get("source"):
        out["source"] = "WoS"
    return out


def _country_label(row: dict) -> str:
    cc = str(row.get("cc") or "")
    if cc:
        return _cc_name(cc)
    return str(row.get("name") or "")


def _as_bar_rows(kind: str, rows: list) -> list:
    ranked = []
    for i, row in enumerate(rows[:10], 1):
        if kind == "countries":
            label = f"{i}. {_country_label(row)}"
        else:
            label = f"{i}. {row['name']}"
        ranked.append({"name": label, "count": int(row["count"]), "cc": row.get("cc")})
    return ranked


def _turkey_in_top(rows: list) -> bool:
    return any(str(r.get("cc") or "") == "TR" for r in rows)


def _turkey_wos_rank(rows: list) -> int | None:
    for i, row in enumerate(rows[:10], 1):
        if str(row.get("cc") or "") == "TR":
            return i
    return None


def _tenth_count(rows: list) -> int | None:
    if len(rows) < 10:
        return None
    try:
        return int(rows[9]["count"])
    except (TypeError, ValueError, KeyError):
        return None


def _country_rank_table(wos_rows: list) -> list:
    table = []
    for i, row in enumerate(wos_rows[:10], 1):
        table.append(
            {
                t("pub.cc_col_rank"): str(i),
                t("pub.cc_col_country"): _country_label(row),
                t("pub.cc_col_count"): _fmt(int(row["count"])),
            }
        )
    if wos_rows and not _turkey_in_top(wos_rows):
        table.append(
            {
                t("pub.cc_col_rank"): t("pub.cc_tr_rank_gt10"),
                t("pub.cc_col_country"): _cc_name("TR"),
                t("pub.cc_col_count"): t("pub.cc_tr_not_measured"),
            }
        )
    return table


def _turkey_overview_table() -> list:
    from backend.publisher_apis import fetch_springer_turkey_topics, key_fingerprint
    from backend.wos_topic_cache import TOPIC_ORDER, wos_overlay

    springer = fetch_springer_turkey_topics(key_fingerprint())
    by_cc = (wos_overlay(None) or {}).get("countries_by_topic") or {}
    rows = []
    for name in TOPIC_ORDER:
        raw = by_cc.get(name) or []
        rank = _turkey_wos_rank(raw)
        n = springer.get(name)
        rows.append(
            {
                t("pub.cc_col_topic"): name,
                t("pub.cc_col_tr_rank"): (
                    t("pub.metric_tr_wos_rank_n", n=rank) if rank else t("pub.metric_tr_wos_out")
                ),
                t("pub.cc_col_tenth"): _fmt(_tenth_count(raw)),
                t("pub.cc_col_springer"): _fmt(n if isinstance(n, int) else None),
            }
        )
    return rows


def _tr_rank_metric(topic: str | None, bundle: dict) -> tuple[str, str | None]:
    from backend.wos_topic_cache import TOPIC_ORDER

    if topic:
        rows = bundle.get("countries") or []
        rank = _turkey_wos_rank(rows)
        if rank:
            return t("pub.metric_tr_wos_rank_n", n=rank), None
        tenth = _tenth_count(rows)
        delta = t("pub.metric_tr_wos_out_delta", tenth=_fmt(tenth)) if tenth is not None else None
        return t("pub.metric_tr_wos_out"), delta
    by_topic = bundle.get("countries_by_topic") or {}
    hits = sum(1 for name in TOPIC_ORDER if _turkey_in_top(by_topic.get(name) or []))
    return f"{hits} / {len(TOPIC_ORDER)}", t("pub.metric_tr_wos_all_delta")


def _render_turkey_note(topic: str | None, wos_rows: list) -> None:
    from backend.publisher_apis import fetch_springer_turkey_topics, key_fingerprint
    from i18n.core import format_int

    springer = fetch_springer_turkey_topics(key_fingerprint())
    in_top = _turkey_in_top(wos_rows)
    tenth = _tenth_count(wos_rows)
    if topic:
        n = springer.get(topic)
        n_txt = format_int(n) if isinstance(n, int) else "—"
        if in_top:
            st.info(t("pub.tr_in_top10", topic=topic, n=n_txt))
        else:
            tenth_txt = format_int(tenth) if isinstance(tenth, int) else "—"
            st.info(t("pub.tr_not_top10", topic=topic, n=n_txt, tenth=tenth_txt))
        return
    bits = []
    for name in ("ISAC", "RIS", "NTN", "AI-RAN", "THz", "Ambient IoT"):
        n = springer.get(name)
        bits.append(f"{name}: {format_int(n) if isinstance(n, int) else '—'}")
    st.info(t("pub.tr_not_top10_all", springer="; ".join(bits)))


def _render_wos_breakdown(kind: str, topic: str | None, wos: bool) -> None:
    """Ülke/kurum: WoS Analyze Results önbelleği. Bundle önbelleğine bağlı değil."""
    from backend.wos_topic_cache import TOPIC_ORDER, wos_overlay
    from components.ui_helpers import show_empty, show_plotly

    overlay = wos_overlay(topic)
    by_key = "countries_by_topic" if kind == "countries" else "institutions_by_topic"
    single_key = "countries" if kind == "countries" else "institutions"
    cap_one = t("pub.cc_caption_wos") if kind == "countries" else t("pub.inst_caption_wos")
    cap_all = t("pub.cc_caption_wos_all") if kind == "countries" else t("pub.inst_caption_wos_all")
    title_one = t("pub.chart_cc_wos") if kind == "countries" else t("pub.chart_inst_wos")
    empty = t("pub.empty_cc_wos") if kind == "countries" else t("pub.empty_inst_wos")
    if not wos:
        cap_one = t("pub.cc_caption") if kind == "countries" else t("pub.inst_caption")
        empty = t("pub.empty_cc") if kind == "countries" else t("pub.empty_inst")

    if not overlay:
        st.caption(cap_one)
        show_empty(empty)
        return

    if topic:
        raw = overlay.get(single_key) or []
        rows = _as_bar_rows(kind, raw)
        st.caption(cap_one)
        if rows:
            show_plotly(render_academic_bar_chart(rows, f"{title_one} — {topic}"))
            if kind == "countries":
                table = _country_rank_table(raw)
                if table:
                    st.caption(t("pub.cc_rank_caption"))
                    st.dataframe(table, hide_index=True, use_container_width=True)
                _render_turkey_note(topic, raw)
        else:
            show_empty(empty)
        return

    by_topic = overlay.get(by_key) or {}
    st.caption(cap_all)
    if kind == "countries":
        overview = _turkey_overview_table()
        if overview:
            st.caption(t("pub.cc_overview_caption"))
            st.dataframe(overview, hide_index=True, use_container_width=True)
    drawn = False
    for name in TOPIC_ORDER:
        raw = by_topic.get(name) or []
        rows = _as_bar_rows(kind, raw)
        if not rows:
            continue
        drawn = True
        st.markdown(f"#### {name}")
        show_plotly(render_academic_bar_chart(rows, f"{title_one} — {name}"))
        if kind == "countries":
            table = _country_rank_table(raw)
            if table:
                st.dataframe(table, hide_index=True, use_container_width=True)
            _render_turkey_note(name, raw)
    if not drawn:
        show_empty(empty)


def _source_total_rows(bundle: dict) -> list:
    from backend.wos_topic_cache import TOPIC_ORDER

    wos = bundle.get("topics") or {}
    springer = bundle.get("springer_topics") or {}
    rows = []
    for name in TOPIC_ORDER:
        w = wos.get(name)
        s = springer.get(name)
        if not isinstance(w, int) and not isinstance(s, int):
            continue
        rows.append(
            {
                "name": name,
                "wos": w if isinstance(w, int) else None,
                "springer": s if isinstance(s, int) else None,
            }
        )
    return rows


def render_academic_publication_module():
    from components.topic_panels import render_pub_topic_panel
    from components.tt_europe_views import render_tt_europe_pub_section
    from components.ui_helpers import (
        current_view_mode,
        render_link_row,
        render_module_header,
        render_paper_card,
        render_spec_pub_sources,
        select_section,
        show_empty,
        show_plotly,
    )

    render_module_header(
        t("pub.title"),
        t("pub.subtitle", source=AcademicService.get_data_source()),
        accent="#00C2FF",
    )

    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("pub.what_title")}</div>
{t("pub.what_body")}
</div>""",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""<div class="glass-card">
<div class="teach-label">{t("pub.access_title")}</div>
{t("pub.access_body")}
</div>""",
        unsafe_allow_html=True,
    )
    if current_view_mode() == "expert":
        st.markdown(
            f"""<div class="glass-card">
<div class="teach-label">{t("pub.expert_title")}</div>
{t("pub.expert_body")}
</div>""",
            unsafe_allow_html=True,
        )

    render_spec_pub_sources()
    topic, region = render_pub_topic_panel("pub")
    bundle = AcademicService.get_bundle(region, topic)
    pubs = bundle.get("publishers") or {}

    c1, c2 = st.columns(2)
    with c1:
        st.metric(t("pub.metric_wos"), _fmt(pubs.get("wos")))
    with c2:
        st.metric(t("pub.metric_springer"), _fmt(pubs.get("springer")))
    st.caption(t("pub.source_metric_caption"))
    if current_view_mode() == "expert":
        from backend.publisher_apis import REGISTER

        k1, k2 = st.columns(2)
        with k1:
            st.link_button(t("pub.key_wos"), REGISTER["wos"])
        with k2:
            st.link_button(t("pub.key_springer"), REGISTER["springer"])

    wos = bundle.get("chart_source") == "wos"
    tr_n = bundle.get("total_tr")
    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        if wos:
            rank_val, rank_delta = _tr_rank_metric(topic, bundle)
            st.metric(t("pub.metric_tr_wos_rank"), rank_val, rank_delta)
        else:
            st.metric(t("pub.metric_tr"), _fmt(tr_n))
    with col_b:
        st.metric(t("pub.metric_wos_core"), _fmt(bundle.get("wos_total")))
    with col_c:
        peak_label = t("pub.metric_peak_year_wos") if wos else t("pub.metric_peak_year")
        from backend.wos_topic_cache import LAST5_YEARS

        years = bundle.get("year_counts") or {}
        years = {str(y): int(years.get(str(y), 0) or 0) for y in LAST5_YEARS if int(years.get(str(y), 0) or 0)}
        if years:
            peak = max(years, key=lambda y: years[y])
            st.metric(peak_label, peak, t("pub.metric_peak_delta", n=_fmt(years[peak])))
        else:
            series = bundle.get("year_series") or {}
            best = None
            for name, yc in series.items():
                if not yc:
                    continue
                last = {str(y): int(yc.get(str(y), 0) or 0) for y in LAST5_YEARS}
                if not any(last.values()):
                    continue
                y = max(last, key=lambda k: last[k])
                cand = (int(last[y]), str(y), str(name))
                if best is None or cand[0] > best[0]:
                    best = cand
            if best:
                st.metric(
                    peak_label,
                    f"{best[1]} · {best[2]}",
                    t("pub.metric_peak_delta", n=_fmt(best[0])),
                )
            else:
                st.metric(peak_label, "—")
    with col_d:
        from backend.publisher_apis import fetch_springer_turkey_topics, key_fingerprint

        tr_sp = fetch_springer_turkey_topics(key_fingerprint())
        if topic:
            n = tr_sp.get(topic)
            st.metric(t("pub.metric_tr_springer"), _fmt(n if isinstance(n, int) else None))
        else:
            st.metric(t("pub.metric_tr_springer"), "—")
        st.caption(t("pub.metric_tr_springer_cap"))
    if wos and bundle.get("wos_fetched_at"):
        st.caption(t("pub.snapshot", ts=bundle["wos_fetched_at"]))

    from backend.source_links import topic_pub_searches

    render_link_row(
        topic_pub_searches(topic or "6G", region),
        key_suffix=f"pub_src_{region}_{topic or 'all'}",
    )

    _labels = [t(f"pub.section.{k}") for k in PUB_SECTION_KEYS]
    _map = dict(zip(_labels, PUB_SECTION_KEYS))
    section = _map.get(
        select_section(t("pub.view"), _labels, key=f"academic_section_story_{get_lang()}"),
        PUB_SECTION_KEYS[0],
    )

    if section == "tt_eu":
        render_tt_europe_pub_section(topic)
        return

    def _trend_fig():
        df = AcademicService.get_trend_df(region, topic)
        if df is None or df.empty:
            return None
        if wos:
            return render_academic_trends_chart(df, t("pub.chart_trend_wos"))
        rename = {c: _cc_name(c) for c in df.columns if c != "Years"}
        return render_academic_trends_chart(df.rename(columns=rename))

    if section == "year":
        st.markdown(t("pub.year_heading"))
        st.caption(t("pub.year_caption_wos") if wos else t("pub.year_caption"))
        from backend.wos_topic_cache import LAST5_YEARS

        years = bundle.get("year_counts") or {}
        years = {str(y): int(years.get(str(y), 0) or 0) for y in LAST5_YEARS}
        year_title = t("pub.chart_year_wos") if wos else t("pub.chart_year")
        if years:
            show_plotly(
                render_academic_database_chart(years, year_title, t("pub.chart_year_x"))
            )
        else:
            fig = _trend_fig()
            if fig is not None:
                show_plotly(fig)
            else:
                show_empty(t("pub.empty_year"))
        topics = bundle.get("topics") or {}
        source_rows = _source_total_rows(bundle)
        if source_rows:
            st.caption(t("pub.wos_springer_caption"))
            show_plotly(
                render_wos_springer_totals_chart(source_rows, t("pub.chart_wos_springer"))
            )
        elif len(topics) > 1:
            show_plotly(
                render_academic_bar_chart(
                    [{"name": k, "count": v} for k, v in topics.items()],
                    t("pub.chart_topic_wos") if wos else t("pub.chart_topic"),
                )
            )

    elif section == "inst":
        st.markdown(t("pub.inst_heading"))
        _render_wos_breakdown("institutions", topic, wos)

    elif section == "country":
        st.markdown(t("pub.cc_heading"))
        _render_wos_breakdown("countries", topic, wos)

    elif section == "cited":
        st.markdown(t("pub.cited_heading"))
        st.caption(t("pub.cited_caption_wos") if wos else t("pub.cited_caption"))
        papers = bundle.get("cited") or []
        if not papers:
            show_empty(t("pub.empty_cited"))
        else:
            for paper in papers:
                render_paper_card(_with_source(paper))

    else:
        st.markdown(t("pub.trend_heading"))
        st.caption(t("pub.trend_caption_wos") if wos else t("pub.trend_caption"))
        fig = _trend_fig()
        if fig is not None:
            show_plotly(fig)
        else:
            show_empty(t("pub.empty_year"))
        render_link_row(
            topic_pub_searches(topic or "6G", region),
            key_suffix=f"pub_trend_{region}_{topic or 'all'}",
        )
