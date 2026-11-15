import streamlit as st
import pandas as pd
import plotly.express as px
df_iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
st.subheader("Nuage de points interactif (Plotly)")
# Création de la figure Plotly par Salma AZIZ
fig_plotly = px.scatter(
df_iris,
x="sepal_width",
y="sepal_length",
color="species",
size="petal_length",
hover_data=["petal_width"],
title="Relation Sépale vs Pétale"
)
# Rendu dans Streamlit
st.plotly_chart(fig_plotly, use_container_width=True)