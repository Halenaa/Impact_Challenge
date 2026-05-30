from __future__ import annotations

import streamlit as st

from utils.database import init_db


st.set_page_config(
    page_title="Borrowed Identity",
    page_icon="BI",
    layout="centered",
)

init_db()

st.title("Borrowed Identity")
st.subheader("A role-based belonging experience for international students in Amsterdam.")

st.write(
    """
    Complete a short belonging profile, receive a temporary city identity,
    try a low-pressure Amsterdam mission, and leave a note for the next student.
    """
)

with st.container(border=True):
    st.markdown("**What happens in this demo**")
    st.write("1. Answer a short profile questionnaire.")
    st.write("2. Receive a borrowed identity and a small city mission.")
    st.write("3. Complete the mission offline, then submit a reflection.")
    st.write("4. Read anonymous notes from students who chose to share them.")

with st.container(border=True):
    st.markdown("**Privacy and care**")
    st.write(
        """
        This is not a diagnosis or clinical tool. Your answers are used only to
        match you with a belonging profile and a role-based task for this pilot.
        Public wall notes are anonymous and shown only after review.
        """
    )

if st.button("Start", type="primary", width="stretch"):
    st.switch_page("pages/1_Profile_Questionnaire.py")

st.page_link("pages/6_Admin_Dashboard.py", label="Admin dashboard", icon=":material/admin_panel_settings:")
