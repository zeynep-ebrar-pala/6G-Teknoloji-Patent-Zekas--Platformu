"""
Türk Telekom 6G Platform - Plotly & Interactive Chart Components
Adheres to corporate dark theme standards (#0E1117 bg, #1A1F2B surface, #0099FF primary, #00C2FF secondary).
Safe fallback if networkx is missing.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, Any, List, Optional

# Defensive import for networkx
try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False

# Corporate Dark Layout Template
DARK_LAYOUT_TEMPLATE = dict(
    paper_bgcolor='#1A1F2B',
    plot_bgcolor='#1A1F2B',
    font=dict(family='Inter, sans-serif', color='#C8D1DC', size=12),
    margin=dict(l=40, r=40, t=50, b=40),
    legend=dict(
        bgcolor='rgba(18, 22, 32, 0.8)',
        bordercolor='rgba(200, 209, 220, 0.1)',
        font=dict(color='#FFFFFF')
    )
)


def _year_labels(years) -> List[str]:
    """Takvim yılını 2024.2 gibi ondalığa çevirmeden etiketler."""
    return [str(int(y)) for y in years]


def _year_axis(labels: List[str]) -> dict:
    return dict(
        title="Takvim yılı",
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
    """Renders TRL Radar Chart for 6G technologies."""
    categories = [tech["acronym"] for tech in technologies_data.values()]
    trl_values = [tech["trl"] for tech in technologies_data.values()]

    # Close the radar loop
    categories_closed = categories + [categories[0]]
    trl_values_closed = trl_values + [trl_values[0]]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=trl_values_closed,
        theta=categories_closed,
        fill='toself',
        name='TRL Seviyesi',
        fillcolor='rgba(0, 153, 255, 0.25)',
        line=dict(color='#00E5FF', width=3),
        marker=dict(size=8, color='#0099FF', symbol='circle')
    ))

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>6G Teknoloji Hazırlık Seviyeleri (TRL 1-9 Radar)</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 9],
                tickvals=[1, 3, 5, 7, 9],
                gridcolor='rgba(200, 209, 220, 0.15)',
                linecolor='rgba(200, 209, 220, 0.2)',
                tickfont=dict(color='#94A3B8')
            ),
            angularaxis=dict(
                gridcolor='rgba(200, 209, 220, 0.15)',
                linecolor='rgba(200, 209, 220, 0.2)',
                tickfont=dict(color='#FFFFFF', size=13)
            ),
            bgcolor='#121620'
        ),
        showlegend=False,
        height=380
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
        **DARK_LAYOUT_TEMPLATE,
        title=dict(
            text=f"<b>Doğrulanmış {tech_label} Patent Kayıt Sayısı / Yıl</b>",
            x=0.02, y=0.95, font=dict(size=14, color="#FFFFFF"),
        ),
        xaxis=_year_axis(labels),
        yaxis=_count_axis("Kayıt sayısı"),
        height=320,
        bargap=0.35,
    )
    return fig

def render_patent_trends_chart(df_trends: pd.DataFrame) -> go.Figure:
    """Yıllık patent kayıtları — kategorik takvim yılı (2024.2 üretilmez)."""
    fig = go.Figure()
    colors = ['#0099FF', '#00E5FF', '#00C853', '#FFB020', '#FF5252', '#9333EA', '#EC4899', '#64748B']
    labels = _year_labels(df_trends["Years"])

    for idx, col in enumerate(df_trends.columns):
        if col == "Years":
            continue
        fig.add_trace(go.Bar(
            x=labels,
            y=df_trends[col],
            name=col,
            marker=dict(color=colors[idx % len(colors)]),
        ))

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        barmode="group",
        title=dict(text="<b>Yıllara Göre 6G Patent Kayıt Sayısı (doğrulanmış küme)</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=_year_axis(labels),
        yaxis=_count_axis("Patent kayıt sayısı"),
        height=420,
        bargap=0.25,
    )
    return fig

def render_company_patent_domain_chart(df_domains: pd.DataFrame) -> go.Figure:
    """Renders radar comparison of patent portfolios across companies."""
    fig = go.Figure()
    domains = [c for c in df_domains.columns if c != 'Company']
    
    colors = ['#0099FF', '#00E5FF', '#00C853', '#FFB020', '#FF5252']
    
    for idx, (_, row) in enumerate(df_domains.head(5).iterrows()):
        company = row['Company']
        values = [row[d] for d in domains]
        values_closed = values + [values[0]]
        domains_closed = domains + [domains[0]]
        
        fig.add_trace(go.Scatterpolar(
            r=values_closed,
            theta=domains_closed,
            fill='toself',
            name=company,
            fillcolor=f"rgba({int(colors[idx][1:3],16)}, {int(colors[idx][3:5],16)}, {int(colors[idx][5:7],16)}, 0.15)",
            line=dict(color=colors[idx], width=2)
        ))

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Firma Bazlı 6G Teknoloji Yetkinlik Dağılımı (%)</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
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
        marker=dict(
            color=list(sorted_kw.values()),
            colorscale=[[0, '#0066B3'], [1, '#00E5FF']]
        )
    ))

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Patent İstemlerinde En Sık Geçen Anahtar Kelimeler</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=dict(title="Geçtiği İstem Sayısı", gridcolor='rgba(200, 209, 220, 0.1)'),
        yaxis=dict(autorange="reversed", gridcolor='rgba(200, 209, 220, 0.1)'),
        height=380
    )
    return fig

def render_academic_trends_chart(df_academic: pd.DataFrame) -> go.Figure:
    """Renders academic publication volume trends by 6G topic."""
    fig = go.Figure()
    colors = ['#0099FF', '#00E5FF', '#00C853', '#FFB020', '#FF5252', '#9333EA']
    
    labels = _year_labels(df_academic["Years"])
    for idx, col in enumerate(df_academic.columns):
        if col != "Years":
            fig.add_trace(go.Scatter(
                x=labels,
                y=df_academic[col],
                mode='lines+markers',
                name=col,
                line=dict(width=2.5, color=colors[idx % len(colors)])
            ))

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Akademik Yayın Sayıları Trendi (OpenAlex, konu bazlı)</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=_year_axis(labels),
        yaxis=dict(title="Yayın Sayısı", gridcolor='rgba(200, 209, 220, 0.1)', rangemode='tozero', tickformat='d'),
        height=400
    )
    return fig

def render_academic_database_chart(
    db_dict: Dict[str, int],
    title: str = "Doğrulanmış Örnek Set — Yayıncı Sayısı",
    xlabel: str = "Yayıncı",
) -> go.Figure:
    """Renders bar chart of verified sample paper publisher counts."""
    labels = list(db_dict.keys())
    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=list(db_dict.values()),
        marker=dict(color=['#0099FF', '#00C2FF', '#00E5FF', '#00C853'][:len(db_dict)])
    )])
    
    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color='#FFFFFF')),
        xaxis=dict(title=xlabel, type="category", gridcolor='rgba(200, 209, 220, 0.1)'),
        yaxis=_count_axis("Makale sayısı"),
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
            G.add_node(domain, size=18, color="#0099FF")
            G.add_edge("6G Core", domain)

        for assignee in assignee_nodes:
            G.add_node(assignee, size=15, color="#00C853")

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
            text="NetworkX yüklü değil; ağ grafiği gösterilemiyor.",
            showarrow=False,
            font=dict(color="#94A3B8"),
        )

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Assignee ↔ Teknoloji Alanı Ağ Grafiği</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=450
    )
    return fig


def render_company_counts_chart(counts: Dict[str, int]) -> go.Figure:
    """En çok kayıtlı firmalar — doğrulanmış küme sayımı."""
    sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    fig = go.Figure(go.Bar(
        x=[c for c, _ in sorted_items],
        y=[n for _, n in sorted_items],
        marker=dict(color="#0099FF"),
    ))
    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>En Çok Kayıtlı Firmalar (doğrulanmış küme)</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        xaxis=dict(title="Firma", gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=dict(title="Patent kayıt sayısı", gridcolor="rgba(200, 209, 220, 0.1)"),
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
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Patent Yoğunluğu (firma × alan, kayıt sayısı)</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
        height=max(360, 40 * len(companies) + 120),
    )
    return fig


def render_patent_sunburst(df_tree: pd.DataFrame) -> go.Figure:
    """Firma → alan → patent numarası ağacı."""
    fig = px.sunburst(
        df_tree,
        path=["company", "domain", "patent"],
        color="domain",
        color_discrete_sequence=["#0099FF", "#00E5FF", "#00C853", "#FFB020", "#FF5252", "#9333EA", "#EC4899"],
    )
    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Patent Ağacı (firma → alan → kayıt)</b>", x=0.02, y=0.95, font=dict(size=16, color="#FFFFFF")),
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
        color_discrete_sequence=["#0099FF", "#00E5FF", "#00C853", "#FFB020", "#FF5252", "#9333EA", "#EC4899"],
    )
    fig.update_traces(marker=dict(size=12, line=dict(width=1, color="#FFFFFF")))
    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Patent Teknoloji Haritası (TF-IDF + PCA, başlık vektörleri)</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
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
        colormap="Blues",
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


def render_academic_bar_chart(items: List[Dict[str, Any]], title: str, name_key: str = "name") -> go.Figure:
    """Kurum veya ülke yayın sayımı (OpenAlex group_by)."""
    names = [i[name_key] for i in items]
    counts = [i["count"] for i in items]
    fig = go.Figure(go.Bar(
        x=counts,
        y=names,
        orientation="h",
        marker=dict(color="#00C2FF"),
    ))
    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text=f"<b>{title}</b>", x=0.02, y=0.95, font=dict(size=15, color="#FFFFFF")),
        xaxis=dict(title="Yayın sayısı (OpenAlex)", gridcolor="rgba(200, 209, 220, 0.1)"),
        yaxis=dict(autorange="reversed", gridcolor="rgba(200, 209, 220, 0.1)"),
        height=max(360, 28 * len(items) + 80),
    )
    return fig

