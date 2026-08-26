"""
Türk Telekom 6G Platform - Plotly & Interactive Chart Components
Adheres to corporate dark theme standards (#0E1117 bg, #1A1F2B surface, #0099FF primary, #00C2FF secondary).
Safe fallback if networkx is missing.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, Any, List, Optional

from data.tt_europe import place_sort_key
from i18n.core import get_lang, t

# Defensive import for networkx
try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False

# Koyu temada yan yana durunca karışmayan nitel palet (ardışık iki renk aynı aileden değil)
QUALITATIVE_COLORS = [
    "#FFB020",  # amber
    "#3B82F6",  # royal blue — tek mavi
    "#22C55E",  # green
    "#EF4444",  # red
    "#A855F7",  # purple
    "#F97316",  # orange
    "#EC4899",  # magenta
    "#14B8A6",  # teal
    "#EAB308",  # yellow
    "#FB7185",  # rose
    "#818CF8",  # indigo
    "#84CC16",  # lime
]

# Firma rengi grafikler arasında sabit kalsın
COMPANY_COLORS = {
    "Ericsson": "#FFB020",
    "Huawei": "#EF4444",
    "Nokia": "#A855F7",
    "Samsung": "#14B8A6",
    "Qualcomm": "#22C55E",
    "ZTE": "#818CF8",
    "NEC": "#EAB308",
    "NICT": "#FB7185",
    "Intel": "#3B82F6",
    "Türk Telekom": "#E20074",
    "Türk Telekom (Netsia)": "#E20074",
    "AT&T": "#F97316",
    "Deutsche Telekom": "#EC4899",
    "InterDigital": "#3B82F6",
    "LG Electronics": "#EAB308",
    "Northeastern Univ.": "#FB7185",
}

DOMAIN_COLORS = {
    "ISAC": "#FFB020",
    "RIS": "#A855F7",
    "Cell-Free": "#3B82F6",
    "THz": "#EF4444",
    "AI-RAN": "#22C55E",
    "NTN": "#F97316",
    "Ambient IoT": "#EC4899",
}

# Corporate Dark Layout Template
DARK_LAYOUT_TEMPLATE = dict(
    paper_bgcolor='#1A1F2B',
    plot_bgcolor='#1A1F2B',
    font=dict(family='Inter, sans-serif', color='#C8D1DC', size=12),
    margin=dict(l=40, r=40, t=50, b=80),
    legend=dict(
        orientation="h",
        yanchor="top",
        y=-0.18,
        x=0.0,
        bgcolor='rgba(18, 22, 32, 0.92)',
        bordercolor='rgba(200, 209, 220, 0.15)',
        font=dict(color='#FFFFFF', size=11),
        itemsizing="constant",
        traceorder="normal",
    )
)


def _layout() -> dict:
    sep = ".," if get_lang() == "tr" else ",."
    return {**DARK_LAYOUT_TEMPLATE, "separators": sep}


def _apply_layout(fig: go.Figure, **kwargs) -> go.Figure:
    """Tema + özel alan. Figure.update_layout(dict, margin=...) Plotly 6’da çiftler."""
    layout = _layout()
    layout.update(kwargs)
    fig.layout.update(layout)
    return fig


def _hex_rgba(hex_color: str, alpha: float) -> str:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


TT_BAR = "#E20074"
OTHER_BAR = "#00C2FF"


def _is_tt_name(name: str) -> bool:
    """Türk Telekom / Netsia. Deutsche Telekom eşleşmez."""
    s = (name or "").casefold()
    return "türk telekom" in s or "turk telekom" in s or "netsia" in s


def _series_color(name: str, index: int = 0) -> str:
    if _is_tt_name(name):
        return TT_BAR
    if name in COMPANY_COLORS:
        return COMPANY_COLORS[name]
    if name in DOMAIN_COLORS:
        return DOMAIN_COLORS[name]
    return QUALITATIVE_COLORS[index % len(QUALITATIVE_COLORS)]


def _color_list(names: List[str]) -> List[str]:
    used = set()
    out: List[str] = []
    fallback_i = 0
    for name in names:
        if _is_tt_name(name):
            out.append(TT_BAR)
            used.add(TT_BAR)
            continue
        color = _series_color(name, fallback_i)
        if color in used:
            while QUALITATIVE_COLORS[fallback_i % len(QUALITATIVE_COLORS)] in used:
                fallback_i += 1
            color = QUALITATIVE_COLORS[fallback_i % len(QUALITATIVE_COLORS)]
        used.add(color)
        out.append(color)
        fallback_i += 1
    return out


def _year_labels(years) -> List[str]:
    """Takvim yılını 2024.2 gibi ondalığa çevirmeden etiketler."""
    return [str(int(y)) for y in years]


def _year_axis(labels: List[str]) -> dict:
    return dict(
        title=t("charts.year"),
        type="category",
        categoryorder="array",
        categoryarray=labels,
        tickmode="array",
        tickvals=labels,
        ticktext=labels,
        gridcolor="rgba(200, 209, 220, 0.1)",
    )


def _ints(vals) -> List[int]:
    out: List[int] = []
    for val in vals:
        try:
            out.append(int(val))
        except (TypeError, ValueError):
            out.append(0)
    return out


def _count_axis(title: str, values: Optional[List[int]] = None) -> dict:
    """Sayım ekseni: 0.5 tik yok; küçük kümede 1’er adım."""
    vals = _ints(values or [])
    vmax = max(vals) if vals else 0
    axis = dict(
        title=title,
        gridcolor="rgba(200, 209, 220, 0.1)",
        rangemode="tozero",
        tickformat="d",
        separatethousands=False,
        hoverformat="d",
    )
    if vmax <= 30:
        axis["dtick"] = 1
        axis["tick0"] = 0
        axis["range"] = [0, max(vmax, 1) + max(1, (vmax + 4) // 5)]
    return axis


def _count_bar(
    labels: List[str],
    values,
    *,
    horizontal: bool = False,
    unit_key: str = "charts.paper_count",
) -> go.Bar:
    vals = _ints(values)
    unit = t(unit_key)
    hover = (
        t("charts.hover_h", unit=unit) if horizontal else t("charts.hover_v", unit=unit)
    )
    if horizontal:
        return go.Bar(
            x=vals,
            y=labels,
            orientation="h",
            marker=dict(color=_color_list(labels)),
            text=[str(v) for v in vals],
            textposition="outside",
            cliponaxis=False,
            hovertemplate=hover,
        )
    return go.Bar(
        x=labels,
        y=vals,
        marker=dict(color=_color_list(labels)),
        text=[str(v) for v in vals],
        textposition="outside",
        cliponaxis=False,
        hovertemplate=hover,
    )

def render_trl_radar_chart(technologies_data: Dict[str, Any]) -> go.Figure:
    """Örümcek ağı TRL: data/technologies.py tam sayıları; hover dayanağı trl_desc."""
    categories = [tech["acronym"] for tech in technologies_data.values()]
    trl_values = [int(tech["trl"]) for tech in technologies_data.values()]
    bases = [str(tech.get("trl_desc") or "") for tech in technologies_data.values()]

    categories_closed = categories + [categories[0]]
    trl_values_closed = trl_values + [trl_values[0]]
    bases_closed = bases + [bases[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=trl_values_closed,
        theta=categories_closed,
        fill="toself",
        name=t("charts.trl_series"),
        fillcolor="rgba(0, 153, 255, 0.25)",
        line=dict(color="#00E5FF", width=3),
        marker=dict(size=8, color="#0099FF", symbol="circle"),
        customdata=bases_closed,
        hovertemplate=t("charts.trl_hover"),
    ))
    fig.add_trace(go.Scatterpolar(
        r=trl_values,
        theta=categories,
        mode="text",
        text=[str(n) for n in trl_values],
        textposition="top center",
        textfont=dict(color="#FFFFFF", size=12, family="Inter, sans-serif"),
        hoverinfo="skip",
        showlegend=False,
    ))

    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.trl_title')}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 9],
                tickvals=[1, 3, 5, 7, 9],
                gridcolor='rgba(200, 209, 220, 0.15)',
                linecolor='rgba(200, 209, 220, 0.2)',
                tickfont=dict(color='#94A3B8', size=12)
            ),
            angularaxis=dict(
                gridcolor='rgba(200, 209, 220, 0.15)',
                linecolor='rgba(200, 209, 220, 0.2)',
                tickfont=dict(color='#FFFFFF', size=14)
            ),
            bgcolor='#121620'
        ),
        showlegend=False,
        height=460
    )
    return fig

def render_technology_record_counts_chart(df_counts: pd.DataFrame, tech_label: str) -> go.Figure:
    """Doğrulanmış patent kayıtlarının yıla göre sayısı — temsili hedef metriği yok."""
    y_col = [c for c in df_counts.columns if c != "Years"][0]
    labels = _year_labels(df_counts["Years"])
    y_vals = _ints(df_counts[y_col])
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=labels,
        y=y_vals,
        marker=dict(color="#00E5FF"),
        name=tech_label,
        text=[str(v) for v in y_vals],
        textposition="outside",
        cliponaxis=False,
        hovertemplate=t("charts.hover_v", unit=t("charts.count")),
    ))
    _apply_layout(
        fig,
        title=dict(
            text=f"<b>{t('charts.tech_counts', label=tech_label)}</b>",
            x=0.02, y=0.95, font=dict(size=14, color="#FFFFFF"),
        ),
        xaxis=_year_axis(labels),
        yaxis=_count_axis(t("charts.count"), y_vals),
        height=320,
        bargap=0.35,
    )
    return fig

def render_patent_trends_chart(df_trends: pd.DataFrame) -> go.Figure:
    """Yıllık patent kayıtları — kategorik takvim yılı (2024.2 üretilmez)."""
    fig = go.Figure()
    labels = _year_labels(df_trends["Years"])
    companies = [c for c in df_trends.columns if c != "Years"]
    colors = _color_list(companies)

    all_vals: List[int] = []
    for col, color in zip(companies, colors):
        y_vals = _ints(df_trends[col])
        all_vals.extend(y_vals)
        fig.add_trace(go.Bar(
            x=labels,
            y=y_vals,
            name=col,
            marker=dict(color=color, line=dict(width=0)),
            hovertemplate=t("charts.hover_v", unit=t("charts.patent_count")),
        ))

    _apply_layout(
        fig,
        barmode="group",
        title=dict(text=f"<b>{t('charts.patent_year')}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=_year_axis(labels),
        yaxis=_count_axis(t("charts.patent_count"), all_vals),
        height=480,
        bargap=0.22,
        bargroupgap=0.08,
    )
    return fig

def render_company_patent_domain_chart(df_domains: pd.DataFrame) -> go.Figure:
    """Firma × konu radar — ham kayıt sayısı, yüzde yok."""
    fig = go.Figure()
    domains = [c for c in df_domains.columns if c != "Company"]
    shown = df_domains.copy()
    value_cols = [c for c in shown.columns if c != "Company"]
    shown["_tot"] = shown[value_cols].sum(axis=1)
    shown = shown[shown["_tot"] > 0].sort_values("_tot", ascending=False).drop(columns=["_tot"])
    companies = shown["Company"].tolist()
    colors = _color_list(companies)
    peak = 1
    for _, row in shown.iterrows():
        peak = max(peak, max((int(row[d] or 0) for d in domains), default=0))

    for idx, (_, row) in enumerate(shown.iterrows()):
        company = row["Company"]
        color = colors[idx]
        values = [int(row[d] or 0) for d in domains]
        values_closed = values + [values[0]]
        domains_closed = domains + [domains[0]]

        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=domains_closed,
            fill="toself",
            name=company,
            fillcolor=_hex_rgba(color, 0.14),
            line=dict(color=color, width=2.5),
            hovertemplate="%{theta}: %{r}<extra>" + company + "</extra>",
        ))

    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.domain_radar')}</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, peak],
                dtick=1 if peak <= 12 else None,
                gridcolor="rgba(200, 209, 220, 0.15)",
                tickformat="d",
            ),
            angularaxis=dict(gridcolor="rgba(200, 209, 220, 0.15)", tickfont=dict(color="#FFFFFF")),
            bgcolor="#121620",
        ),
        height=440,
    )
    return fig

def render_patent_keywords_chart(keywords_dict: Dict[str, int]) -> go.Figure:
    """Renders bar chart representing top keywords in patent claim texts."""
    sorted_kw = dict(sorted(keywords_dict.items(), key=lambda x: x[1], reverse=True))
    
    fig = go.Figure(go.Bar(
        x=list(sorted_kw.values()),
        y=list(sorted_kw.keys()),
        orientation='h',
        marker=dict(color=_color_list(list(sorted_kw.keys())))
    ))

    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.keywords')}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=dict(title=t("charts.kw_x"), gridcolor='rgba(200, 209, 220, 0.1)'),
        yaxis=dict(autorange="reversed", gridcolor='rgba(200, 209, 220, 0.1)'),
        height=380
    )
    return fig

def render_academic_trends_chart(
    df_academic: pd.DataFrame,
    title: str | None = None,
) -> go.Figure:
    """Renders academic publication volume trends by 6G topic."""
    fig = go.Figure()
    labels = _year_labels(df_academic["Years"])
    topics = [c for c in df_academic.columns if c != "Years"]
    colors = _color_list(topics)
    markers = ["circle", "square", "diamond", "triangle-up", "star", "x", "cross", "hexagon"]
    chart_title = title or t("charts.academic_trend")

    for idx, (col, color) in enumerate(zip(topics, colors)):
        y_vals = _ints(df_academic[col])
        fig.add_trace(go.Scatter(
            x=labels,
            y=y_vals,
            mode="lines+markers",
            name=col,
            line=dict(width=3, color=color),
            marker=dict(size=9, color=color, symbol=markers[idx % len(markers)], line=dict(width=1, color="#FFFFFF")),
            hovertemplate=t("charts.hover_v", unit=t("charts.paper_count")),
        ))

    _apply_layout(
        fig,
        title=dict(text=f"<b>{chart_title}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=_year_axis(labels),
        yaxis=_count_axis(t("charts.paper_count"), [
            int(v) for col in topics for v in _ints(df_academic[col])
        ]),
        height=480
    )
    return fig


def render_academic_database_chart(
    db_dict: Dict[str, int],
    title: str | None = None,
    xlabel: str | None = None,
) -> go.Figure:
    """Renders bar chart of measured paper counts (integer axis, integer hover)."""
    title = title or t("charts.db_default")
    xlabel = xlabel or t("charts.publisher")
    labels = list(db_dict.keys())
    vals = _ints(db_dict.values())
    fig = go.Figure(_count_bar(labels, vals, unit_key="charts.paper_count"))
    _apply_layout(
        fig,
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color='#FFFFFF')),
        xaxis=dict(title=xlabel, type="category", gridcolor='rgba(200, 209, 220, 0.1)'),
        yaxis=_count_axis(t("charts.paper_count"), vals),
        height=360,
        bargap=0.35,
    )
    return fig

def render_patent_network_graph(edges: Optional[List[tuple]] = None) -> go.Figure:
    """Renders assignee–technology domain graph from verified patent edges."""
    if edges is None:
        edges = []

    if HAS_NETWORKX:
        G = nx.Graph()

        G.add_node("6G Core", size=25, color="#00E5FF")
        domain_nodes = sorted({e[1] for e in edges})
        assignee_nodes = sorted({e[0] for e in edges})

        for domain in domain_nodes:
            G.add_node(domain, size=18, color=_series_color(domain))
            G.add_edge("6G Core", domain)

        for assignee in assignee_nodes:
            G.add_node(assignee, size=15, color=_series_color(assignee))

        G.add_edges_from(edges)
        
        pos = nx.spring_layout(G, seed=42)
        
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=1.5, color='rgba(200, 209, 220, 0.3)'),
            hoverinfo='none',
            mode='lines'
        )

        node_x = []
        node_y = []
        node_text = []
        node_color = []
        node_size = []
        
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(node)
            node_color.append(G.nodes[node]['color'])
            node_size.append(G.nodes[node]['size'])

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            text=node_text,
            textposition="top center",
            textfont=dict(color='#FFFFFF', size=11),
            marker=dict(
                color=node_color,
                size=node_size,
                line_width=2,
                line_color='#FFFFFF'
            )
        )
        fig = go.Figure(data=[edge_trace, node_trace])
    else:
        fig = go.Figure()
        fig.add_annotation(
            text=t("charts.nx_missing"),
            showarrow=False,
            font=dict(color="#94A3B8"),
        )

    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.network')}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=450
    )
    return fig


def render_company_counts_chart(
    counts: Dict[str, int], order: Optional[List[str]] = None
) -> go.Figure:
    """Şartname firmalarının tamamı; 0 da çubuk (Lens boş = uydurma yok)."""
    if order:
        names = list(order)
        vals = _ints(int(counts.get(n, 0) or 0) for n in names)
    else:
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        names = [c for c, _ in sorted_items]
        vals = _ints(n for _, n in sorted_items)
    fig = go.Figure(_count_bar(names, vals, unit_key="charts.patent_count"))
    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.company_counts')}</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        xaxis=dict(title=t("charts.company"), gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=_count_axis(t("charts.patent_count"), vals),
        height=400,
        bargap=0.28,
    )
    return fig


def render_patent_topic_mix_chart(
    counts: Dict[str, int], order: Optional[List[str]] = None
) -> go.Figure:
    """Yedi 6G konusu — Unclassified yok."""
    names = list(order) if order else [c for c, _ in sorted(counts.items(), key=lambda x: x[1], reverse=True)]
    vals = _ints(int(counts.get(n, 0) or 0) for n in names)
    fig = go.Figure(_count_bar(names, vals, unit_key="charts.patent_count"))
    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.topic_mix')}</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        xaxis=dict(title=t("charts.topic_axis"), gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=_count_axis(t("charts.patent_count"), vals),
        height=360,
        bargap=0.28,
    )
    return fig


def render_patent_density_heatmap(df_density: pd.DataFrame) -> go.Figure:
    """Firma × teknoloji — Lens total, hücrede tam sayı."""
    companies = df_density["Company"].tolist()
    domains = [c for c in df_density.columns if c != "Company"]
    z = [[int(v or 0) for v in row] for row in df_density[domains].values.tolist()]
    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=domains,
            y=companies,
            colorscale=[[0, "#121620"], [0.5, "#0066B3"], [1, "#00E5FF"]],
            hoverongaps=False,
            text=z,
            texttemplate="%{text:d}",
            textfont=dict(color="#FFFFFF", size=11),
            colorbar=dict(tickformat="d", title=t("charts.patent_count")),
        )
    )
    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.density')}</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        height=max(380, 44 * len(companies) + 120),
    )
    return fig


def render_patent_sunburst(df_tree: pd.DataFrame) -> go.Figure:
    """Firma → konu treemap. Yayın no yok; alan = Lens total."""
    ids: List[str] = []
    labels: List[str] = []
    parents: List[str] = []
    values: List[int] = []
    colors: List[str] = []
    for company, grp in df_tree.groupby("company", sort=False):
        cid = f"c:{company}"
        ids.append(cid)
        labels.append(str(company))
        parents.append("")
        values.append(int(grp["n"].sum()))
        colors.append("#334155")
        for _, row in grp.iterrows():
            domain = str(row["domain"])
            ids.append(f"{cid}/{domain}")
            labels.append(domain)
            parents.append(cid)
            values.append(int(row["n"]))
            colors.append(DOMAIN_COLORS.get(domain, "#64748B"))
    fig = go.Figure(
        go.Treemap(
            ids=ids,
            labels=labels,
            parents=parents,
            values=values,
            branchvalues="total",
            marker=dict(colors=colors, line=dict(width=1, color="#1A1F2B")),
            textinfo="label+value",
            hovertemplate="<b>%{label}</b><br>"
            + t("charts.patent_count")
            + ": %{value:d}<extra></extra>",
        )
    )
    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.sunburst')}</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        height=520,
        margin=dict(l=20, r=20, t=50, b=20),
    )
    return fig


def render_patent_tfidf_map(df_map: pd.DataFrame) -> go.Figure:
    """Patent başlıklarının TF-IDF + PCA 2D haritası."""
    fig = px.scatter(
        df_map,
        x="x",
        y="y",
        color="domain",
        hover_name="title",
        hover_data={"company": True, "id": True, "year": True, "x": False, "y": False},
        color_discrete_map=DOMAIN_COLORS,
        color_discrete_sequence=QUALITATIVE_COLORS,
    )
    fig.update_traces(marker=dict(size=12, line=dict(width=1, color="#FFFFFF")))
    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.tfidf')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title="PCA-1", gridcolor="rgba(200, 209, 220, 0.1)", zeroline=False),
        yaxis=dict(title="PCA-2", gridcolor="rgba(200, 209, 220, 0.1)", zeroline=False),
        height=440,
    )
    return fig


def render_patent_wordcloud(keywords_dict: Dict[str, int]):
    """Patent başlıklarından kelime bulutu (matplotlib). Başarısızsa None döner."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud
    except ImportError:
        return None
    if not keywords_dict:
        return None
    wc = WordCloud(
        width=900,
        height=380,
        background_color="#1A1F2B",
        colormap="tab10",
        prefer_horizontal=0.9,
        min_font_size=10,
    ).generate_from_frequencies(keywords_dict)
    fig, ax = plt.subplots(figsize=(9, 3.8))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    fig.patch.set_facecolor("#1A1F2B")
    ax.set_facecolor("#1A1F2B")
    fig.tight_layout(pad=0)
    return fig


