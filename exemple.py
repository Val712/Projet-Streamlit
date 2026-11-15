import streamlit as st
import pandas as pd
df_flights = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv")
# Préparation des données : évolution annuelle du total des passagers
annual_passengers = df_flights.groupby("year")["passengers"].sum()
st.subheader("Évolution du trafic aérien (Bar Chart natif)")
st.bar_chart(annual_passengers)