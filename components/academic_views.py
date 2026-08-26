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
    render_eu_mno_leader_chart,
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


def _country_list_items(rows: list, turkey: dict | None = None, *, region: str = "both") -> list:
    items = _as_bar_rows("countries", rows)
    if region != "both" or not items or _turkey_in_top(rows):
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


def _country_rank_table(rows: list, turkey: dict | None = None, *, region: str = "both") -> list:
    table = []
    for i, row in enumerate(rows[:10], 1):
        table.append(
            {
                t("pub.cc_col_rank"): str(i),
                t("pub.cc_col_country"): _country_label(row),
                t("pub.cc_col_count"): _fmt(int(row["count"])),
            }
        )
    if region != "both" or not rows or _turkey_in_top(rows):
        return table
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


def _region_country_rows(bundle: dict) -> list:
    rows = list(bundle.get("countries") or [])
    if rows:
        return rows
    seen: dict = {}
    for group in (bundle.get("countries_by_topic") or {}).values():
        for row in group or []:
            cc = str(row.get("cc") or "")
            if cc and cc not in seen:
                seen[cc] = row
    return list(seen.values())


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


def _render_breakdown(kind: str, topic: str | None, bundle: dict, region: str = "both") -> None:
    from backend.springer_live import TOPIC_ORDER
    from components.ui_helpers import show_empty, show_plotly

    cap_one = t("pub.cc_caption") if kind == "countries" else t("pub.inst_caption")
    if region == "tr":
        cap_one = t("pub.cc_caption_tr") if kind == "countries" else t("pub.inst_caption_tr")
    elif region == "eu":
        cap_one = t("pub.cc_caption_eu") if kind == "countries" else t("pub.inst_caption_eu")
    cap_all = t("pub.cc_caption_all") if kind == "countries" else t("pub.inst_caption_all")
    title_one = t("pub.chart_cc") if kind == "countries" else t("pub.chart_inst")
    empty = t("pub.empty_cc") if kind == "countries" else t("pub.empty_inst")
    turkey_map = bundle.get("turkey_by_topic") or {}

    if topic:
        raw = bundle.get("countries" if kind == "countries" else "institutions") or []
        turkey = bundle.get("turkey") or {}
        st.caption(cap_one)
        rows = _country_list_items(raw, turkey, region=region) if kind == "countries" else _as_bar_rows(kind, raw)
        if not rows:
            show_empty(empty)
            return
        if kind == "countries":
            show_plotly(render_country_rank_chart(rows, f"{title_one} — {topic}"))
            table = _country_rank_table(raw, turkey, region=region)
            if table:
                st.caption(t("pub.cc_rank_caption"))
                st.dataframe(table, hide_index=True, use_container_width=True)
        else:
            show_plotly(render_academic_bar_chart(rows, f"{title_one} — {topic}"))
        return

    st.caption(cap_all if region == "both" else cap_one)
    by_topic = bundle.get("countries_by_topic" if kind == "countries" else "institutions_by_topic") or {}
    drawn = False
    for name in TOPIC_ORDER:
        raw = by_topic.get(name) or []
        turkey = turkey_map.get(name) or {}
        rows = _country_list_items(raw, turkey, region=region) if kind == "countries" else _as_bar_rows(kind, raw)
        if not rows:
            continue
        drawn = True
        st.markdown(f"#### {name}")
        if kind == "countries":
            show_plotly(render_country_rank_chart(rows, f"{title_one} — {name}"))
            table = _country_rank_table(raw, turkey, region=region)
            if table:
                st.dataframe(table, hide_index=True, use_container_width=True)
        else:
            show_plotly(render_academic_bar_chart(rows, f"{title_one} — {name}"))
    if not drawn:
        show_empty(empty)