def render_tt_europe_choropleth(rows: List[Dict[str, Any]], lang: str = "tr") -> go.Figure:
    """Yalnızca adı doğrulanmış ülkeler; KKTC ISO boyası değil kare işaret. 19/24 iddiası boyanmaz."""
    name_col = "name_tr" if lang == "tr" else "name_en"
    label_col = "label_tr" if lang == "tr" else "label_en"
    place_col = t("tt_eu.named_col_place")
    layer_col = t("tt_eu.map_col_layer")
    ordered = sorted(rows, key=lambda r: place_sort_key(str(r.get(name_col) or ""), lang))
    fig = go.Figure()
    for row in ordered:
        nm = str(row.get(name_col) or "")
        color = row.get("color") or "#64748B"
        layer = t(f"tt_eu.layer.{row.get('layer')}")
        iso = str(row.get("iso3") or "")
        if len(iso) == 3:
            fig.add_trace(
                go.Choropleth(
                    locations=[iso],
                    z=[1],
                    zmin=0,
                    zmax=1,
                    locationmode="ISO-3",
                    colorscale=[[0, color], [1, color]],
                    showscale=False,
                    name=nm,
                    showlegend=True,
                    hovertext=nm,
                    customdata=[[layer]],
                    hovertemplate="<b>%{hovertext}</b><br>" + layer_col + ": %{customdata[0]}<extra></extra>",
                    marker_line_width=0.6,
                    marker_line_color="rgba(200,209,220,0.35)",
                )
            )
            continue
        if row.get("lat") is None or row.get("lon") is None:
            continue
        fig.add_trace(
            go.Scattergeo(
                lon=[row["lon"]],
                lat=[row["lat"]],
                text=[nm],
                mode="markers+text",
                textposition="top center",
                marker=dict(
                    size=13,
                    color=color,
                    symbol="square",
                    line=dict(width=1.2, color="#FFFFFF"),
                ),
                name=nm,
                hovertext=[row.get(label_col) or ""],
                hovertemplate="<b>%{text}</b><br>%{hovertext}<extra></extra>",
            )
        )
    fig.update_geos(
        bgcolor="#1A1F2B",
        landcolor="#121620",
        oceancolor="#0E1117",
        lakecolor="#0E1117",
        subunitcolor="rgba(200,209,220,0.2)",
        countrycolor="rgba(200,209,220,0.25)",
        coastlinecolor="rgba(200,209,220,0.3)",
        showlakes=False,
        showframe=False,
        showcountries=True,
        showcoastlines=True,
        projection_type="natural earth",
        center=dict(lat=46.5, lon=22.0),
        lonaxis_range=[-12, 46],
        lataxis_range=[33.2, 72],
    )
    layout = _layout()
    layout.update(
        title=dict(text=f"<b>{t('charts.tt_map')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        height=560,
        legend_title_text=place_col,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.98,
            xanchor="left",
            x=0.0,
            bgcolor="rgba(18, 22, 32, 0.92)",
            font=dict(color="#FFFFFF", size=11),
            traceorder="normal",
        ),
        margin=dict(l=10, r=10, t=50, b=10),
        coloraxis_showscale=False,
    )
    fig.layout.update(layout)
    return fig


