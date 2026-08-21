"""
Modül 3 — Akademik Yayın Analizi.
Yedi 6G konusu, Springer Nature Meta API: yıl, kurum, ülke, atıf, trend.
"""

from __future__ import annotations

import streamlit as st

from backend.academic_service import AcademicService
from i18n.core import format_int, get_lang, t
from components.charts import (
    render_academic_bar_chart,
    render_academic_database_chart,
    render_academic_trends_chart,
    render_country_rank_chart,
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
    out["source"] = "Springer"
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
    return any(str(r.get("cc") or "") == "TR" for r in rows[:10])


def _turkey_rank(rows: list) -> int | None:
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


def _country_list_items(rows: list, turkey: dict | None = None) -> list:
    items = _as_bar_rows("countries", rows)
    if not items or _turkey_in_top(rows):
        return items
    items.append({"name": t("pub.cc_ellipsis"), "count": None, "gap": True})
    info = turkey or {}
    rank = info.get("rank") if isinstance(info.get("rank"), int) else None
    count = info.get("count") if isinstance(info.get("count"), int) else None
    if isinstance(count, int):
        label = t("pub.cc_tr_list_label_n", n=rank) if rank else t("pub.cc_tr_list_label")
        items.append({"name": label, "count": count, "cc": "TR"})
        return items
    items.append({"name": t("pub.cc_tr_list_label"), "count": None, "cc": "TR", "out": True})
    return items


def _country_rank_table(rows: list, turkey: dict | None = None) -> list:
    table = []
    for i, row in enumerate(rows[:10], 1):
        table.append(
            {
                t("pub.cc_col_rank"): str(i),
                t("pub.cc_col_country"): _country_label(row),
                t("pub.cc_col_count"): _fmt(int(row["count"])),
            }
        )
    if rows and not _turkey_in_top(rows):
        table.append(
            {
                t("pub.cc_col_rank"): t("pub.cc_ellipsis"),
                t("pub.cc_col_country"): t("pub.cc_ellipsis"),
                t("pub.cc_col_count"): t("pub.cc_ellipsis"),
            }
        )
        info = turkey or {}
        rank = info.get("rank") if isinstance(info.get("rank"), int) else None
        count = info.get("count") if isinstance(info.get("count"), int) else None
        table.append(
            {
                t("pub.cc_col_rank"): str(rank) if rank else t("pub.cc_tr_rank_gt10"),
                t("pub.cc_col_country"): _cc_name("TR"),
                t("pub.cc_col_count"): _fmt(count) if isinstance(count, int) else t("pub.cc_tr_not_measured"),
            }
        )
    return table


def _turkey_info(bundle: dict, topic: str | None) -> dict:
    if topic:
        return bundle.get("turkey") or (bundle.get("turkey_by_topic") or {}).get(topic) or {}
    return {}


def _tr_rank_metric(topic: str | None, bundle: dict) -> tuple[str, str | None]:
    from backend.springer_live import TOPIC_ORDER

    turkey_map = bundle.get("turkey_by_topic") or {}
    if topic:
        info = _turkey_info(bundle, topic)
        rank = info.get("rank") if isinstance(info.get("rank"), int) else _turkey_rank(bundle.get("countries") or [])
        count = info.get("count") if isinstance(info.get("count"), int) else None
        if rank:
            return t("pub.metric_tr_rank_n", n=rank), (
                t("pub.metric_peak_delta", n=_fmt(count)) if isinstance(count, int) else None
            )
        tenth = _tenth_count(bundle.get("countries") or [])
        delta = t("pub.metric_tr_out_delta", tenth=_fmt(tenth)) if tenth is not None else None
        return t("pub.metric_tr_out"), delta
    measured = [name for name in TOPIC_ORDER if isinstance((turkey_map.get(name) or {}).get("rank"), int)]
    if measured:
        return f"{len(measured)} / {len(TOPIC_ORDER)}", t("pub.metric_tr_all_live")
    return "—", None


def _render_breakdown(kind: str, topic: str | None, bundle: dict) -> None:
    from backend.springer_live import TOPIC_ORDER
    from components.ui_helpers import show_empty, show_plotly

    cap_one = t("pub.cc_caption") if kind == "countries" else t("pub.inst_caption")
    cap_all = t("pub.cc_caption_all") if kind == "countries" else t("pub.inst_caption_all")
    title_one = t("pub.chart_cc") if kind == "countries" else t("pub.chart_inst")
    empty = t("pub.empty_cc") if kind == "countries" else t("pub.empty_inst")
    turkey_map = bundle.get("turkey_by_topic") or {}

    if topic:
        raw = bundle.get("countries" if kind == "countries" else "institutions") or []
        turkey = bundle.get("turkey") or {}
        st.caption(cap_one)
        rows = _country_list_items(raw, turkey) if kind == "countries" else _as_bar_rows(kind, raw)
        if not rows:
            show_empty(empty)
            return
        if kind == "countries":
            show_plotly(render_country_rank_chart(rows, f"{title_one} — {topic}"))
            table = _country_rank_table(raw, turkey)
            if table:
                st.caption(t("pub.cc_rank_caption"))
                st.dataframe(table, hide_index=True, use_container_width=True)
        else:
            show_plotly(render_academic_bar_chart(rows, f"{title_one} — {topic}"))
        return

    st.caption(cap_all)
    by_topic = bundle.get("countries_by_topic" if kind == "countries" else "institutions_by_topic") or {}
    drawn = False
    for name in TOPIC_ORDER:
        raw = by_topic.get(name) or []
        turkey = turkey_map.get(name) or {}
        rows = _country_list_items(raw, turkey) if kind == "countries" else _as_bar_rows(kind, raw)
        if not rows:
            continue
        drawn = True
        st.markdown(f"#### {name}")
        if kind == "countries":
            show_plotly(render_country_rank_chart(rows, f"{title_one} — {name}"))
            table = _country_rank_table(raw, turkey)
            if table:
                st.dataframe(table, hide_index=True, use_container_width=True)
        else:
            show_plotly(render_academic_bar_chart(rows, f"{title_one} — {name}"))
    if not drawn:
        show_empty(empty)


def render_academic_publication_module():
    from backend.springer_live import TOPIC_ORDER, TREND_YEARS, ensure_prefetch, prefetch_status
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
    ensure_prefetch()
    topic, region = render_pub_topic_panel("pub")
    bundle = AcademicService.get_bundle(region, topic)
    status = prefetch_status()
    if status.get("running") and int(status.get("total") or 0) > 0:
        done = min(int(status.get("done") or 0), int(status["total"]))
        st.info(t("pub.bg_wait", done=format_int(done), total=format_int(status["total"])))
        st.progress(done / max(int(status["total"]), 1))
    if status.get("error"):
        st.warning(t("pub.api_error", detail=str(status["error"]).replace("{", "(").replace("}", ")")))

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(t("pub.metric_springer"), _fmt(bundle.get("total") if topic else None))
    with c2:
        rank_val, rank_delta = _tr_rank_metric(topic, bundle)
        st.metric(t("pub.metric_tr_rank"), rank_val, rank_delta)
    with c3:
        years = bundle.get("year_counts") or {}
        years = {str(y): int(years.get(str(y), 0) or 0) for y in TREND_YEARS if int(years.get(str(y), 0) or 0)}
        if years:
            peak = max(years, key=lambda y: years[y])
            st.metric(t("pub.metric_peak_year"), peak, t("pub.metric_peak_delta", n=_fmt(years[peak])))
        else:
            st.metric(t("pub.metric_peak_year"), "—")
    with c4:
        info = _turkey_info(bundle, topic)
        st.metric(t("pub.metric_tr_count"), _fmt(info.get("count") if isinstance(info.get("count"), int) else None))
    st.caption(t("pub.source_metric_caption"))
    if bundle.get("fetched_at"):
        st.caption(t("pub.snapshot", ts=bundle["fetched_at"]))

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
        return render_academic_trends_chart(df, t("pub.chart_trend"))

    if section == "year":
        st.markdown(t("pub.year_heading"))
        st.caption(t("pub.year_caption"))
        years = bundle.get("year_counts") or {}
        years = {str(y): int(years.get(str(y), 0) or 0) for y in TREND_YEARS}
        if any(years.values()):
            show_plotly(render_academic_database_chart(years, t("pub.chart_year"), t("pub.chart_year_x")))
        else:
            fig = _trend_fig()
            if fig is not None:
                show_plotly(fig)
            else:
                show_empty(t("pub.empty_year"))
        topics = bundle.get("topics") or {}
        if topics:
            show_plotly(
                render_academic_bar_chart(
                    [{"name": k, "count": v} for k, v in topics.items() if k in TOPIC_ORDER],
                    t("pub.chart_topic"),
                )
            )

    elif section == "inst":
        st.markdown(t("pub.inst_heading"))
        _render_breakdown("institutions", topic, bundle)

    elif section == "country":
        st.markdown(t("pub.cc_heading"))
        _render_breakdown("countries", topic, bundle)

    elif section == "cited":
        st.markdown(t("pub.cited_heading"))
        st.caption(t("pub.cited_caption"))
        papers = bundle.get("cited") or []
        if not papers:
            show_empty(t("pub.empty_cited"))
        else:
            for paper in papers:
                render_paper_card(_with_source(paper))

    else:
        st.markdown(t("pub.trend_heading"))
        st.caption(t("pub.trend_caption"))
        fig = _trend_fig()
        if fig is not None:
            show_plotly(fig)
        else:
            show_empty(t("pub.empty_year"))
        render_link_row(
            topic_pub_searches(topic or "6G", region),
            key_suffix=f"pub_tr_{region}_{topic or 'all'}",
        )
