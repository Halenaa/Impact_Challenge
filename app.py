from __future__ import annotations

import streamlit as st

from utils.database import init_db
from utils.ui import configure_page, flow_card


configure_page("Home")
init_db()

left, right = st.columns([1.22, 0.78], gap="large", vertical_alignment="center")

with left:
    st.markdown(
        """
        <div class="hastory-hero-main">
            <div class="hastory-kicker">Amsterdam belonging pilot</div>
            <h1>Hastory</h1>
            <p class="hastory-lede">
                A role-based belonging experience for international students in Amsterdam.
                Complete a short profile, receive a temporary city identity, try a
                low-pressure mission, and leave a note for the next student.
            </p>
            <div class="hastory-chip-row">
                <span class="hastory-chip">10-15 minute profile</span>
                <span class="hastory-chip">Amsterdam missions</span>
                <span class="hastory-chip">Anonymous wall</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    action_left, action_right = st.columns([0.62, 0.38], gap="medium")
    with action_left:
        if st.button("Start profile", type="primary", width="stretch"):
            st.switch_page("pages/1_Profile_Questionnaire.py")
    with action_right:
        st.page_link(
            "pages/6_Admin_Dashboard.py",
            label="Admin",
            icon=":material/admin_panel_settings:",
        )

with right:
    flow_html = "".join(
        [
            flow_card(1, "Profile", "Answer a short belonging questionnaire."),
            flow_card(2, "Identity", "Receive a temporary city role."),
            flow_card(3, "Mission", "Complete a small offline Amsterdam task."),
            flow_card(4, "Wall", "Read approved anonymous notes from others."),
        ]
    )
    st.markdown(
        f"""
        <div class="hastory-side-panel">
            <div class="hastory-card-label">Experience route</div>
            <h2>One complete pilot loop</h2>
            <div class="hastory-flow">{flow_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="hastory-grid" style="margin-top: 1.4rem;">
        <div class="hastory-card">
            <div class="hastory-card-label">Care boundary</div>
            <h3>Belonging support, not diagnosis</h3>
            <p>
                Hastory uses a belonging profile to match a role-based city task.
                It is not a clinical or therapeutic assessment.
            </p>
        </div>
        <div class="hastory-card">
            <div class="hastory-card-label">Privacy</div>
            <h3>Anonymous by default</h3>
            <p>
                Wall notes are optional, anonymous, and shown only after admin review
                during the pilot.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
