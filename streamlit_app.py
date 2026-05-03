import streamlit as st

pages = {
    "running": [
        st.Page("pages/running.py", title="running data"),
        st.Page("pages/running_upload.py", title="running upload"),
    ],
    "clothes": [
        st.Page("pages/clothes.py", title="digital wardrobe"),
    ],
    "transport": [
        st.Page("pages/transport.py", title="transport as of 2026-4-24"),
    ],
}


pg = st.navigation(pages, position="top")
pg.run()