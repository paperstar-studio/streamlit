import os
import gpxpy
import pandas as pd
import geopy.distance
from numpy_ext import rolling_apply
from sqlalchemy import create_engine, text
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def rolling_metric_pace(duration, distance):
	return (duration.sum() / 60) / (distance.sum() / 1000)


def main_app():
	st.title("run upload")

	uploaded_files = st.file_uploader("run files", accept_multiple_files=True)
	if uploaded_files is not None:
		for file in uploaded_files:
			if "route_" in file.name:
				gpx = gpxpy.parse(file.getvalue())
				points = []
				for segment in gpx.tracks[0].segments:
					for p in segment.points:
						points.append(
							{'timestamp': p.time, 'lat': p.latitude, 'lon': p.longitude, 'elevation': p.elevation, })
				df = pd.DataFrame.from_records(points)
				df['run_id'] = file.name.split('.')[0].split('/')[-1]
				coords = [(p.lat, p.lon) for p in df.itertuples()]
				df['distance'] = [0] + [geopy.distance.distance(from_, to).m for from_, to in zip(coords[:-1], coords[1:])]
				df['distance_cumulative'] = df.distance.cumsum()
				df['duration'] = df.timestamp.diff().dt.total_seconds().fillna(0)
				df['duration_cumulative'] = df.duration.cumsum()
				df['rolling_average_pace'] = rolling_apply(rolling_metric_pace, 100, df.duration.values, df.distance.values)
				df['pace_metric'] = pd.Series((df.duration / 60) / (df.distance / 1000)).bfill()
				try:
					with engine.connect() as con:
						con.execute(
							text(f"""DELETE FROM public.public_running_coordinates WHERE run_id='{file.name.split('.')[0]}' """))
						con.commit()
					df.to_sql(f"public_running_coordinates", index=False, if_exists='append', con=engine)
				except Exception as e:
					st.badge(e, color='red')
				st.badge(f"upload of {file} done", color="green")

	return None


if __name__ == "__main__":
	engine = create_engine(os.environ["POSTGRES_URI"])
	if os.environ['app_password'] == st.text_input("password", type='password'):	
		main_app()
	else:
		st.badge("plassword pls ...", color='red')
	