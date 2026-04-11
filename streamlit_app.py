import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


pages = {
    "running": [
        st.Page("pages/running.py", title="running data"),
    ],
}

pg = st.navigation(pages, position="top")