"""
Modül 3 — Akademik Yayın Analizi.
Yedi 6G konusu, Springer Nature Meta API: yıl, ülke, atıf.
"""

from __future__ import annotations

import streamlit as st

from backend.academic_service import AcademicService
from i18n.core import format_int, get_lang, t, topic_label
from components.charts import (
    render_academic_bar_chart,
    render_academic_database_chart,
    render_academic_trends_chart,
    render_country_rank_chart,
    render_eu_mno_leader_chart,
)

PUB_SECTION_KEYS = ["year", "country", "cited", "tt_eu"]


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
    cc = str(row.get("cc") or "").strip()
    if not cc:
        from backend.springer_live import COUNTRY_CC

        cc = COUNTRY_CC.get(str(row.get("name") or "").strip().upper()) or ""
    if cc:
        return _cc_name(cc)
    return str(row.get("name") or "")


def _as_bar_rows(kind: str, rows: list) -> list:
    ranked = []
    for i, row in enumerate(rows[:10], 1):
        if kind == "countries":
            label = f"{i}. {_country_label(row)}"
        else:
            label = f"{i}. {row.get('name') or '—'}"
        try:
            n = int(row["count"])
        except (TypeError, ValueError, KeyError):
            continue
        ranked.append({"name": label, "count": n, "cc": row.get("cc")})
    return ranked


def _turkey_in_top(rows: list) -> bool:
    return any(str(r.get("cc") or "") == "TR" for r in rows[:10])


def _tr_row(rows: list) -> dict | None:
    for row in rows:
        if str(row.get("cc") or "") == "TR":
            return row
    return None


def _sorted_cc(rows: list) -> list:
    out = []
    for row in rows:
        try:
            n = int(row["count"])
        except (TypeError, ValueError, KeyError):
            continue
        item = dict(row)
        item["count"] = n
        out.append(item)
    out.sort(key=lambda r: (-int(r["count"]), str(r.get("cc") or r.get("name") or "")))
    return out


def _country_list_items(rows: list, turkey: dict | None = None, *, region: str = "both") -> list:
    """Aynı eksendeki kayıt sayısına göre sıra. Daha uzun çubuk alta yazılmaz."""
    working = _sorted_cc(rows)
    info = turkey or {}
    if region == "both" and working and _tr_row(working) is None:
        extra = info.get("count")
        if isinstance(extra, int):
            working = _sorted_cc(working + [{"cc": "TR", "name": "Turkey", "count": extra}])
    items = _as_bar_rows("countries", working)
    if region != "both" or not items or _turkey_in_top(working):
        return items
    items.append({"name": t("pub.cc_ellipsis"), "count": None, "gap": True})
    tr = _tr_row(working)
    if tr is not None:
        rank = next(i for i, row in enumerate(working, 1) if str(row.get("cc") or "") == "TR")
        items.append({"name": t("pub.cc_tr_list_label_n", n=rank), "count": int(tr["count"]), "cc": "TR"})
        return items
    items.append({"name": t("pub.cc_tr_list_label"), "count": None, "cc": "TR", "out": True})
    return items


