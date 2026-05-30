from __future__ import annotations

import streamlit as st

from data.identities import IDENTITIES
from data.tasks import TASKS
from utils.ui import configure_page, page_header


configure_page("Mission")

identity_id = st.session_state.get("identity_id")
if not identity_id:
    st.warning("Start with the belonging profile so this page can show your task.")
    st.page_link("pages/1_Profile_Questionnaire.py", label="Go to questionnaire", icon=":material/arrow_forward:")
    st.stop()

identity = IDENTITIES[identity_id]
task = TASKS[identity["task_id"]]
st.session_state["task_id"] = identity["task_id"]

page_header("Mission", task["title"], identity["story"])

left, right = st.columns([1.1, 0.9], gap="large")

with left:
    with st.container(border=True):
        st.markdown("**Mission**")
        st.write(task["mission"])
    with st.container(border=True):
        st.markdown("**Reflection prompt**")
        st.write(task["reflection_prompt"])
        st.markdown("**Pass-it-forward prompt**")
        st.write(task["pass_forward_prompt"])

with right:
    with st.container(border=True):
        st.markdown("**Where to go**")
        st.write(task["location"])
        st.link_button("Open Google Maps", task["maps_url"], width="stretch")
    with st.container(border=True):
        st.markdown("**Safety note**")
        st.write(task["safety_note"])

if st.button("I completed this task", type="primary", width="stretch"):
    st.switch_page("pages/4_Submit_Reflection.py")