def render_tt_role_kind_chart(items: List[Dict[str, Any]]) -> go.Figure:
    """Kanıt türü adedi — pazar payı değil. 0 çubuk çizilmez."""
    drawn = [i for i in items if int(i.get("count") or 0) > 0]
    names = [t(f"tt_eu.layer.{i['id']}") for i in drawn]
    counts = [int(i["count"]) for i in drawn]
    fig = go.Figure(go.Bar(
        x=counts,
        y=names,
        orientation="h",
        marker=dict(color=["#E20074", "#00C2FF", "#A855F7", "#FFB020", "#14B8A6", "#64748B"][: len(names)]),
    ))
    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.tt_role')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title=t("charts.tt_role_x"), gridcolor="rgba(200, 209, 220, 0.1)", dtick=1),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        height=max(320, 36 * max(len(drawn), 1) + 80),
    )
    return fig


def render_tt_vs_vendors_chart(counts: Dict[str, int]) -> go.Figure:
    """Kilitli örnek küme. Küresel pazar veya SEP payı değildir."""
    sorted_items = sorted(
        ((n, v) for n, v in counts.items() if int(v or 0) > 0),
        key=lambda x: x[1],
        reverse=True,
    )
    names = [c for c, _ in sorted_items]
    vals = _ints(n for _, n in sorted_items)
    fig = go.Figure(_count_bar(names, vals, unit_key="charts.patent_count"))
    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.tt_vs_vendors')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title=t("charts.company"), gridcolor="rgba(200, 209, 220, 0.1)", tickangle=-25),
        yaxis=_count_axis(t("charts.patent_count"), vals),
        height=400,
        bargap=0.28,
    )
    return fig


