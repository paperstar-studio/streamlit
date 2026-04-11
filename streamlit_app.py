import streamlit as st

pages = {
    "running": [
        st.Page("pages/running.py", title="running data"),
    ],
    "clothes": [
        st.Page("pages/clothes.py", title="digital wardrobe"),
    ],
}


pg = st.navigation(pages, position="top")
pg.run()