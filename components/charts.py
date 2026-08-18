"""
Türk Telekom 6G Platform - Plotly & Interactive Chart Components
Adheres to corporate dark theme standards (#0E1117 bg, #1A1F2B surface, #0099FF primary, #00C2FF secondary).
Safe fallback if networkx is missing.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, Any, List, Optional

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


def _hex_rgba(hex_color: str, alpha: float) -> str:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


def _series_color(name: str, index: int = 0) -> str:
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


def _count_axis(title: str) -> dict:
    return dict(
        title=title,
        gridcolor="rgba(200, 209, 220, 0.1)",
        rangemode="tozero",
        tickformat="d",
        separatethousands=False,
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

    fig.update_layout(
        **_layout(),
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
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=labels,
        y=df_counts[y_col],
        marker=dict(color="#00E5FF"),
        name=tech_label,
    ))
    fig.update_layout(
        **_layout(),
        title=dict(
            text=f"<b>{t('charts.tech_counts', label=tech_label)}</b>",
            x=0.02, y=0.95, font=dict(size=14, color="#FFFFFF"),
        ),
        xaxis=_year_axis(labels),
        yaxis=_count_axis(t("charts.count")),
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

    for col, color in zip(companies, colors):
        fig.add_trace(go.Bar(
            x=labels,
            y=df_trends[col],
            name=col,
            marker=dict(color=color, line=dict(width=0)),
        ))

    fig.update_layout(
        **_layout(),
        barmode="group",
        title=dict(text=f"<b>{t('charts.patent_year')}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=_year_axis(labels),
        yaxis=_count_axis(t("charts.patent_count")),
        height=480,
        bargap=0.22,
        bargroupgap=0.08,
    )
    return fig

def render_company_patent_domain_chart(df_domains: pd.DataFrame) -> go.Figure:
    """Renders radar comparison of patent portfolios across companies."""
    fig = go.Figure()
    domains = [c for c in df_domains.columns if c != 'Company']
    shown = df_domains.copy()
    value_cols = [c for c in shown.columns if c != "Company"]
    shown["_tot"] = shown[value_cols].sum(axis=1)
    shown = shown.sort_values("_tot", ascending=False).head(5).drop(columns=["_tot"])
    companies = shown["Company"].tolist()
    colors = _color_list(companies)

    for idx, (_, row) in enumerate(shown.iterrows()):
        company = row['Company']
        color = colors[idx]
        values = [row[d] for d in domains]
        values_closed = values + [values[0]]
        domains_closed = domains + [domains[0]]

        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=domains_closed,
            fill='toself',
            name=company,
            fillcolor=_hex_rgba(color, 0.14),
            line=dict(color=color, width=2.5),
        ))

    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.domain_radar')}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor='rgba(200, 209, 220, 0.15)'),
            angularaxis=dict(gridcolor='rgba(200, 209, 220, 0.15)', tickfont=dict(color='#FFFFFF')),
            bgcolor='#121620'
        ),
        height=440
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

    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.keywords')}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=dict(title=t("charts.kw_x"), gridcolor='rgba(200, 209, 220, 0.1)'),
        yaxis=dict(autorange="reversed", gridcolor='rgba(200, 209, 220, 0.1)'),
        height=380
    )
    return fig

def render_academic_trends_chart(df_academic: pd.DataFrame) -> go.Figure:
    """Renders academic publication volume trends by 6G topic."""
    fig = go.Figure()
    labels = _year_labels(df_academic["Years"])
    topics = [c for c in df_academic.columns if c != "Years"]
    colors = _color_list(topics)
    markers = ["circle", "square", "diamond", "triangle-up", "star", "x", "cross", "hexagon"]

    for idx, (col, color) in enumerate(zip(topics, colors)):
        fig.add_trace(go.Scatter(
            x=labels,
            y=df_academic[col],
            mode="lines+markers",
            name=col,
            line=dict(width=3, color=color),
            marker=dict(size=9, color=color, symbol=markers[idx % len(markers)], line=dict(width=1, color="#FFFFFF")),
        ))

    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.academic_trend')}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=_year_axis(labels),
        yaxis=dict(title=t("charts.pub_count"), gridcolor='rgba(200, 209, 220, 0.1)', rangemode='tozero', tickformat='d'),
        height=480
    )
    return fig

def render_academic_database_chart(
    db_dict: Dict[str, int],
    title: str | None = None,
    xlabel: str | None = None,
) -> go.Figure:
    """Renders bar chart of verified sample paper publisher counts."""
    title = title or t("charts.db_default")
    xlabel = xlabel or t("charts.publisher")
    labels = list(db_dict.keys())
    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=list(db_dict.values()),
        marker=dict(color=_color_list(labels))
    )])
    
    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color='#FFFFFF')),
        xaxis=dict(title=xlabel, type="category", gridcolor='rgba(200, 209, 220, 0.1)'),
        yaxis=_count_axis(t("charts.paper_count")),
        height=360
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

    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.network')}</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=450
    )
    return fig


def render_company_counts_chart(counts: Dict[str, int]) -> go.Figure:
    """En çok kayıtlı firmalar — doğrulanmış küme sayımı."""
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    names = [c for c, _ in sorted_items]
    fig = go.Figure(go.Bar(
        x=names,
        y=[n for _, n in sorted_items],
        marker=dict(color=_color_list(names)),
    ))
    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.company_counts')}</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        xaxis=dict(title=t("charts.company"), gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=dict(title=t("charts.patent_count"), gridcolor="rgba(200, 209, 220, 0.1)"),
        height=360,
    )
    return fig


def render_patent_density_heatmap(df_density: pd.DataFrame) -> go.Figure:
    """Firma × teknoloji alanı yoğunluk ısı haritası."""
    companies = df_density["Company"].tolist()
    domains = [c for c in df_density.columns if c != "Company"]
    z = df_density[domains].values.tolist()
    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=domains,
        y=companies,
        colorscale=[[0, "#121620"], [0.5, "#0066B3"], [1, "#00E5FF"]],
        hoverongaps=False,
    ))
    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.density')}</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        height=max(360, 40 * len(companies) + 120),
    )
    return fig


def render_patent_sunburst(df_tree: pd.DataFrame) -> go.Figure:
    """Firma → alan → patent numarası ağacı."""
    fig = px.sunburst(
        df_tree,
        path=["company", "domain", "patent"],
        color="domain",
        color_discrete_map=DOMAIN_COLORS,
        color_discrete_sequence=QUALITATIVE_COLORS,
    )
    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.sunburst')}</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        height=480,
    )
    fig.update_traces(insidetextorientation="radial")
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
    fig.update_layout(
        **_layout(),
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
    """Yalnızca adı doğrulanmış ülkeler. 19/24 iddiası boyanmaz."""
    df = pd.DataFrame(rows)
    name_col = "name_tr" if lang == "tr" else "name_en"
    label_col = "label_tr" if lang == "tr" else "label_en"
    df["cat"] = df["layer"].map(lambda k: t(f"tt_eu.layer.{k}"))
    df["place"] = df[name_col]
    df["hint"] = df[label_col]
    color_map = {
        t("tt_eu.layer.hq"): "#E20074",
        t("tt_eu.layer.wholesale"): "#00C2FF",
        t("tt_eu.layer.rd_collab"): "#A855F7",
        t("tt_eu.layer.standards"): "#FFB020",
        t("tt_eu.layer.mou_venue"): "#14B8A6",
    }
    fig = px.choropleth(
        df,
        locations="iso3",
        color="cat",
        hover_name="place",
        hover_data={"iso3": False, "cat": True, "hint": True, "place": False},
        color_discrete_map=color_map,
        category_orders={"cat": list(color_map.keys())},
        locationmode="ISO-3",
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
        # Plotly «europe» kapsamı Anadolu’yu keser; TR + UA + SE + ES buraya sığmalı.
        projection_type="natural earth",
        center=dict(lat=48.2, lon=19.5),
        lonaxis_range=[-12, 48],
        lataxis_range=[34, 72],
    )
    layout = _layout()
    layout.update(
        title=dict(text=f"<b>{t('charts.tt_map')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        height=520,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.98,
            xanchor="left",
            x=0.0,
            bgcolor="rgba(18, 22, 32, 0.92)",
            font=dict(color="#FFFFFF", size=11),
        ),
        margin=dict(l=10, r=10, t=50, b=10),
    )
    fig.update_layout(**layout)
    fig.update_traces(marker_line_width=0.6, marker_line_color="rgba(200,209,220,0.35)")
    return fig


def render_tt_role_kind_chart(items: List[Dict[str, Any]]) -> go.Figure:
    """Kanıt türü adedi — pazar payı değil."""
    names = [t(f"tt_eu.layer.{i['id']}") for i in items]
    counts = [i["count"] for i in items]
    fig = go.Figure(go.Bar(
        x=counts,
        y=names,
        orientation="h",
        marker=dict(color=["#E20074", "#00C2FF", "#A855F7", "#FFB020", "#14B8A6", "#64748B"][: len(names)]),
    ))
    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.tt_role')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title=t("charts.tt_role_x"), gridcolor="rgba(200, 209, 220, 0.1)", dtick=1),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        height=max(320, 36 * max(len(items), 1) + 80),
    )
    return fig


def render_tt_vs_vendors_chart(counts: Dict[str, int]) -> go.Figure:
    """Kilitli örnek küme. Küresel pazar veya SEP payı değildir."""
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    names = [c for c, _ in sorted_items]
    fig = go.Figure(go.Bar(
        x=names,
        y=[n for _, n in sorted_items],
        marker=dict(color=_color_list(names)),
    ))
    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.tt_vs_vendors')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title=t("charts.company"), gridcolor="rgba(200, 209, 220, 0.1)", tickangle=-25),
        yaxis=_count_axis(t("charts.patent_count")),
        height=400,
        bargap=0.28,
    )
    return fig


def render_tt_office_chart(counts: Dict[str, int]) -> go.Figure:
    """TT-grup doğrulanmış patentlerin ofis kodu — EP 0 ise 0 basılır."""
    order = ["EP", "US", "TR"]
    names = [k for k in order if k in counts] + [k for k in counts if k not in order]
    fig = go.Figure(go.Bar(
        x=names,
        y=[counts[k] for k in names],
        marker=dict(color="#E20074"),
    ))
    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.tt_office')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title=t("charts.tt_office_x"), gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=_count_axis(t("charts.patent_count")),
        height=340,
        bargap=0.35,
    )
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
    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{t('charts.tt_europe')}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title=t("charts.tt_europe_x"), gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        height=max(320, 36 * max(len(items), 1) + 80),
    )
    return fig


def render_academic_bar_chart(items: List[Dict[str, Any]], title: str, name_key: str = "name") -> go.Figure:
    """Kurum veya ülke yayın sayımı (OpenAlex group_by)."""
    names = [i[name_key] for i in items]
    counts = [i["count"] for i in items]
    fig = go.Figure(go.Bar(
        x=counts,
        y=names,
        orientation="h",
        marker=dict(color=_color_list(names)),
    ))
    fig.update_layout(
        **_layout(),
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title=t("charts.oa_bar_x"), gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        height=max(360, 28 * len(items) + 80),
    )
    return fig