def render_tt_country_rank_chart(
    rows: List[Dict[str, Any]], value_key: str, title: str, x_title: str
) -> go.Figure:
    """Kilitli 3 MNO + TT. Yayın: kilitli DOI (TT). Patent: kilitli örnek. 0 çubuk yok."""
    ordered = sorted(
        [r for r in rows if int(r.get(value_key) or 0) > 0],
        key=lambda r: int(r.get(value_key) or 0),
        reverse=True,
    )
    names = [r["name"] for r in ordered]
    vals = [int(r.get(value_key) or 0) for r in ordered]
    colors = [TT_BAR if r.get("is_tt") or _is_tt_name(r.get("name") or "") else OTHER_BAR for r in ordered]
    fig = go.Figure(go.Bar(
        x=names,
        y=vals,
        marker=dict(color=colors),
        text=[str(v) for v in vals],
        textposition="outside",
        cliponaxis=False,
        hovertemplate=t("charts.hover_v", unit=x_title),
    ))
    _apply_layout(
        fig,
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title=t("charts.company"), gridcolor="rgba(200, 209, 220, 0.1)", tickangle=-20),
        yaxis=_count_axis(x_title, vals),
        height=360,
        bargap=0.28,
    )
    return fig


def render_tt_europe_overview_chart(
    rows: List[Dict[str, Any]],
    value_key: str,
    rank_key: str,
    name_key: str,
    title: str,
    x_title: str,
    *,
    label_key: Optional[str] = None,
) -> go.Figure:
    """Avrupa geneli sayı; 0 olan ülke çizilmez. Uydurma yok."""
    positive = [r for r in rows if int(r.get(value_key) or 0) > 0]
    ordered = sorted(positive, key=lambda r: int(r.get(value_key) or 0), reverse=True)
    if not ordered:
        ordered = []
    names = []
    for r in ordered:
        base = r[name_key]
        extra = r.get(label_key) if label_key else None
        names.append(f"{base} · {extra}" if extra else base)
    vals = [int(r.get(value_key) or 0) for r in ordered]
    colors = [
        TT_BAR if _is_tt_name(r.get(label_key) or "") or _is_tt_name(names[i] if i < len(names) else "") else OTHER_BAR
        for i, r in enumerate(ordered)
    ]
    fig = go.Figure(
        go.Bar(
            x=vals,
            y=names or ["—"],
            orientation="h",
            marker=dict(color=colors or [OTHER_BAR]),
            text=[str(v) for v in (vals or [0])],
            textposition="outside",
        )
    )
    layout = _layout()
    layout.update(
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=_count_axis(x_title, vals),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        height=max(360, 28 * max(len(ordered), 1) + 80),
        margin=dict(l=40, r=70, t=50, b=40),
        showlegend=False,
    )
    fig.layout.update(layout)
    return fig


