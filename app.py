import streamlit as st
import pandas as pd
# Titre principal de la page
st.title("Mon Premier Dashboard Streamlit ")
# Texte de présentation
st.write("Bienvenue sur cette application interactive dédiée à l'analyse de données.")
taxis = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv")
st.header("Dashboard Analyse Taxis - Valérie")
# Menu déroulant (Selectbox)
quartier_depart = st.selectbox("Choisissez votre quartier de prise en charge :",
taxis["pickup_borough"].dropna().unique())
#print(list(taxis.columns))
#print(taxis["pickup_borough"])

#filtrer le datafram selon le quartier choisi
filtre = taxis[taxis["pickup_borough"]== quartier_depart]
st.write(f"{len(filtre)} courses au départ de {quartier_depart}")


#5 premières lignes du tableau filtré
st.dataframe(filtre.head(5))

# Métrique : nombre total de courses dans ce quartier
st.metric("Nombre total de courses", len(filtre))

#st.dataframe(taxis)
st.table(taxis)