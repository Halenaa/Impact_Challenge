from __future__ import annotations

import streamlit as st

from data.questions import QUESTIONS
from utils.database import init_db, save_profile, save_user
from utils.matching import calculate_scores, get_challenge_type, match_identity


st.set_page_config(page_title="Belonging Profile", page_icon="BI", layout="centered")
init_db()

st.title("Belonging Profile")
st.write("Answer a few questions so the demo can match you with a temporary city identity.")

with st.form("profile_form"):
    nickname = st.text_input("Nickname", placeholder="Choose any name for this pilot")
    email_optional = st.text_input("Email (optional)", placeholder="Only if you want follow-up")
    pre_belonging_score = st.slider("Current belonging score", 1, 10, 5)

    answers: dict[str, str] = {}
    for question in QUESTIONS:
        answers[question["id"]] = st.radio(
            question["label"],
            question["options"],
            key=question["id"],
        )

    submitted = st.form_submit_button("See my borrowed identity", type="primary", width="stretch")

if submitted:
    if not nickname.strip():
        st.error("Please add a nickname before continuing.")
        st.stop()

    scores = calculate_scores(answers)
    challenge_type = get_challenge_type(scores)
    identity_id = match_identity(challenge_type)
    user_id = save_user(nickname, email_optional)
    profile_id = save_profile(
        user_id=user_id,
        answers=answers,
        pre_belonging_score=pre_belonging_score,
        challenge_type=challenge_type,
        identity_id=identity_id,
    )

    st.session_state["user_id"] = user_id
    st.session_state["profile_id"] = profile_id
    st.session_state["nickname"] = nickname.strip()
    st.session_state["pre_belonging_score"] = pre_belonging_score
    st.session_state["answers"] = answers
    st.session_state["scores"] = scores
    st.session_state["challenge_type"] = challenge_type
    st.session_state["identity_id"] = identity_id

    st.switch_page("pages/2_Identity_Result.py")