def tt_vs_comparable_rows(
    rows: List[Dict[str, Any]],
    *,
    lead_key: str = "pub_lead_n",
    tt_key: str = "tt_pub_n",
    lead_name_key: str = "pub_lead",
) -> List[Dict[str, Any]]:
    """Rakip gerçekten sayıldıysa karşılaştır; TT=TT kopya çubuğu dönmez."""
    out: List[Dict[str, Any]] = []
    for row in rows:
        lead_n = int(row.get(lead_key) or 0)
        tt_n = int(row.get(tt_key) or 0)
        if lead_n <= 0 and tt_n <= 0:
            continue
        lead_label = str(row.get(lead_name_key) or "")
        if _is_tt_name(lead_label) and lead_n == tt_n:
            continue
        if lead_n == tt_n and tt_n > 0:
            continue
        out.append(row)
    return out


def render_tt_vs_leader_chart(
    rows: List[Dict[str, Any]],
    name_key: str,
    title: str,
    x_title: str,
    *,
    lead_key: str = "pub_lead_n",
    tt_key: str = "tt_pub_n",
    lead_name: str | None = None,
) -> go.Figure:
    """Ülke 1. operatör vs Türk Telekom. Aynı sayı iki kez çizilmez."""
    name_field = "pat_lead" if lead_key.startswith("pat") else "pub_lead"
    ordered = tt_vs_comparable_rows(
        rows, lead_key=lead_key, tt_key=tt_key, lead_name_key=name_field
    )
    ordered = sorted(ordered, key=lambda r: int(r.get(lead_key) or 0), reverse=True)
    names = [r[name_key] for r in ordered]
    lead = [int(r.get(lead_key) or 0) for r in ordered]
    tt = [int(r.get(tt_key) or 0) for r in ordered]
    fig = go.Figure()
    fig.add_bar(
        name=lead_name or t("tt_eu.overview_pub_lead_short"),
        y=names or ["—"],
        x=lead or [0],
        orientation="h",
        marker_color=OTHER_BAR,
    )
    fig.add_bar(
        name="Türk Telekom",
        y=names or ["—"],
        x=tt or [0],
        orientation="h",
        marker_color=TT_BAR,
    )
    layout = _layout()
    layout.update(
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=_count_axis(x_title, (lead or [0]) + (tt or [0])),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        barmode="group",
        height=max(420, 34 * max(len(ordered), 1) + 90),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0.0),
        margin=dict(l=40, r=40, t=70, b=40),
    )
    fig.layout.update(layout)
    return fig


