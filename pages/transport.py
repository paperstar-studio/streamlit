import os
import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

def main_app(): # bought moped on 2026-4-23 THURSDAY
	st.title("money spent on moped")
	df = pd.DataFrame([
		{'start':datetime(2026,4,23), 'cost':1999.00, 'end':datetime.now(), 'name':'moped'},
		{'start':datetime(2026,4,23), 'cost':99.00, 'end':datetime.now(), 'name':'moped EU import'},
		{'start':datetime(2026,4,24), 'cost':255.00, 'end':datetime.now(), 'name':'zulassung'},
	])
	df['duration'] = (df['end'] - df['start']).dt.days
	df['cost per day'] = df['cost'] / df['duration']
	col1, col2, col3, col4 = st.columns(4)
	with col1:		st.metric("total cost", round(df['cost'].sum()))
	with col2:		st.metric("days used", (datetime.now()-datetime(2026,4,23)).days)
	with col3:		st.metric("cost / day", round(df['cost per day'].sum()))
	st.write("cost table:")
	st.dataframe(df, height=(35*(len(df.index)+1)+3))
	st.divider()

	return df['cost'].sum()


def km_input(engine):
	st.title("distance driven with moped")
	already_driven = pd.read_sql("SELECT * FROM moped_km order by timestamp", con=engine)
	col1, col2, col3 = st.columns(3)
	with col1:		timestamp = st.datetime_input("timestamp")
	with col2:		km = st.number_input("km on app")
	with col3:		km_moped = st.number_input("km on moped", value=None)

	if st.button("upload to db"):
		df = pd.DataFrame([{'timestamp':timestamp, 'km_account':km, 'km_moped':km_moped}])
		df.to_sql("moped_km", index=True, if_exists='append', con=engine)
		st.badge("success", color="green")


	st.plotly_chart(px.line(already_driven, x='timestamp', y=['km_account', 'km_moped'], markers=True))

	st.divider()

	return already_driven['km_account'].max()


if __name__ == "__main__":
	engine = create_engine(os.environ["POSTGRES_URI"])
	total_cost = main_app()
	total_km = km_input(engine)