def _render_breakdown(topic: str | None, bundle: dict, region: str = "both") -> None:
    from backend.springer_live import TOPIC_ORDER
    from components.ui_helpers import show_empty, show_plotly

    cap_one = t("pub.cc_caption")
    if region == "eu":
        cap_one = t("pub.cc_caption_eu")
    cap_all = t("pub.cc_caption_all")
    title_one = t("pub.chart_cc")
    empty = t("pub.empty_cc")
    turkey_map = bundle.get("turkey_by_topic") or {}
    st.markdown(f"### {title_one}")

    def _draw_cc(raw: list, chart_title: str | None = None, turkey: dict | None = None, topic_key: str | None = None) -> bool:
        info = turkey if turkey is not None else (bundle.get("turkey") or {})
        rows = _country_list_items(raw, info, region=region)
        if not rows:
            return False
        title = chart_title or title_one
        show_plotly(render_country_rank_chart(rows, title, topic=topic_key))
        return True

    if topic:
        raw = bundle.get("countries") or []
        st.markdown(f"#### {topic_label(topic)}")
        st.caption(cap_one)
        if _draw_cc(raw, f"{title_one} — {topic}", topic_key=topic):
            return
        show_empty(empty)
        return

    st.caption(cap_all if region == "both" else cap_one)
    by_topic = bundle.get("countries_by_topic") or {}
    drawn = False
    for name in TOPIC_ORDER:
        raw = by_topic.get(name) or []
        turkey = turkey_map.get(name) or {}
        rows = _country_list_items(raw, turkey, region=region)
        if not rows:
            continue
        drawn = True
        st.markdown(f"#### {topic_label(name)}")
        show_plotly(render_country_rank_chart(rows, f"{title_one} — {name}", topic=name))
    if drawn:
        return
    pooled = bundle.get("countries") or []
    if pooled and _draw_cc(pooled, title_one):
        return
    if region != "both":
        wide = AcademicService.get_bundle("both", topic)
        wide_raw = wide.get("countries") or []
        if wide_raw:
            st.caption(t("pub.cc_region_fallback"))
            if _draw_cc(wide_raw, title_one):
                return
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
        lead=t("pub.lead"),
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
    if region == "tr":
        region = "both"
    _labels = [t(f"pub.section.{k}") for k in PUB_SECTION_KEYS]
    _map = dict(zip(_labels, PUB_SECTION_KEYS))
    section = _map.get(
        select_section(t("pub.view"), _labels, key=f"academic_section_story_{get_lang()}_v4"),
        PUB_SECTION_KEYS[0],
    )

    bundle = AcademicService.get_bundle(region, topic)
    fetched = str(bundle.get("fetched_at") or "")
    if fetched:
        st.caption(t("app.live_cached", ts=fetched))

    def _trend_fig():
        df = AcademicService.get_trend_df(region, topic)
        if df is None or df.empty:
            return None
        return render_academic_trends_chart(df, t("pub.chart_one_title"))

    if section == "year":
        st.caption(t("pub.chart_one_body"))
        years = bundle.get("year_counts") or {}
        years = {str(y): int(years.get(str(y), 0) or 0) for y in trend_years()}
        fig = _trend_fig()
        if fig is not None:
            show_plotly(fig)
        elif any(years.values()):
            show_plotly(render_academic_database_chart(years, t("pub.chart_one_title"), t("pub.chart_year_x")))
        else:
            show_empty(t("pub.empty_year_region") if region != "both" else t("pub.empty_year"))

        st.caption(t("pub.chart_two_body"))
        if current_view_mode() == "expert":
            st.caption(t("pub.chart_two_body_expert"))
        series = bundle.get("year_series") or {}
        topic_rows = []
        for name in TOPIC_ORDER:
            years = series.get(name) or {}
            n = sum(int(years.get(str(y), 0) or 0) for y in trend_years())
            if n > 0:
                topic_rows.append({"name": topic_label(name), "count": n})
        if not topic_rows:
            topics = bundle.get("topics") or {}
            topic_rows = [
                {"name": topic_label(k), "count": v}
                for k, v in topics.items()
                if k in TOPIC_ORDER and isinstance(v, int)
            ]
        if topic_rows:
            show_plotly(render_academic_bar_chart(topic_rows, t("pub.chart_two_title")))
        else:
            show_empty(t("pub.empty_year_region") if region != "both" else t("pub.empty_year"))

        if region == "eu":
            _render_eu_mno_panel(topic)

    elif section == "country":
        _render_breakdown(topic, bundle, region)

    elif section == "cited":
        st.caption(t("pub.cited_caption") if region == "both" else t("pub.cited_caption_region"))
        papers = AcademicService.get_cited_papers(region, topic)
        if not papers:
            show_empty(t("pub.empty_cited_region") if region == "eu" else t("pub.empty_cited"))
        else:
            for paper in papers:
                render_paper_card(_with_source(paper))

    elif section == "tt_eu":
        render_tt_europe_pub_section(topic)
