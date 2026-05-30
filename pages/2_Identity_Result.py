from __future__ import annotations

import streamlit as st

from data.identities import CHALLENGE_EXPLANATIONS, IDENTITIES


st.set_page_config(page_title="Identity Result", page_icon="BI", layout="centered")

st.title("Your Borrowed Identity")

identity_id = st.session_state.get("identity_id")
challenge_type = st.session_state.get("challenge_type")

if not identity_id or not challenge_type:
    st.warning("Start with the belonging profile so this page can show your result.")
    st.page_link("pages/1_Profile_Questionnaire.py", label="Go to questionnaire", icon=":material/arrow_forward:")
    st.stop()

identity = IDENTITIES[identity_id]
st.caption(f"Hi, {st.session_state.get('nickname', 'there')}.")

with st.container(border=True):
    st.markdown("**Your current belonging profile**")
    st.header(challenge_type)
    st.write(CHALLENGE_EXPLANATIONS[challenge_type])

with st.container(border=True):
    st.markdown("**Your borrowed identity**")
    st.header(identity["title"])
    st.write(identity["story"])
    st.info(identity["short_description"])

if st.button("View my task", type="primary", width="stretch"):
    st.switch_page("pages/3_Task_Page.py")