def render_tt_office_chart(counts: Dict[str, int]) -> go.Figure:
    """TT-grup doğrulanmış patentlerin ofisi — kod değil açık ad."""
    label = {
        "EP": t("charts.office_epo"),
        "US": t("charts.office_uspto"),
        "TR": t("charts.office_turkpatent"),
    }
    order = ["EP", "US", "TR"]
    keys = [k for k in order if int(counts.get(k) or 0) > 0]
    keys += [k for k in counts if k not in order and int(counts.get(k) or 0) > 0]
    names = [label.get(k, k) for k in keys]
    vals = [int(counts[k]) for k in keys]
    fig = go.Figure(
        go.Bar(
            x=names,
            y=vals,
            text=[str(v) for v in vals],
            textposition="outside",
            cliponaxis=False,
            marker=dict(color="#E20074"),
            hovertemplate=t("charts.hover_v", unit=t("charts.patent_count")),
        )
    )
    layout = _layout()
    layout.update(
        title=dict(text=f"<b>{t('charts.tt_office')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(
            title=t("charts.tt_office_x"),
            gridcolor="rgba(200, 209, 220, 0.1)",
            tickangle=-18,
            automargin=True,
        ),
        yaxis=_count_axis(t("charts.patent_count"), vals),
        height=380,
        bargap=0.35,
        margin=dict(l=40, r=20, t=50, b=110),
    )
    fig.layout.update(layout)
    return fig


