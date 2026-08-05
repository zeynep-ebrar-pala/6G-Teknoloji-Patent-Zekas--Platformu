"""
Türk Telekom 6G Platform - Plotly & Interactive Chart Components
Adheres to corporate dark theme standards (#0E1117 bg, #1A1F2B surface, #0099FF primary, #00C2FF secondary).
Safe fallback if networkx is missing.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import Dict, Any, List

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

def render_technology_performance_chart(tech_id: str) -> go.Figure:
    """Renders performance metric comparison chart for a selected tech."""
    metrics_map = {
        "isac": {"Target 6G": 100, "5G Baseline": 10, "Unit": "Geniş Bant Sinyal (GHz)"},
        "ris": {"Target 6G": 95, "5G Baseline": 20, "Unit": "Kapsama Artışı (%)"},
        "cell_free": {"Target 6G": 99.9, "5G Baseline": 90, "Unit": "Hücre Kenarı Deneyimi (%)"},
        "thz": {"Target 6G": 1000, "5G Baseline": 20, "Unit": "Veri Hızı (Gbps)"},
        "ai_ran": {"Target 6G": 40, "5G Baseline": 5, "Unit": "Enerji Tasarrufu (%)"},
        "ntn": {"Target 6G": 100, "5G Baseline": 60, "Unit": "Küresel Kapsama (%)"},
        "ambient_iot": {"Target 6G": 0.001, "5G Baseline": 10, "Unit": "Güç Tüketimi (mW)"}
    }
    
    data = metrics_map.get(tech_id, {"Target 6G": 100, "5G Baseline": 20, "Unit": "Skor"})
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["5G Mevcut Durum", "6G Hedeflenen Performans"],
        y=[data["5G Baseline"], data["Target 6G"]],
        marker=dict(color=['#0066B3', '#00E5FF']),
        text=[f"{data['5G Baseline']} {data['Unit']}", f"{data['Target 6G']} {data['Unit']}"],
        textposition='auto',
        width=0.4
    ))

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text=f"<b>5G vs 6G Kıyaslama Metriği ({data['Unit']})</b>", x=0.02, y=0.95, font=dict(size=14, color='#FFFFFF')),
        yaxis=dict(gridcolor='rgba(200, 209, 220, 0.1)'),
        height=320
    )
    return fig

def render_patent_trends_chart(df_trends: pd.DataFrame) -> go.Figure:
    """Renders annual patent trends across major telecom companies."""
    fig = go.Figure()
    colors = ['#0099FF', '#00E5FF', '#00C853', '#FFB020', '#FF5252', '#9333EA', '#EC4899', '#64748B']
    
    years = df_trends["Years"]
    for idx, col in enumerate(df_trends.columns):
        if col != "Years":
            fig.add_trace(go.Scatter(
                x=years,
                y=df_trends[col],
                mode='lines+markers',
                name=col,
                line=dict(width=2.5, color=colors[idx % len(colors)]),
                marker=dict(size=6)
            ))

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Yıllara Göre 6G Patent Başvuru Trendi (2020-2026)</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=dict(title="Yıl", gridcolor='rgba(200, 209, 220, 0.1)'),
        yaxis=dict(title="Kumülatif Patent Sayısı", gridcolor='rgba(200, 209, 220, 0.1)'),
        height=420
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
            radialaxis=dict(visible=True, range=[0, 30], gridcolor='rgba(200, 209, 220, 0.15)'),
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
    
    years = df_academic["Years"]
    for idx, col in enumerate(df_academic.columns):
        if col != "Years":
            fig.add_trace(go.Scatter(
                x=years,
                y=df_academic[col],
                mode='lines+markers',
                name=col,
                line=dict(width=2.5, color=colors[idx % len(colors)])
            ))

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Akademik Yayın Sayıları Trendi (Konu Bazlı 2020-2026)</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        xaxis=dict(title="Yıl", gridcolor='rgba(200, 209, 220, 0.1)'),
        yaxis=dict(title="Yayın Sayısı", gridcolor='rgba(200, 209, 220, 0.1)'),
        height=400
    )
    return fig

def render_academic_database_chart(db_dict: Dict[str, float]) -> go.Figure:
    """Renders donut chart of database indexing shares."""
    fig = go.Figure(data=[go.Pie(
        labels=list(db_dict.keys()),
        values=list(db_dict.values()),
        hole=.45,
        marker=dict(colors=['#0099FF', '#00C2FF', '#00E5FF', '#00C853'])
    )])
    
    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>Veritabanı Bazında Akademik Yayın Payı (%)</b>", x=0.02, y=0.95, font=dict(size=15, color='#FFFFFF')),
        height=360
    )
    return fig

def render_patent_network_graph() -> go.Figure:
    """Renders interactive technology and patent citation graph using NetworkX or Plotly fallback."""
    if HAS_NETWORKX:
        G = nx.Graph()
        
        # Nodes: Tech Domains & Key Assignees
        G.add_node("6G Core", size=25, color="#00E5FF")
        G.add_node("ISAC", size=18, color="#0099FF")
        G.add_node("RIS", size=18, color="#0099FF")
        G.add_node("NTN", size=18, color="#0099FF")
        G.add_node("Huawei", size=15, color="#00C853")
        G.add_node("Qualcomm", size=15, color="#00C853")
        G.add_node("Ericsson", size=15, color="#00C853")
        G.add_node("Nokia", size=15, color="#00C853")
        G.add_node("Türk Telekom Ar-Ge", size=20, color="#FFB020")
        
        # Edges
        edges = [
            ("6G Core", "ISAC"), ("6G Core", "RIS"), ("6G Core", "NTN"),
            ("ISAC", "Huawei"), ("ISAC", "Qualcomm"), ("RIS", "Nokia"),
            ("RIS", "Qualcomm"), ("NTN", "Ericsson"), ("RIS", "Türk Telekom Ar-Ge"),
            ("ISAC", "Türk Telekom Ar-Ge")
        ]
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
        # Fallback direct Plotly scatter graph if networkx is loading
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=[0, 1, -1, 0, 2, -2],
            y=[0, 1, 1, -1, -2, -2],
            mode='markers+text',
            text=["6G Core", "ISAC", "RIS", "Türk Telekom Ar-Ge", "Huawei", "Qualcomm"],
            marker=dict(size=[25, 18, 18, 20, 15, 15], color=['#00E5FF', '#0099FF', '#0099FF', '#FFB020', '#00C853', '#00C853'])
        ))

    fig.update_layout(
        **DARK_LAYOUT_TEMPLATE,
        title=dict(text="<b>6G Patent & Teknoloji Lisanslama Bağlantı Ağacı (Network Graph)</b>", x=0.02, y=0.95, font=dict(size=16, color='#FFFFFF')),
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        height=450
    )
    return fig
