import streamlit as st

def inject_custom_styles():
    """
    Injects Türk Telekom Corporate Dark Theme CSS.
    Adheres strictly to Microsoft Fluent, Apple HIG, GitHub Dark, and Tesla Dashboard design standards.
    Color Palette:
    - Background: #0E1117
    - Surface: #1A1F2B
    - Primary: #0099FF
    - Secondary: #00C2FF
    - Accent: #00E5FF
    - Success: #00C853
    - Warning: #FFB020
    - Danger: #FF5252
    - Text Primary: #FFFFFF (Headers, bold titles)
    - Text Body: #E2E8F0 (High readability body text)
    - Text Muted: #94A3B8 (Captions, subtitles)
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

        /* Global Defaults */
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            color: #E2E8F0;
            background-color: #0E1117;
            -webkit-font-smoothing: antialiased;
        }

        .stApp {
            background-color: #0E1117;
            background-image: 
                radial-gradient(at 0% 0%, rgba(0, 153, 255, 0.08) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(0, 229, 255, 0.05) 0px, transparent 50%);
            background-attachment: fixed;
        }

        /* Typography Hierarchy (Ensures high contrast & no blurry thin text) */
        h1, h2, h3, h4, h5, h6 {
            color: #FFFFFF !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }

        p, span, li, label {
            color: #E2E8F0;
            font-weight: 400;
        }

        strong, b {
            color: #FFFFFF !important;
            font-weight: 700 !important;
        }

        /* Header Container Banner */
        .tt-header-container {
            background: linear-gradient(135deg, rgba(26, 31, 43, 0.95) 0%, rgba(14, 17, 23, 0.9) 100%);
            border: 1px solid rgba(0, 153, 255, 0.25);
            border-radius: 10px;
            padding: 8px 16px;
            margin-bottom: 8px;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(16px);
        }

        .tt-badge {
            background: linear-gradient(90deg, #0099FF 0%, #00C2FF 100%);
            color: #FFFFFF !important;
            font-weight: 800 !important;
            font-size: 0.58rem;
            letter-spacing: 1.4px;
            padding: 2px 8px;
            border-radius: 12px;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 3px;
            box-shadow: 0 0 8px rgba(0, 153, 255, 0.3);
        }

        .tt-title {
            color: #FFFFFF !important;
            font-size: 1.18rem;
            font-weight: 800 !important;
            margin: 0;
            line-height: 1.15;
        }

        .tt-subtitle {
            color: #CBD5E1;
            font-size: 0.78rem;
            margin-top: 2px;
            margin-bottom: 0;
        }

        .home-intro {
            background: rgba(0, 200, 83, 0.08);
            border: 1px solid rgba(0, 200, 83, 0.4);
            border-radius: 10px;
            padding: 10px 14px;
            margin: 0 0 8px 0;
        }
        .home-intro h4 {
            color: #00C853 !important;
            margin: 0 0 4px 0 !important;
            font-size: 0.95rem !important;
        }
        .home-intro p {
            color: #E2E8F0 !important;
            font-size: 0.82rem !important;
            line-height: 1.42 !important;
            margin: 0 0 6px 0 !important;
        }
        .home-intro p.home-intro-note {
            color: #94A3B8 !important;
            font-size: 0.76rem !important;
            margin: 0 !important;
        }
        .home-cards-head {
            margin: 0 0 6px 0;
        }
        .home-cards-head h3 {
            color: #FFFFFF !important;
            font-size: 1.02rem !important;
            margin: 0 0 2px 0 !important;
            font-weight: 700 !important;
        }
        .home-cards-head p {
            color: #94A3B8 !important;
            font-size: 0.76rem !important;
            margin: 0 !important;
            line-height: 1.35 !important;
        }
        .home-radar-note {
            color: #94A3B8 !important;
            font-size: 0.78rem !important;
            margin: 6px 0 8px 0 !important;
            line-height: 1.45 !important;
        }

        /* Dual Depth Cards (Temel Seviye vs Uzman) */
        .dual-card-beginner {
            background: rgba(0, 200, 83, 0.08);
            border: 1px solid rgba(0, 200, 83, 0.35);
            border-radius: 12px;
            padding: 14px 16px;
            margin-bottom: 10px;
            backdrop-filter: blur(8px);
        }

        .dual-card-beginner h4 {
            color: #00C853 !important;
            margin-top: 0;
            margin-bottom: 6px;
            font-size: 1rem;
        }

        .dual-card-beginner p {
            font-size: 0.9rem;
            line-height: 1.5;
        }

        .teach-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin: 8px 0 18px 0;
        }
        .teach-item {
            background: rgba(0, 229, 255, 0.06);
            border: 1px solid rgba(0, 229, 255, 0.18);
            border-left: 3px solid #00E5FF;
            border-radius: 10px;
            padding: 14px 16px;
        }
        .teach-item p {
            color: #E2E8F0 !important;
            font-size: 0.92rem;
            line-height: 1.6;
            margin: 6px 0 0 0;
        }
        .teach-label {
            color: #00E5FF;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }
        .card-kicker {
            display: block !important;
            width: 100%;
            box-sizing: border-box;
            background: rgba(255, 176, 32, 0.14);
            border: 1px solid rgba(255, 176, 32, 0.4);
            border-left: 4px solid #FFB020;
            color: #FFD37A !important;
            font-size: 0.86rem !important;
            font-weight: 800 !important;
            letter-spacing: 0.01em;
            padding: 6px 10px;
            border-radius: 6px;
            margin: 0 0 8px 0;
            line-height: 1.3;
            text-transform: none;
        }
        @media (max-width: 900px) {
            .teach-grid { grid-template-columns: 1fr; }
        }

        .dual-card-expert {
            background: rgba(0, 153, 255, 0.08);
            border: 1px solid rgba(0, 153, 255, 0.35);
            border-radius: 12px;
            padding: 14px 16px;
            margin-bottom: 10px;
            backdrop-filter: blur(8px);
        }

        .dual-card-expert h4 {
            color: #00C2FF !important;
            margin-top: 0;
            margin-bottom: 6px;
            font-size: 1rem;
        }

        /* Glassmorphism Surface Cards */
        .glass-card {
            background: #1A1F2B;
            border: 1px solid rgba(200, 209, 220, 0.15);
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .home-tech-card {
            min-height: 0 !important;
            padding: 10px 12px !important;
            margin-bottom: 8px !important;
        }
        .home-tech-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2px;
            gap: 6px;
            flex-wrap: wrap;
        }
        .home-tech-icon { font-size: 1.35rem; line-height: 1; }
        .home-tech-acronym {
            color: #FFFFFF !important;
            margin: 0 !important;
            font-size: 0.98rem !important;
            overflow-wrap: anywhere;
        }
        .home-tech-title {
            color: #00C2FF;
            font-size: 0.7rem;
            font-weight: 600;
            margin: 0 0 6px 0;
            overflow-wrap: anywhere;
        }
        .home-tech-blurb {
            color: #E2E8F0 !important;
            font-size: 0.8rem !important;
            line-height: 1.45 !important;
            margin: 0 0 8px 0 !important;
            overflow-wrap: anywhere;
        }
        .home-tech-chips { margin-bottom: 4px; }
        .home-chip {
            background: rgba(0, 153, 255, 0.12);
            color: #00C2FF;
            border: 1px solid rgba(0, 153, 255, 0.3);
            font-size: 0.68rem;
            padding: 2px 7px;
            border-radius: 6px;
            font-weight: 600;
            display: inline-block;
            margin: 2px 2px 2px 0;
            overflow-wrap: anywhere;
        }
        .home-tech-cta {
            padding-top: 5px;
            border-top: 1px solid rgba(255,255,255,0.08);
            font-size: 0.7rem;
            color: #94A3B8;
            overflow-wrap: anywhere;
        }

        .glass-card:hover {
            border-color: rgba(0, 153, 255, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 12px 30px rgba(0, 153, 255, 0.15);
        }

        /* TRL Level Pills */
        .trl-pill {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 16px;
            font-weight: 700 !important;
            font-size: 0.74rem;
            text-align: center;
        }

        .trl-low {
            background: rgba(255, 82, 82, 0.15);
            color: #FF5252 !important;
            border: 1px solid rgba(255, 82, 82, 0.35);
        }

        .trl-mid {
            background: rgba(255, 176, 32, 0.15);
            color: #FFB020 !important;
            border: 1px solid rgba(255, 176, 32, 0.35);
        }

        .trl-high {
            background: rgba(0, 200, 83, 0.15);
            color: #00C853 !important;
            border: 1px solid rgba(0, 200, 83, 0.35);
        }

        /* Formula & Code Blocks */
        .formula-box {
            font-family: 'JetBrains Mono', monospace;
            background: #090C12;
            border: 1px solid #2A3245;
            border-left: 4px solid #00E5FF;
            border-radius: 8px;
            padding: 16px 20px;
            color: #00E5FF !important;
            font-size: 0.92rem;
            margin: 14px 0;
            overflow-x: auto;
        }

        .formula-card {
            background: rgba(0, 229, 255, 0.06);
            border: 1px solid rgba(0, 229, 255, 0.22);
            border-left: 4px solid #00E5FF;
            border-radius: 12px;
            padding: 16px 18px 8px 18px;
            margin: 16px 0 8px 0;
        }

        .term-chip {
            display: inline-block;
            background: rgba(0, 153, 255, 0.16);
            color: #7DD3FC !important;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
            margin: 0 4px 4px 0;
        }

        .symbol-table, .compare-table {
            width: 100%;
            border-collapse: collapse;
            margin: 8px 0 18px 0;
            font-size: 0.86rem;
            background: #121620;
            border-radius: 10px;
            overflow: hidden;
        }
        .symbol-table th, .compare-table th {
            background: #1A2438;
            color: #00E5FF !important;
            text-align: left;
            padding: 10px 12px;
            font-weight: 700;
            border-bottom: 1px solid rgba(0, 229, 255, 0.2);
        }
        .symbol-table td, .compare-table td {
            color: #E2E8F0 !important;
            padding: 9px 12px;
            border-bottom: 1px solid rgba(255,255,255,0.06);
            vertical-align: top;
            line-height: 1.45;
        }
        .symbol-table td.sym {
            font-family: 'JetBrains Mono', monospace;
            color: #00E5FF !important;
            white-space: nowrap;
        }
        .compare-table td:first-child {
            color: #FFFFFF !important;
            font-weight: 700;
            white-space: nowrap;
        }

        /* Sidebar — marka, TR/EN, Temel/Uzman, menü. Telif yok (üst üste binmesin). */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #10151E 0%, #121620 42%, #0E1117 100%);
            border-right: 1px solid rgba(0, 153, 255, 0.14);
        }
        [data-testid="stSidebarContent"] {
            display: flex !important;
            flex-direction: column !important;
            height: 100% !important;
            min-height: 100% !important;
        }
        [data-testid="stSidebarUserContent"] {
            order: 1 !important;
            padding: 4px 8px 8px 8px !important;
        }
        [data-testid="stSidebarNav"] {
            order: 2 !important;
        }
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            gap: 0.55rem !important;
        }

        .tt-sidebar-brand {
            text-align: center;
            padding: 8px 4px 12px 4px;
            margin-bottom: 2px;
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }
        .tt-sidebar-logo {
            background: linear-gradient(135deg, #0099FF 0%, #00C2FF 100%);
            width: 40px;
            height: 40px;
            border-radius: 11px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            box-shadow: 0 0 16px rgba(0, 153, 255, 0.32);
        }
        .tt-sidebar-brand h3 {
            color: #FFFFFF !important;
            margin: 8px 0 0 0 !important;
            font-size: 0.92rem !important;
            font-weight: 700 !important;
            line-height: 1.2 !important;
        }
        .tt-sidebar-brand p {
            color: #7DD8FF !important;
            font-size: 0.66rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.07em;
            text-transform: uppercase;
            margin: 3px 0 0 0 !important;
            line-height: 1.25 !important;
        }
        .tt-sidebar-label {
            color: #94A3B8 !important;
            font-size: 0.66rem !important;
            font-weight: 600 !important;
            letter-spacing: 0.07em;
            text-transform: uppercase;
            display: block !important;
            margin: 12px 2px 10px 2px !important;
            padding: 0 0 2px 0 !important;
            line-height: 1.3 !important;
            position: relative;
            z-index: 2;
        }

        [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] {
            gap: 6px !important;
            background: rgba(255,255,255,0.035);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 11px;
            padding: 4px;
            margin-top: 0.45rem !important;
            margin-bottom: 2px !important;
            position: relative;
            z-index: 1;
        }
        [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] .stButton button {
            min-height: 1.7rem !important;
            height: 1.7rem !important;
            font-size: 0.7rem !important;
            font-weight: 650 !important;
            letter-spacing: 0.03em;
            border-radius: 8px !important;
            padding: 0 4px !important;
        }
        [data-testid="stSidebar"] .stButton button {
            min-height: 2rem !important;
            font-size: 0.78rem !important;
            font-weight: 600 !important;
            letter-spacing: 0;
            border-radius: 8px !important;
            white-space: normal !important;
        }

        [data-testid="stSidebarNav"] {
            border-top: 1px solid rgba(255,255,255,0.07);
            margin-top: 10px !important;
            padding: 8px 6px 8px 6px !important;
            display: flex !important;
            flex-direction: column !important;
            flex: 1 1 auto !important;
        }
        [data-testid="stSidebarNav"]::after {
            content: var(--tt-sidebar-footer, "© 2026 Türk Telekom Ar-Ge");
            display: block;
            order: 99;
            margin-top: 10px;
            padding: 12px 8px 14px;
            text-align: center;
            font-size: 0.65rem;
            font-weight: 500;
            letter-spacing: 0.02em;
            color: #64748B;
            border-top: 1px solid rgba(255,255,255,0.07);
            line-height: 1.35;
        }
        [data-testid="stSidebarNav"] li {
            margin: 0 !important;
        }
        [data-testid="stSidebarNav"] a {
            padding: 0.42rem 0.65rem !important;
            border-radius: 9px !important;
            font-size: 0.84rem !important;
            font-weight: 500 !important;
            line-height: 1.25 !important;
        }
        [data-testid="stSidebarNav"] a,
        [data-testid="stSidebarNav"] span {
            white-space: normal !important;
            line-height: 1.25 !important;
        }
        [data-testid="stSidebarNav"] a:hover {
            background: rgba(0, 153, 255, 0.12) !important;
        }
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background: rgba(0, 153, 255, 0.16) !important;
            font-weight: 650 !important;
        }

        [data-testid="stSidebar"] .stMarkdown {
            margin-bottom: 0.15rem !important;
        }
        [data-testid="stSidebar"] [data-testid="stElementContainer"]:has(.tt-sidebar-label) {
            margin-bottom: 0.15rem !important;
        }

        /* Custom Tabs Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 6px;
            background-color: #121620;
            padding: 6px;
            border-radius: 12px;
            border: 1px solid rgba(200, 209, 220, 0.1);
        }

        .stTabs [data-baseweb="tab"] {
            height: 42px;
            border-radius: 8px;
            color: #CBD5E1;
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.2s ease;
        }

        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #0099FF 0%, #00C2FF 100%) !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            box-shadow: 0 4px 14px rgba(0, 153, 255, 0.35);
        }

        /* Metric Cards */
        [data-testid="stMetricValue"] {
            color: #00E5FF !important;
            font-weight: 700 !important;
        }

        /* Kaynakta Aç butonları */
        div[data-testid="stLinkButton"] a,
        .stLinkButton a {
            background: linear-gradient(135deg, #0099FF 0%, #00C2FF 100%) !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            border: none !important;
            box-shadow: 0 4px 14px rgba(0, 153, 255, 0.35);
            white-space: normal !important;
            overflow-wrap: anywhere;
            text-align: center;
            line-height: 1.3;
        }

        /* i18n: EN/TR length mismatch must not clip or overflow */
        .tt-title, .tt-subtitle, .tt-badge, .glass-card, .glass-card h2, .glass-card h4,
        .dual-card-beginner, .dual-card-expert, .card-kicker, .teach-item p {
            overflow-wrap: anywhere;
            word-break: break-word;
        }
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] label,
        [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {
            overflow-wrap: anywhere;
        }
        .stButton button, [data-testid="stBaseButton-secondary"], [data-testid="stBaseButton-primary"] {
            white-space: normal !important;
            height: auto !important;
            min-height: 2.4rem;
            line-height: 1.3;
        }
        [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] .stButton button,
        [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] [data-testid="stBaseButton-secondary"],
        [data-testid="stSidebar"] [data-testid="stHorizontalBlock"] [data-testid="stBaseButton-primary"] {
            min-height: 1.7rem !important;
            height: 1.7rem !important;
            font-size: 0.7rem !important;
            line-height: 1.2 !important;
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }
        [data-testid="stMetricLabel"], [data-testid="stMetricValue"], [data-testid="stMetricDelta"] {
            overflow-wrap: anywhere;
            white-space: normal !important;
        }
        [data-baseweb="tab"], [data-testid="stPills"] button {
            white-space: normal !important;
            height: auto !important;
        }

        /* Streamlit 1.61: varsayılan ~6rem üst boşluk kartları katlıyor */
        header[data-testid="stHeader"],
        .stAppHeader,
        [data-testid="stHeader"] {
            background: rgba(14, 17, 23, 0.85) !important;
            height: 2.4rem !important;
        }
        [data-testid="stDecoration"] { display: none !important; }
        .stMainBlockContainer,
        [data-testid="stMainBlockContainer"],
        .stMain .block-container,
        section.stMain .block-container,
        div.block-container {
            padding-top: 2.6rem !important;
            padding-bottom: 1.2rem !important;
            padding-left: 1.4rem !important;
            padding-right: 1.4rem !important;
        }
        [data-testid="stMain"] [data-testid="stVerticalBlock"] {
            gap: 0.35rem !important;
        }
        [data-testid="stMain"] .stMarkdown {
            margin-bottom: 0 !important;
        }
        [data-testid="stMain"] h3 {
            margin: 0.1rem 0 0.05rem 0 !important;
            font-size: 1.02rem !important;
        }
        [data-testid="stMain"] [data-testid="stCaptionContainer"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
