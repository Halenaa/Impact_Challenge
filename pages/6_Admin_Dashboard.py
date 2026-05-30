from __future__ import annotations

import os

import pandas as pd
import streamlit as st

from data.identities import IDENTITIES
from utils.database import approve_submission, get_dashboard_data, init_db
from utils.safety import flag_sensitive_content
from utils.ui import configure_page, page_header


configure_page("Admin")
init_db()

page_header("Admin", "Dashboard", "Pilot metrics, wall review, and CSV export for Hastory.")

try:
    configured_password = st.secrets.get("ADMIN_PASSWORD")
except Exception:
    configured_password = None
admin_password = configured_password or os.getenv("ADMIN_PASSWORD", "borrowed-admin")
password = st.text_input("Admin password", type="password")

if password != admin_password:
    st.info("Enter the admin password to view pilot data.")
    st.stop()

data = get_dashboard_data()
users = data["users"]
profiles = data["profiles"]
submissions = data["submissions"]

merged = submissions.merge(
    profiles[["user_id", "pre_belonging_score"]],
    on="user_id",
    how="left",
) if not submissions.empty and not profiles.empty else pd.DataFrame()

average_pre = profiles["pre_belonging_score"].mean() if not profiles.empty else 0
average_post = submissions["post_belonging_score"].mean() if not submissions.empty else 0
average_change = (
    (merged["post_belonging_score"] - merged["pre_belonging_score"]).mean()
    if not merged.empty
    else 0
)

metric_columns = st.columns(4)
metric_columns[0].metric("Participants", len(users))
metric_columns[1].metric("Submissions", len(submissions))
metric_columns[2].metric("Avg pre-belonging", f"{average_pre:.1f}" if average_pre else "0.0")
metric_columns[3].metric("Avg change", f"{average_change:+.1f}" if average_change else "0.0")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Challenge Distribution")
    if profiles.empty:
        st.info("No profile data yet.")
    else:
        challenge_counts = profiles["challenge_type"].value_counts()
        st.bar_chart(challenge_counts)

with right:
    st.subheader("Identity Usage")
    if profiles.empty:
        st.info("No identity data yet.")
    else:
        identity_counts = profiles["identity_id"].map(
            lambda identity_id: IDENTITIES.get(identity_id, {}).get("title", identity_id)
        ).value_counts()
        st.bar_chart(identity_counts)

st.divider()

st.subheader("Before / After Belonging")
if merged.empty:
    st.info("No completed submission data yet.")
else:
    score_frame = merged[["user_id", "pre_belonging_score", "post_belonging_score"]].copy()
    score_frame["change"] = score_frame["post_belonging_score"] - score_frame["pre_belonging_score"]
    st.dataframe(score_frame, width="stretch", hide_index=True)

st.divider()

st.subheader("Review Resonance Wall Submissions")
if submissions.empty:
    st.info("No submissions yet.")
else:
    review_items = submissions[submissions["consent_for_wall"] == 1]
    if review_items.empty:
        st.info("No submissions with wall consent yet.")
    for _, row in review_items.iterrows():
        identity_title = IDENTITIES.get(row["identity_id"], {}).get("title", row["identity_id"])
        flags = flag_sensitive_content(f"{row['reflection_text']} {row['pass_forward_note']}")
        status = "Approved" if row["approved_for_wall"] else "Waiting for review"
        with st.container(border=True):
            st.caption(f"Submission #{row['submission_id']} | {identity_title} | {status}")
            if flags:
                st.warning(f"Review carefully. Sensitive terms flagged: {', '.join(flags)}")
            st.markdown("**Reflection**")
            st.write(row["reflection_text"])
            st.markdown("**Location**")
            st.write(row["location_text"] or "Not provided")
            st.markdown("**Pass-it-forward note**")
            st.write(row["pass_forward_note"] or "Not provided")
            approve_col, hide_col = st.columns(2)
            if approve_col.button("Approve for wall", key=f"approve_{row['submission_id']}"):
                approve_submission(int(row["submission_id"]), True)
                st.rerun()
            if hide_col.button("Hide from wall", key=f"hide_{row['submission_id']}"):
                approve_submission(int(row["submission_id"]), False)
                st.rerun()

st.divider()

st.subheader("Raw Data")
tab_users, tab_profiles, tab_submissions = st.tabs(["Users", "Profiles", "Submissions"])
with tab_users:
    st.dataframe(users, width="stretch", hide_index=True)
    st.download_button("Export users CSV", users.to_csv(index=False), "users.csv", "text/csv")
with tab_profiles:
    st.dataframe(profiles, width="stretch", hide_index=True)
    st.download_button("Export profiles CSV", profiles.to_csv(index=False), "profiles.csv", "text/csv")
with tab_submissions:
    st.dataframe(submissions, width="stretch", hide_index=True)
    st.download_button(
        "Export submissions CSV",
        submissions.to_csv(index=False),
        "submissions.csv",
        "text/csv",
    )
