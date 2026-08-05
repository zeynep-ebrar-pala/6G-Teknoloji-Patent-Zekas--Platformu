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
            border-radius: 16px;
            padding: 26px 36px;
            margin-bottom: 28px;
            box-shadow: 0 12px 32px rgba(0, 0, 0, 0.4), 0 0 20px rgba(0, 153, 255, 0.1);
            backdrop-filter: blur(16px);
        }

        .tt-badge {
            background: linear-gradient(90deg, #0099FF 0%, #00C2FF 100%);
            color: #FFFFFF !important;
            font-weight: 800 !important;
            font-size: 0.72rem;
            letter-spacing: 1.8px;
            padding: 4px 14px;
            border-radius: 20px;
            text-transform: uppercase;
            display: inline-block;
            margin-bottom: 12px;
            box-shadow: 0 0 14px rgba(0, 153, 255, 0.4);
        }

        .tt-title {
            color: #FFFFFF !important;
            font-size: 2.2rem;
            font-weight: 800 !important;
            margin: 0;
            line-height: 1.2;
        }

        .tt-subtitle {
            color: #CBD5E1;
            font-size: 1.02rem;
            margin-top: 8px;
            margin-bottom: 0;
        }

        /* Dual Depth Cards (Temel Seviye vs Uzman) */
        .dual-card-beginner {
            background: rgba(0, 200, 83, 0.08);
            border: 1px solid rgba(0, 200, 83, 0.35);
            border-radius: 14px;
            padding: 22px;
            margin-bottom: 20px;
            backdrop-filter: blur(8px);
        }

        .dual-card-beginner h4 {
            color: #00C853 !important;
            margin-top: 0;
            margin-bottom: 12px;
            font-size: 1.1rem;
        }

        .dual-card-expert {
            background: rgba(0, 153, 255, 0.08);
            border: 1px solid rgba(0, 153, 255, 0.35);
            border-radius: 14px;
            padding: 22px;
            margin-bottom: 20px;
            backdrop-filter: blur(8px);
        }

        .dual-card-expert h4 {
            color: #00C2FF !important;
            margin-top: 0;
            margin-bottom: 12px;
            font-size: 1.1rem;
        }

        /* Glassmorphism Surface Cards */
        .glass-card {
            background: #1A1F2B;
            border: 1px solid rgba(200, 209, 220, 0.15);
            border-radius: 14px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .glass-card:hover {
            border-color: rgba(0, 153, 255, 0.4);
            transform: translateY(-2px);
            box-shadow: 0 12px 30px rgba(0, 153, 255, 0.15);
        }

        /* TRL Level Pills */
        .trl-pill {
            display: inline-block;
            padding: 5px 14px;
            border-radius: 20px;
            font-weight: 700 !important;
            font-size: 0.82rem;
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

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #121620;
            border-right: 1px solid rgba(200, 209, 220, 0.08);
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

        /* Hide Default Streamlit Header */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