def _render_region_operators(region: str) -> None:
    from data.eu_operators import countries_for_region

    if region not in ("tr", "eu"):
        return
    rows = countries_for_region(region)
    if not rows:
        return
    st.caption(t("pub.mno_caption"))
    chips = []
    for country in rows:
        ops = ", ".join(str(op.get("name") or "") for op in (country.get("operators") or []) if op.get("name"))
        if not ops:
            continue
        label = country.get("name_tr") if get_lang() == "tr" else country.get("name_en")
        chips.append(f"**{label}:** {ops}")
    if region == "tr":
        st.markdown(" · ".join(chips))
        return
    st.markdown("\n".join(f"- {line}" for line in chips[:8]))


def _mno_ops_line(ops: list) -> str:
    measured = [r for r in ops if isinstance(r.get("n"), int)]
    measured.sort(key=lambda r: (-int(r["n"]), str(r.get("name") or "")))
    bits = []
    for i, row in enumerate(measured, 1):
        bits.append(f"{i}. {row['name']} ({_fmt(int(row['n']))})")
    for row in ops:
        if isinstance(row.get("n"), int):
            continue
        bits.append(f"{row.get('name') or '—'} (—)")
    return " · ".join(bits) if bits else "—"


def _render_eu_mno_panel(topic: str | None) -> None:
    """Avrupa yüzü: ülke başına kilitli 3 MNO (Türkiye dahil) + TT sırası."""
    from backend.config import get_springer_api_key
    from backend.live_refresh import render_watch
    from backend.mno_pub_live import chart_rows, ensure_prefetch, prefetch_status, tt_europe_place
    from components.ui_helpers import current_view_mode, show_empty, show_plotly

    st.markdown(f"### {t('pub.mno_heading')}")
    st.caption(t("pub.mno_body"))
    if current_view_mode() == "expert":
        st.caption(t("pub.mno_body_expert"))
    if not get_springer_api_key():
        show_empty(t("pub.mno_need_key"))
        return
    ensure_prefetch(topic)
    render_watch("mno", "mno_live")
    rows = chart_rows(topic)
    place = tt_europe_place(topic)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(t("pub.metric_eu_tt"), _fmt(place.get("tt_n")))
    with c2:
        rank = place.get("rank")
        field = place.get("field_n")
        if isinstance(rank, int) and isinstance(field, int) and field > 0:
            st.metric(t("pub.metric_eu_tt_rank"), t("pub.metric_eu_tt_rank_n", rank=rank, field=field))
        else:
            st.metric(t("pub.metric_eu_tt_rank"), "—")
    with c3:
        top = rows[0] if rows else None
        if top:
            country = top.get("name_tr") if get_lang() == "tr" else top.get("name_en")
            label = f"{top.get('firm') or '—'} ({country})"
        else:
            label = "—"
        st.metric(t("pub.metric_eu_mno_top"), label)
    if not rows:
        if not prefetch_status().get("running"):
            show_empty(t("pub.mno_empty"))
        return
    show_plotly(render_eu_mno_leader_chart(rows, t("pub.mno_chart_title"), t("pub.mno_chart_x")))
    table = []
    lang = get_lang()
    leaders = place.get("leaders") or []
    by_cc = {str(r.get("cc") or ""): r for r in leaders}
    for row in rows:
        cc = str(row.get("cc") or "")
        country = row.get("name_tr") if lang == "tr" else row.get("name_en")
        hit = by_cc.get(cc)
        ops_line = _mno_ops_line(hit.get("ops") or []) if hit else "—"
        table.append(
            {
                t("pub.mno_col_country"): country,
                t("pub.mno_col_lead"): row.get("firm") or "—",
                t("pub.mno_col_n"): _fmt(row.get("n") if isinstance(row.get("n"), int) else None),
                t("pub.mno_col_three"): ops_line,
            }
        )
    st.caption(t("pub.mno_table_caption"))
    three = t("pub.mno_col_three")
    st.dataframe(
        table,
        hide_index=True,
        width="stretch",
        column_config={three: st.column_config.TextColumn(three, width="large")},
    )


