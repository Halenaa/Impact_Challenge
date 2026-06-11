from __future__ import annotations

from pathlib import Path

import streamlit as st

from data.identities import CHALLENGE_EXPLANATIONS, IDENTITIES
from utils.ui import configure_page, page_header


configure_page("Identity")

identity_id = st.session_state.get("identity_id")
challenge_type = st.session_state.get("challenge_type")

if not identity_id or not challenge_type:
    st.warning("Start with the belonging profile so this page can show your result.")
    st.page_link("pages/1_Profile_Questionnaire.py", label="Go to questionnaire", icon=":material/arrow_forward:")
    st.stop()

identity = IDENTITIES[identity_id]
showcase_dir = Path(__file__).resolve().parents[1] / "assets" / "showcase"
front_card_path = showcase_dir / f"{identity_id}_front.png"
back_card_path = showcase_dir / f"{identity_id}_back.png"

page_header(
    "Identity match",
    "Your Hastory Identity",
    f"Hi, {st.session_state.get('nickname', 'there')}. This is your Hastory card.",
)

profile_col, identity_col = st.columns([0.9, 1.1], gap="large")
with profile_col:
    st.markdown(
        f"""
        <div class="hastory-card">
            <div class="hastory-card-label">Belonging profile</div>
            <h2>{challenge_type}</h2>
            <p>{CHALLENGE_EXPLANATIONS[challenge_type]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="hastory-card">
            <div class="hastory-card-label">Temporary city role</div>
            <h2>{identity["title"]}</h2>
            <p>{identity["story"]}</p>
            <div class="hastory-chip-row">
                <span class="hastory-chip">{identity["short_description"]}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with identity_col:
    st.markdown('<div class="hastory-card-label">Your issued card</div>', unsafe_allow_html=True)
    if front_card_path.exists() and back_card_path.exists():
        front_tab, back_tab = st.tabs(["Front", "Back"])
        with front_tab:
            st.image(str(front_card_path), use_container_width=True)
        with back_tab:
            st.image(str(back_card_path), use_container_width=True)
    else:
        st.info("Showcase card art for this identity is not available yet.")
        st.markdown(
            f"""
            <div class="hastory-card">
                <div class="hastory-card-label">Temporary city role</div>
                <h2>{identity["title"]}</h2>
                <p>{identity["story"]}</p>
                <div class="hastory-chip-row">
                    <span class="hastory-chip">{identity["short_description"]}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

if st.button("View my task", type="primary", width="stretch"):
    st.switch_page("pages/3_Task_Page.py")