def render_tt_europe_presence_chart(items: List[Dict[str, Any]], name_key: str = "name") -> go.Figure:
    """Avrupa dokunuşu sayısı (işbirliği/standart/proje) — patent sayısı değildir."""
    names = [i[name_key] for i in items]
    counts = [i["count"] for i in items]
    fig = go.Figure(go.Bar(
        x=counts,
        y=names,
        orientation="h",
        marker=dict(color="#818CF8"),
    ))
    _apply_layout(
        fig,
        title=dict(text=f"<b>{t('charts.tt_europe')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title=t("charts.tt_europe_x"), gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        height=max(320, 36 * max(len(items), 1) + 80),
    )
    return fig


def render_academic_bar_chart(
    items: List[Dict[str, Any]],
    title: str,
    name_key: str = "name",
    x_title: str | None = None,
) -> go.Figure:
    """Kilitli makale kümesi veya tamsayı sayım — oran ekseni yok."""
    names = [i[name_key] for i in items]
    vals = _ints(i["count"] for i in items)
    fig = go.Figure(_count_bar(names, vals, horizontal=True, unit_key="charts.paper_count"))
    layout = _layout()
    layout.update(
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=_count_axis(x_title or t("charts.paper_count"), vals),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        height=max(360, 28 * max(len(items), 1) + 80),
        bargap=0.28,
        margin=dict(l=40, r=70, t=50, b=40),
    )
    fig.layout.update(layout)
    return fig


def render_country_rank_chart(
    items: List[Dict[str, Any]],
    title: str,
    name_key: str = "name",
) -> go.Figure:
    """İlk 10 çubuk, sonra …, sonra Türkiye sırası. None sayım 0 yazılmaz."""
    unit = t("charts.paper_count")
    hover_n = t("charts.hover_h", unit=unit)
    labels: List[str] = []
    xs: List[Optional[int]] = []
    texts: List[str] = []
    colors: List[str] = []
    hovers: List[str] = []
    counted: List[int] = []
    fallback_i = 0
    for row in items:
        label = str(row.get(name_key) or "")
        labels.append(label)
        if row.get("gap"):
            xs.append(float("nan"))
            texts.append("")
            colors.append("rgba(148, 163, 184, 0.0)")
            hovers.append("<extra></extra>")
            continue
        if row.get("out") or row.get("count") is None:
            xs.append(float("nan"))
            texts.append(t("pub.metric_tr_out"))
            colors.append(TT_BAR)
            hovers.append("%{y}<extra></extra>")
            continue
        n = int(row["count"])
        xs.append(n)
        texts.append(str(n))
        counted.append(n)
        is_tr = str(row.get("cc") or "") == "TR" or "türkiye" in label.casefold()
        if is_tr:
            colors.append(TT_BAR)
        else:
            colors.append(QUALITATIVE_COLORS[fallback_i % len(QUALITATIVE_COLORS)])
            fallback_i += 1
        hovers.append(hover_n)
    fig = go.Figure(
        go.Bar(
            x=xs,
            y=labels,
            orientation="h",
            marker=dict(color=colors),
            text=texts,
            textposition="outside",
            cliponaxis=False,
            hovertemplate=hovers,
        )
    )
    layout = _layout()
    layout.update(
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=_count_axis(t("charts.paper_count"), counted),
        yaxis=dict(
            autorange="reversed",
            categoryorder="array",
            categoryarray=labels,
            gridcolor="rgba(200, 209, 220, 0.1)",
        ),
        height=max(400, 28 * max(len(labels), 1) + 90),
        bargap=0.28,
        margin=dict(l=40, r=110, t=50, b=40),
    )
    fig.layout.update(layout)
    return fig


def render_academic_grouped_bar(
    by_topic: Dict[str, List[Dict[str, Any]]],
    title: str,
    *,
    name_key: str = "name",
) -> go.Figure:
    """Konu başına tamsayı çubuk. Konular toplanmaz; listede yoksa 0 basılmaz."""
    max_by: Dict[str, int] = {}
    for items in by_topic.values():
        for item in items:
            label = str(item.get(name_key) or "").strip()
            if not label:
                continue
            try:
                n = int(item["count"])
            except (TypeError, ValueError, KeyError):
                continue
            max_by[label] = max(max_by.get(label, 0), n)
    labels = sorted(max_by, key=lambda n: (-max_by[n], n))
    fig = go.Figure()
    shown: List[int] = []
    unit = t("charts.paper_count")
    hover = t("charts.hover_h", unit=unit)
    for idx, (topic, items) in enumerate(by_topic.items()):
        lookup = {
            str(item.get(name_key) or "").strip(): int(item["count"])
            for item in items
            if item.get(name_key) and isinstance(item.get("count"), int)
        }
        xs = [lookup.get(lab) for lab in labels]
        shown.extend(v for v in xs if isinstance(v, int))
        fig.add_trace(
            go.Bar(
                name=str(topic),
                x=xs,
                y=labels,
                orientation="h",
                marker=dict(color=QUALITATIVE_COLORS[idx % len(QUALITATIVE_COLORS)]),
                hovertemplate=hover,
            )
        )
    layout = _layout()
    layout.update(
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=_count_axis(t("charts.paper_count"), shown),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        barmode="group",
        bargap=0.22,
        height=max(420, 22 * max(len(labels), 1) + 110),
        legend=dict(orientation="h", y=1.12, font=dict(size=11)),
        margin=dict(l=40, r=40, t=70, b=40),
    )
    fig.layout.update(layout)
    return fig


def render_eu_mno_leader_chart(rows: List[Dict[str, Any]], title: str, x_title: str) -> go.Figure:
    """Türkiye + Avrupa: kilitli 3 MNO içinden en yüksek Springer sayısı."""
    lang = get_lang()
    ordered = sorted(rows, key=lambda r: int(r.get("n") or 0), reverse=True)
    labels: List[str] = []
    vals: List[int] = []
    colors: List[str] = []
    hovers: List[str] = []
    unit = t("charts.paper_count")
    for r in ordered:
        country = str(r.get("name_tr") if lang == "tr" else r.get("name_en") or "")
        firm = str(r.get("firm") or "")
        labels.append(f"{country} · {firm}")
        n = int(r.get("n") or 0)
        vals.append(n)
        colors.append(TT_BAR if r.get("is_tt") or _is_tt_name(firm) else OTHER_BAR)
        hovers.append(f"{country} · {firm}<br>{n} {unit}<extra></extra>")
    fig = go.Figure(
        go.Bar(
            x=vals or [0],
            y=labels or ["—"],
            orientation="h",
            marker=dict(color=colors or [OTHER_BAR]),
            text=[str(v) for v in (vals or [0])],
            textposition="outside",
            cliponaxis=False,
            hovertemplate="%{customdata}<extra></extra>",
            customdata=hovers or ["—"],
        )
    )
    layout = _layout()
    layout.update(
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=_count_axis(x_title, vals or [0]),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        height=max(420, 28 * max(len(ordered), 1) + 90),
        showlegend=False,
        margin=dict(l=40, r=70, t=50, b=40),
    )
    fig.layout.update(layout)
    return fig

