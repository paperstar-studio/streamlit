import pandas as pd
import streamlit as st
from datetime import datetime



# bought moped on 2026-4-23 THURSDAY

def main_app():
	#st.badge(label="test", color='blue')

	df = pd.DataFrame([
		{'start':datetime(2026,4,23), 'cost':1999.00, 'end':datetime.now(), 'name':'moped'},
		{'start':datetime(2026,4,23), 'cost':99.00, 'end':datetime.now(), 'name':'moped EU import'},
		{'start':datetime(2026,4,24), 'cost':255.00, 'end':datetime.now(), 'name':'zulassung'},
	])
	df['duration'] = (df['end'] - df['start']).dt.days
	df['cost per day'] = df['cost'] / df['duration']




	col1, col2, col3, col4 = st.columns(4)
	with col1:
		st.metric("days since transport switch", df['cost'].sum())
	with col2:
		st.metric("spent since transport switch", (datetime.now()-datetime(2026,4,23)).days)
	with col3:
		st.metric("cost per day", df['cost per day'].sum())


	st.divider()

	st.dataframe(df, height=(35*(len(df.index)+1)+3))




if __name__ == "__main__":
	main_app()