from __future__ import annotations

import streamlit as st


NAV_ITEMS = [
    ("Home", "app.py", ":material/home:"),
    ("Profile", "pages/1_Profile_Questionnaire.py", ":material/radar:"),
    ("Identity", "pages/2_Identity_Result.py", ":material/id_card:"),
    ("Mission", "pages/3_Task_Page.py", ":material/explore:"),
    ("Reflection", "pages/4_Submit_Reflection.py", ":material/edit_note:"),
    ("Wall", "pages/5_Resonance_Wall.py", ":material/forum:"),
    ("Admin", "pages/6_Admin_Dashboard.py", ":material/monitoring:"),
]


def configure_page(title: str) -> None:
    st.set_page_config(
        page_title=f"{title} | Hastory",
        page_icon="H",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    apply_theme()
    render_sidebar()


def apply_theme() -> None:
    st.markdown(
        """
        <style>
        :root {
            --hastory-ink: #23242f;
            --hastory-muted: #666b78;
            --hastory-soft: #f6f3ee;
            --hastory-panel: #ffffff;
            --hastory-panel-strong: #fff8f3;
            --hastory-coral: #f2554b;
            --hastory-coral-dark: #d83f35;
            --hastory-teal: #1f8a83;
            --hastory-line: rgba(35, 36, 47, 0.12);
            --hastory-shadow: 0 22px 70px rgba(35, 36, 47, 0.08);
        }

        html, body, [class*="css"] {
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }

        .stApp {
            background:
                radial-gradient(circle at top right, rgba(31, 138, 131, 0.10), transparent 32rem),
                linear-gradient(135deg, #fbfaf7 0%, #f3f7f6 48%, #fffdfb 100%);
            color: var(--hastory-ink);
        }

        .main .block-container {
            max-width: 1480px;
            padding: 4.2rem 5vw 6rem;
        }

        [data-testid="stSidebar"] {
            background: #fbfaf7;
            border-right: 1px solid var(--hastory-line);
            box-shadow: 16px 0 40px rgba(35, 36, 47, 0.04);
            min-width: 300px;
        }

        [data-testid="stSidebarNav"] {
            display: none;
        }

        [data-testid="stSidebarUserContent"] {
            padding: 2rem 1.2rem 2rem;
        }

        .hastory-sidebar-brand {
            padding: 1.2rem 1rem 1.4rem;
            margin-bottom: 1rem;
            border-bottom: 1px solid var(--hastory-line);
        }

        .hastory-logo {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 3.2rem;
            height: 3.2rem;
            border-radius: 1rem;
            background: var(--hastory-ink);
            color: white;
            font-size: 1.35rem;
            font-weight: 900;
            letter-spacing: 0;
            margin-bottom: 0.9rem;
        }

        .hastory-sidebar-brand h2 {
            margin: 0;
            color: var(--hastory-ink);
            font-size: 1.65rem;
            line-height: 1.05;
            letter-spacing: 0;
        }

        .hastory-sidebar-brand p {
            margin: 0.45rem 0 0;
            color: var(--hastory-muted);
            font-size: 1rem;
            line-height: 1.35;
        }

        section[data-testid="stSidebar"] a {
            min-height: 3.05rem;
            border-radius: 0.95rem;
            color: var(--hastory-ink) !important;
            font-size: 1.05rem !important;
            font-weight: 750 !important;
            margin: 0.18rem 0;
            padding: 0.35rem 0.55rem !important;
        }

        section[data-testid="stSidebar"] a:hover {
            background: rgba(242, 85, 75, 0.09);
            color: var(--hastory-coral-dark) !important;
        }

        section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            font-size: 1rem;
        }

        h1 {
            color: var(--hastory-ink);
            font-size: clamp(3.2rem, 5vw, 6.2rem) !important;
            line-height: 0.96 !important;
            letter-spacing: 0 !important;
            margin-bottom: 1rem !important;
        }

        h2 {
            font-size: clamp(2rem, 3vw, 3.1rem) !important;
            line-height: 1.05 !important;
            letter-spacing: 0 !important;
        }

        h3 {
            font-size: clamp(1.45rem, 2vw, 2rem) !important;
            letter-spacing: 0 !important;
        }

        p, li, label, [data-testid="stMarkdownContainer"] {
            font-size: 1.08rem;
            line-height: 1.68;
        }

        .hastory-page {
            width: 100%;
        }

        .hastory-hero {
            display: grid;
            grid-template-columns: minmax(0, 1.15fr) minmax(360px, 0.85fr);
            gap: clamp(1.4rem, 4vw, 4rem);
            align-items: stretch;
            min-height: calc(100vh - 8.4rem);
        }

        .hastory-hero-main {
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: clamp(1rem, 3vw, 2.4rem) 0;
        }

        .hastory-kicker {
            display: inline-flex;
            width: fit-content;
            align-items: center;
            gap: 0.55rem;
            border: 1px solid var(--hastory-line);
            background: rgba(255, 255, 255, 0.72);
            border-radius: 999px;
            padding: 0.52rem 0.9rem;
            color: var(--hastory-teal);
            font-weight: 800;
            font-size: 0.95rem;
            margin-bottom: 1.3rem;
        }

        .hastory-lede {
            max-width: 760px;
            color: var(--hastory-muted);
            font-size: clamp(1.2rem, 1.7vw, 1.55rem);
            line-height: 1.55;
            margin: 0 0 2rem;
        }

        .hastory-actions {
            display: grid;
            grid-template-columns: minmax(180px, 260px) minmax(180px, 260px);
            gap: 0.9rem;
            align-items: center;
            margin-top: 1.5rem;
        }

        .hastory-side-panel,
        .hastory-panel {
            border: 1px solid var(--hastory-line);
            background: rgba(255, 255, 255, 0.78);
            border-radius: 1.35rem;
            box-shadow: var(--hastory-shadow);
        }

        .hastory-side-panel {
            padding: clamp(1.4rem, 3vw, 2.2rem);
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .hastory-flow {
            display: grid;
            gap: 0.85rem;
            margin-top: 1.25rem;
        }

        .hastory-flow-item {
            display: grid;
            grid-template-columns: 2.2rem 1fr;
            gap: 0.9rem;
            align-items: start;
            padding: 1rem;
            border-radius: 1rem;
            background: rgba(246, 243, 238, 0.72);
        }

        .hastory-step {
            width: 2.2rem;
            height: 2.2rem;
            border-radius: 999px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background: var(--hastory-coral);
            color: white;
            font-weight: 900;
        }

        .hastory-flow-item strong {
            display: block;
            color: var(--hastory-ink);
            font-size: 1.05rem;
            margin-bottom: 0.15rem;
        }

        .hastory-flow-item span {
            color: var(--hastory-muted);
            font-size: 0.98rem;
            line-height: 1.42;
        }

        .hastory-chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.7rem;
            margin: 1rem 0 0;
        }

        .hastory-chip {
            border-radius: 999px;
            padding: 0.52rem 0.82rem;
            background: rgba(31, 138, 131, 0.10);
            color: #12645f;
            font-weight: 800;
            font-size: 0.95rem;
        }

        .hastory-header {
            max-width: 980px;
            margin-bottom: 2rem;
        }

        .hastory-header p {
            color: var(--hastory-muted);
            font-size: clamp(1.15rem, 1.5vw, 1.38rem);
            line-height: 1.55;
            margin-top: 0.6rem;
        }

        .hastory-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 1.2rem;
        }

        .hastory-card {
            border: 1px solid var(--hastory-line);
            background: rgba(255, 255, 255, 0.82);
            border-radius: 1.2rem;
            padding: clamp(1.2rem, 2vw, 1.8rem);
            box-shadow: var(--hastory-shadow);
        }

        .hastory-card-label {
            color: var(--hastory-teal);
            font-weight: 900;
            text-transform: uppercase;
            font-size: 0.78rem;
            letter-spacing: 0.08em;
            margin-bottom: 0.8rem;
        }

        .hastory-card h2,
        .hastory-card h3,
        .hastory-side-panel h2 {
            margin-top: 0 !important;
        }

        .hastory-card p {
            color: var(--hastory-muted);
            margin-bottom: 0;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 1.2rem !important;
            background: rgba(255, 255, 255, 0.84) !important;
            box-shadow: var(--hastory-shadow);
        }

        .stButton > button,
        .stDownloadButton > button,
        .stFormSubmitButton > button,
        .stLinkButton > a {
            min-height: 3.35rem;
            border-radius: 1rem !important;
            font-size: 1.05rem !important;
            font-weight: 850 !important;
            border: 1px solid rgba(35, 36, 47, 0.12) !important;
        }

        .stButton > button[kind="primary"],
        .stFormSubmitButton > button[kind="primary"] {
            background: var(--hastory-coral) !important;
            border-color: var(--hastory-coral) !important;
            color: white !important;
            box-shadow: 0 16px 34px rgba(242, 85, 75, 0.22);
        }

        .stButton > button[kind="primary"]:hover,
        .stFormSubmitButton > button[kind="primary"]:hover {
            background: var(--hastory-coral-dark) !important;
            border-color: var(--hastory-coral-dark) !important;
        }

        .stTextInput input,
        .stTextArea textarea {
            border-radius: 0.95rem !important;
            min-height: 3rem;
            font-size: 1.05rem !important;
        }

        .stRadio label,
        .stCheckbox label,
        .stSlider label,
        .stTextInput label,
        .stTextArea label {
            font-size: 1.02rem !important;
            font-weight: 760 !important;
            color: var(--hastory-ink) !important;
        }

        div[role="radiogroup"] label {
            padding: 0.42rem 0;
        }

        [data-testid="stMetric"] {
            border: 1px solid var(--hastory-line);
            border-radius: 1.1rem;
            padding: 1.1rem 1.25rem;
            background: rgba(255, 255, 255, 0.84);
            box-shadow: var(--hastory-shadow);
        }

        @media (max-width: 1100px) {
            .main .block-container {
                padding: 2.5rem 1.4rem 4rem;
            }

            .hastory-hero,
            .hastory-grid {
                grid-template-columns: 1fr;
                min-height: auto;
            }

            .hastory-actions {
                grid-template-columns: 1fr;
            }
        }

        @media (max-width: 720px) {
            [data-testid="stSidebar"] {
                min-width: 260px;
            }

            .main .block-container {
                padding: 1.4rem 1rem 3rem;
            }

            h1 {
                font-size: clamp(2.6rem, 14vw, 4.1rem) !important;
            }

            .hastory-lede {
                font-size: 1.12rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar() -> None:
    with st.sidebar:
        st.markdown(
            """
            <div class="hastory-sidebar-brand">
                <div class="hastory-logo">H</div>
                <h2>Hastory</h2>
                <p>Amsterdam belonging pilot</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for label, target, icon in NAV_ITEMS:
            st.page_link(target, label=label, icon=icon)


def page_header(kicker: str, title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="hastory-header">
            <div class="hastory-kicker">{kicker}</div>
            <h1>{title}</h1>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def flow_card(number: int, title: str, body: str) -> str:
    return (
        '<div class="hastory-flow-item">'
        f'<div class="hastory-step">{number}</div>'
        f"<div><strong>{title}</strong><span>{body}</span></div>"
        "</div>"
    )
