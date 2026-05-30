from __future__ import annotations

import streamlit as st

from data.identities import IDENTITIES
from data.tasks import TASKS
from utils.database import init_db, save_submission
from utils.ui import configure_page, page_header


configure_page("Reflection")
init_db()

user_id = st.session_state.get("user_id")
identity_id = st.session_state.get("identity_id")
challenge_type = st.session_state.get("challenge_type")

if not user_id or not identity_id or not challenge_type:
    st.warning("Start with the belonging profile before submitting a reflection.")
    st.page_link("pages/1_Profile_Questionnaire.py", label="Go to questionnaire", icon=":material/arrow_forward:")
    st.stop()

identity = IDENTITIES[identity_id]
task = TASKS[identity["task_id"]]

page_header(
    "Reflection",
    "Submit Reflection",
    "Your reflection is saved for the pilot. Anonymous wall sharing is optional and reviewed first.",
)

form_col, side_col = st.columns([1.25, 0.75], gap="large")

with form_col:
    with st.form("submission_form"):
        what_did_you_do = st.text_area("What did you do?", height=130)
        location_text = st.text_input("Where did you go?", placeholder="Example: near Prinsengracht")
        what_did_you_notice = st.text_area("What did you notice?", height=130)
        how_did_you_feel = st.text_area("How did you feel after the task?", height=130)
        post_belonging_score = st.slider("Belonging score after the task", 1, 10, 5)
        recommendation_score = st.slider("How likely are you to recommend this experience?", 1, 10, 7)
        pass_forward_note = st.text_area(
            "What would you tell the next person with this identity?",
            height=130,
        )
        consent_for_wall = st.checkbox("Yes, this note can be shown anonymously after review.")

        submitted = st.form_submit_button("Submit reflection", type="primary", width="stretch")

with side_col:
    st.markdown(
        f"""
        <div class="hastory-card">
            <div class="hastory-card-label">Current identity</div>
            <h3>{identity["title"]}</h3>
            <p>{task["reflection_prompt"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if submitted:
    required_fields = [what_did_you_do, what_did_you_notice, how_did_you_feel, pass_forward_note]
    if any(not value.strip() for value in required_fields):
        st.error("Please complete the reflection fields before submitting.")
        st.stop()

    reflection_text = "\n\n".join(
        [
            f"What I did: {what_did_you_do.strip()}",
            f"What I noticed: {what_did_you_notice.strip()}",
            f"How I felt: {how_did_you_feel.strip()}",
        ]
    )
    submission_id = save_submission(
        user_id=user_id,
        identity_id=identity_id,
        challenge_type=challenge_type,
        task_id=identity["task_id"],
        reflection_text=reflection_text,
        location_text=location_text,
        pass_forward_note=pass_forward_note,
        post_belonging_score=post_belonging_score,
        recommendation_score=recommendation_score,
        consent_for_wall=consent_for_wall,
    )
    st.session_state["submission_id"] = submission_id
    st.success("Thank you. Your reflection has been saved.")
    st.info("If you chose wall sharing, an admin still needs to approve it before it appears.")
    st.page_link("pages/5_Resonance_Wall.py", label="Visit the resonance wall", icon=":material/arrow_forward:")
