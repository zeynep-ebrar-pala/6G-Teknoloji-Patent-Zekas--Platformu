"""
Teknoloji performans KPI grafikleri — makale/patent sayısı değil.
charts.py'den ayrı tutulur; tech.py doğrudan buradan import eder.
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple

import plotly.graph_objects as go

from components.charts import _apply_layout, _color_list, _count_axis, _ints
from i18n.core import get_lang, t


def render_technology_performance_bar(
    metrics: List[Dict[str, Any]],
    title: str,
    unit: str,
) -> go.Figure:
    lang = get_lang()
    labels: List[str] = []
    vals: List[int] = []
    displays: List[str] = []
    for m in metrics:
        labels.append(str(m.get(f"label_{lang}") or m.get("label_en") or ""))
        try:
            v = int(m.get("value") or 0)
        except (TypeError, ValueError):
            v = 0
        vals.append(v)
        displays.append(str(m.get(f"display_{lang}") or m.get("display_en") or str(v)))
    fig = go.Figure(
        go.Bar(
            x=labels,
            y=vals,
            marker=dict(color=_color_list(labels)),
            text=displays,
            textposition="outside",
            cliponaxis=False,
            hovertemplate="%{x}<br><b>%{text}</b><extra></extra>",
        )
    )
    y_title = unit if unit else t("charts.perf_value")
    _apply_layout(
        fig,
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=14, color="#FFFFFF")),
        xaxis=dict(title="", type="category", gridcolor="rgba(200, 209, 220, 0.1)", tickangle=-12),
        yaxis=_count_axis(y_title, vals),
        height=340,
        bargap=0.32,
    )
    return fig


def render_technology_performance_line(
    points: List[Dict[str, Any]],
    title: str,
    x_title: str,
    y_title: str,
) -> go.Figure:
    lang = get_lang()
    xs: List[float] = []
    ys: List[float] = []
    labels: List[str] = []
    for p in points:
        try:
            xs.append(float(p.get("x") or 0))
            ys.append(float(p.get("y") or 0))
        except (TypeError, ValueError):
            continue
        labels.append(str(p.get(f"label_{lang}") or p.get("label_en") or ""))
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=xs,
            y=ys,
            mode="lines+markers+text",
            line=dict(width=3, color="#FFB020"),
            marker=dict(size=10, color="#FFB020", line=dict(width=1, color="#FFFFFF")),
            text=labels,
            textposition="top center",
            textfont=dict(color="#FFFFFF", size=11),
            hovertemplate=f"%{{x}} {x_title}<br><b>%{{y}}</b> {y_title}<extra></extra>",
        )
    )
    _apply_layout(
        fig,
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=14, color="#FFFFFF")),
        xaxis=dict(title=x_title, gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=_count_axis(y_title, _ints(ys)),
        height=360,
    )
    return fig


def render_technology_performance_charts(tech_id: str) -> Tuple[List[go.Figure], str]:
    from data.tech_performance import get_tech_performance

    profile = get_tech_performance(tech_id)
    if not profile:
        return [], ""
    lang = get_lang()
    caption = str(profile.get(f"caption_{lang}") or profile.get("caption_en") or "")
    figures: List[go.Figure] = []
    for chart in profile.get("charts") or []:
        ctype = chart.get("type") or "bar"
        title = str(chart.get(f"title_{lang}") or chart.get("title_en") or "")
        if ctype == "line":
            x_unit = str(chart.get(f"x_unit_{lang}") or chart.get("x_unit_en") or "")
            y_unit = str(chart.get(f"y_unit_{lang}") or chart.get("y_unit_en") or "")
            x_title = str(chart.get(f"x_title_{lang}") or chart.get("x_title_en") or "")
            y_title = str(chart.get(f"y_title_{lang}") or chart.get("y_title_en") or "")
            if x_unit:
                x_title = f"{x_title} ({x_unit})"
            if y_unit:
                y_title = f"{y_title} ({y_unit})"
            figures.append(
                render_technology_performance_line(
                    chart.get("points") or [],
                    title,
                    x_title,
                    y_title,
                )
            )
        else:
            unit = str(chart.get(f"unit_{lang}") or chart.get("unit_en") or "")
            figures.append(
                render_technology_performance_bar(
                    chart.get("metrics") or [],
                    title,
                    unit,
                )
            )
    return figures, caption
