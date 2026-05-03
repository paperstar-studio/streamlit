# ADD per day km and per day min / month breakdown june.29.2025

import os
import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from sqlalchemy import create_engine

st.set_page_config(layout='wide')

load_dotenv()

def get_running_data():
    engine = create_engine(str(os.environ['POSTGRES_URI']).replace('postgres://', 'postgresql://'))
    with open('pages/sql/running.sql', 'r') as query:
        df = pd.read_sql_query(query.read(), engine)
        df['date'] = pd.to_datetime(df['date'], unit="ms")
    return df


if __name__ == "__main__":
    st.markdown("""<h3 style="text-align: center">running data</h3><p style="text-align: center">totals since march 27, 2025</p>""", unsafe_allow_html=True)

    df = get_running_data()

    aggregation = {'date': 'min', 'distance [ km ]': 'sum', 'duration [ hours ]': 'sum', 'elevation_gain [ km ]': 'sum'}
    ddf = pd.DataFrame(df.groupby([df['date'].dt.month], as_index=False).agg(aggregation))
    ddf['avg. pace [ min/km ]'] = ((ddf['duration [ hours ]']) / ddf['distance [ km ]'] * 60).round(2)
    ddf['days_in_month'] = ddf['date'].dt.days_in_month
    ddf['distance [ avg. km / day ]'] = ddf['distance [ km ]'].astype('float') / ddf['days_in_month'].astype('float')
    ddf['duration [ avg. min / day ]'] = 60 * ddf['duration [ hours ]'].astype('float') / ddf['days_in_month'].astype('float')
    num_days = datetime.now() - datetime(2025, 3, 26)
    

    col1, col2, col3 = st.columns(3)

    with col1:
        col11, col22, col33 = st.columns(3)
        with col11:     st.metric("",value=num_days.days, delta_description="days")
        with col22:     st.metric("",value=round(ddf['distance [ km ]'].sum()), delta_description="km")
        with col33:     st.metric("",value=round(ddf['duration [ hours ]'].sum()), delta_description="hours")
        col111, col222, col333 = st.columns(3)
        with col111:    pass
        with col222:    st.metric("",value=round(ddf['distance [ km ]'].sum()/num_days.days,2), delta_description="km / day")
        with col333:    st.metric("",value=round(ddf['duration [ hours ]'].sum()/num_days.days,2), delta_description="hours / day")

    ddf.set_index(keys=['date'], inplace=True)
    ddf_t = ddf.transpose()
    ddf_t.columns = ddf_t.columns.astype('str').str.replace('00:00:00+00:00', '')
    ddf_t.insert(len(ddf_t.columns), '2025-08-01', None)
    
    fig = px.scatter(df, x='date', y='distance [ km ]',  title="individual run distances", trendline="lowess")
    for month in range(4,13):
        fig.add_vline(x=datetime(2025, month, 1), line_width=1, line_dash="dash", line_color="grey")
    for month in range(1,7):
        fig.add_vline(x=datetime(2026, month, 1), line_width=1, line_dash="dash", line_color="grey")
    fig.add_hline(y=df['distance [ km ]'].mean(), line_width=2, line_dash="dash", line_color="black")

    fig.update_layout(showlegend=False)
    fig.update_layout(coloraxis_showscale=False)
    with col2:
        st.plotly_chart(fig)

    df['cummulative distance [ km ]'] = df['distance [ km ]'].cumsum()
    fig_cumm = px.line(df, x='date', y='cummulative distance [ km ]', title='cummulative run dstiance')
    with col3:
        st.plotly_chart(fig_cumm)


    st.markdown("""<style>#MainMenu {visibility: hidden;}footer {visibility: hidden;}</style>""", unsafe_allow_html=True)