def render_academic_publication_module():
    from backend.live_refresh import render_watch
    from backend.springer_live import TOPIC_ORDER, ensure_prefetch
    from backend.years import trend_years
    from components.topic_panels import render_pub_topic_panel
    from components.tt_europe_views import render_tt_europe_pub_section
    from components.ui_helpers import (
        current_view_mode,
        render_link_row,
        render_module_header,
        render_paper_card,
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

    ensure_prefetch()
    render_watch("springer", "pub")
    topic, region = render_pub_topic_panel("pub")
    _labels = [t(f"pub.section.{k}") for k in PUB_SECTION_KEYS]
    _map = dict(zip(_labels, PUB_SECTION_KEYS))
    section = _map.get(
        select_section(t("pub.view"), _labels, key=f"academic_section_story_{get_lang()}"),
        PUB_SECTION_KEYS[0],
    )
    if region == "tr":
        _render_region_operators(region)

    bundle = AcademicService.get_bundle(region, topic)
    fetched = str(bundle.get("fetched_at") or "")
    if fetched:
        st.caption(t("app.live_cached", ts=fetched))

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(t("pub.metric_springer"), _fmt(bundle.get("total")))
    with c2:
        if region == "eu":
            eu_rows = _region_country_rows(bundle)
            st.metric(t("pub.metric_eu_n"), _fmt(len(eu_rows) if eu_rows else None))
        else:
            rank_val, _rank_delta = _tr_rank_metric(topic, bundle)
            st.metric(t("pub.metric_tr_rank"), rank_val)
    with c3:
        if region == "eu":
            rows = _region_country_rows(bundle)
            top = rows[0] if rows else None
            label = _country_label(top) if top else "—"
            st.metric(t("pub.metric_eu_top"), label)
        else:
            info = _turkey_info(bundle, topic)
            st.metric(
                t("pub.metric_tr_count"),
                _fmt(info.get("count") if isinstance(info.get("count"), int) else None),
            )

    from backend.source_links import topic_pub_searches

    render_link_row(
        topic_pub_searches(topic or "6G", region),
        key_suffix=f"pub_src_{region}_{topic or 'all'}",
    )

    if region == "eu":
        _render_eu_mno_panel(topic)

    if section == "tt_eu":
        render_tt_europe_pub_section(topic)
        return

    def _trend_fig():
        df = AcademicService.get_trend_df(region, topic)
        if df is None or df.empty:
            return None
        return render_academic_trends_chart(df, t("pub.chart_trend"))

    if section == "year":
        st.caption(t("pub.year_caption") if region == "both" else t("pub.year_caption_region"))
        years = bundle.get("year_counts") or {}
        years = {str(y): int(years.get(str(y), 0) or 0) for y in trend_years()}
        shown = False
        if any(years.values()):
            show_plotly(render_academic_database_chart(years, t("pub.chart_year"), t("pub.chart_year_x")))
            shown = True
        else:
            fig = _trend_fig()
            if fig is not None:
                show_plotly(fig)
                shown = True
        topics = bundle.get("topics") or {}
        if topics:
            show_plotly(
                render_academic_bar_chart(
                    [{"name": k, "count": v} for k, v in topics.items() if k in TOPIC_ORDER],
                    t("pub.chart_topic"),
                )
            )
            shown = True
        if not shown:
            show_empty(t("pub.empty_year_region") if region != "both" else t("pub.empty_year"))

    elif section == "inst":
        _render_breakdown("institutions", topic, bundle, region)

    elif section == "country":
        _render_breakdown("countries", topic, bundle, region)

    elif section == "cited":
        st.caption(t("pub.cited_caption") if region == "both" else t("pub.cited_caption_region"))
        papers = bundle.get("cited") or []
        if not papers:
            show_empty(t("pub.empty_cited_region") if region != "both" else t("pub.empty_cited"))
        else:
            for paper in papers:
                render_paper_card(_with_source(paper))

    else:
        st.caption(t("pub.trend_caption") if region == "both" else t("pub.year_caption_region"))
        fig = _trend_fig()
        if fig is not None:
            show_plotly(fig)
        else:
            show_empty(t("pub.empty_year_region") if region != "both" else t("pub.empty_year"))
