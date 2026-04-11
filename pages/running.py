# ADD per day km and per day min / month breakdown june.29.2025

import os
import toml
import pandas as pd
import streamlit as st
from utils import socials_get
import plotly.express as px
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from sqlalchemy import create_engine
from st_social_media_links import SocialMediaIcons

st.set_page_config( page_title="paperstar studio", page_icon=":shark:", )

toggle_value = True

with st.sidebar:
    st.markdown("""<h5 style="text-align: center">socials</h5>""", unsafe_allow_html=True)
    SocialMediaIcons(socials_get()).render(sidebar=True, justify_content="space-evenly")
    if 'selection' not in st.session_state:
        st.session_state.selection = 'dark'
    if 'selection_index' not in st.session_state:
        st.session_state.selection_index = 1

session_state = st.session_state
load_dotenv()

#@st.cache_data(ttl='1d', show_spinner=True)
def get_running_data():
    engine = create_engine(str(os.environ['POSTGRES_URI']).replace('postgres://', 'postgresql://'))
    with open('pages/sql/running.sql', 'r') as query:
        df = pd.read_sql_query(query.read(), engine)
        df['date'] = pd.to_datetime(df['date'], unit="ms")
    return df


if __name__ == "__main__":
    st.markdown("""
        <h1 style="text-align: center"> paperstar studio </h1>
        <p style="text-align: center">a creative place</p>
    """, unsafe_allow_html=True)
    st.divider()

    st.code("""
hello,
my name is abel
i love building software with a focus on data """, language=None, line_numbers=True, wrap_lines=True)

    st.divider()
    st.markdown("""<h3 style="text-align: center">running data</h3><p style="text-align: center">totals since march 27, 2025</p>""", unsafe_allow_html=True)
    st.divider()

    df = get_running_data()

    aggregation = {'date': 'min', 'distance [ km ]': 'sum', 'duration [ hours ]': 'sum', 'elevation_gain [ km ]': 'sum'}
    ddf = pd.DataFrame(df.groupby([df['date'].dt.month], as_index=False).agg(aggregation))
    ddf['avg. pace [ min/km ]'] = ((ddf['duration [ hours ]']) / ddf['distance [ km ]'] * 60).round(2)
    ddf['days_in_month'] = ddf['date'].dt.days_in_month
    ddf['distance [ avg. km / day ]'] = ddf['distance [ km ]'].astype('float') / ddf['days_in_month'].astype('float')
    ddf['duration [ avg. min / day ]'] = 60 * ddf['duration [ hours ]'].astype('float') / ddf['days_in_month'].astype('float')
    num_days = datetime.now() - datetime(2025, 3, 26)
    st.code(f"""
{round(ddf['distance [ km ]'].sum())}  km      total for an average of {round(ddf['distance [ km ]'].sum() / num_days.days, 2)} km / day
{round(ddf['duration [ hours ]'].sum(), 1)} hours   total for an average of {round((ddf['duration [ hours ]'].sum() * 60) / num_days.days)} minutes / day
{num_days.days}  days    since 2025-03-27 """, language=None, line_numbers=True, wrap_lines=True)


    ddf.set_index(keys=['date'], inplace=True)
    ddf_t = ddf.transpose()
    ddf_t.columns = ddf_t.columns.astype('str').str.replace('00:00:00+00:00', '')
    ddf_t.insert(len(ddf_t.columns), '2025-08-01', None)
    
    fig = px.scatter(df, x='date', y='distance [ km ]',  title="individual run distances and elevation gains", trendline="lowess")
    
    fig.add_vline(x=datetime(2025, 4,1), line_width=1, line_dash="dash", line_color="grey")
    fig.add_vline(x=datetime(2025, 5, 1), line_width=1, line_dash="dash", line_color="grey")
    fig.add_vline(x=datetime(2025, 6, 1), line_width=1, line_dash="dash", line_color="grey")
    fig.add_vline(x=datetime(2025, 7, 1), line_width=1, line_dash="dash", line_color="grey")
    fig.add_vline(x=datetime(2025, 8, 1), line_width=1, line_dash="dash", line_color="grey")
    fig.add_vline(x=datetime(2025, 9, 1), line_width=1, line_dash="dash", line_color="grey")
    fig.add_vline(x=datetime(2025, 10, 1), line_width=1, line_dash="dash", line_color="grey")
    fig.add_vline(x=datetime(2025, 11, 1), line_width=1, line_dash="dash", line_color="grey")
    fig.add_vline(x=datetime(2025, 12, 1), line_width=1, line_dash="dash", line_color="grey")
    for month in range(1,6):
        fig.add_vline(x=datetime(2026, month, 1), line_width=1, line_dash="dash", line_color="grey")
    
    fig.add_hline(y=df['distance [ km ]'].mean(), line_width=2, line_dash="dash", line_color="black")

    fig.update_layout(showlegend=False)
    fig.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig)


    st.markdown("""<style>#MainMenu {visibility: hidden;}footer {visibility: hidden;}</style>""", unsafe_allow_html=True)
