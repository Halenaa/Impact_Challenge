from __future__ import annotations

import streamlit as st

from data.identities import IDENTITIES
from utils.database import get_public_wall_posts, init_db


st.set_page_config(page_title="Resonance Wall", page_icon="BI", layout="wide")
init_db()

st.title("Anonymous Resonance Wall")
st.write("You are not the only one. These notes were shared anonymously and approved for the wall.")

posts = get_public_wall_posts()

if posts.empty:
    st.info("No approved notes yet. Once the pilot has reviewed shared reflections, they will appear here.")
    st.stop()

columns = st.columns(3)
for index, post in posts.iterrows():
    identity = IDENTITIES.get(post["identity_id"], {"title": post["identity_id"]})
    with columns[index % 3]:
        with st.container(border=True):
            st.caption(identity["title"])
            st.markdown("**Someone wrote**")
            st.write(post["reflection_text"])
            if post["location_text"]:
                st.markdown("**Location**")
                st.write(post["location_text"])
            if post["pass_forward_note"]:
                st.markdown("**For the next person**")
                st.write(post["pass_forward_note"])
            st.button("I relate", key=f"relate_{post['submission_id']}", width="stretch")
