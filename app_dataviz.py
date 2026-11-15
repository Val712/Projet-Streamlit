import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement direct du dataset "flights" depuis GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
    return pd.read_csv(url)

df_flights = load_data()

st.title("Analyse du trafic aérien")

# Ordre des mois tel qu'il apparaît dans le fichier (Jan, Feb, ...)
months_order = list(df_flights["month"].unique())

# 3a. Slider : plage d'années
year_min = int(df_flights["year"].min())
year_max = int(df_flights["year"].max())
year_range = st.slider(
    "Plage d'années",
    min_value=year_min,
    max_value=year_max,
    value=(1949, 1960),
)

# 3b. Selectbox : un mois précis ou tous les mois
month_choice = st.selectbox("Mois", ["Tous les mois"] + months_order)

# Application des filtres
df_filtered = df_flights[
    (df_flights["year"] >= year_range[0]) & (df_flights["year"] <= year_range[1])
]
if month_choice != "Tous les mois":
    df_filtered = df_filtered[df_filtered["month"] == month_choice]

# Vérification temporaire
st.write(f"Années : {year_range[0]} à {year_range[1]} | Mois : {month_choice}")
st.dataframe(df_filtered)






# 4a. Indicateur : total des passagers sur la période sélectionnée
total_passengers = int(df_filtered["passengers"].sum())

st.metric(
    label="Total des passagers sur la période sélectionnée",
    value=f"{total_passengers:,}".replace(",", " "),
)
# 4b. Graphique en lignes : évolution du nombre de passagers
st.subheader("Évolution du nombre de passagers")

if month_choice == "Tous les mois":
    # Une valeur par mois, dans l'ordre chronologique
    df_plot = df_filtered.copy()
    month_num = {m: i + 1 for i, m in enumerate(months_order)}
    df_plot["date"] = pd.to_datetime(
        df_plot["year"].astype(str) + "-" + df_plot["month"].map(month_num).astype(str) + "-01"
    )
    st.line_chart(df_plot.set_index("date")["passengers"])
else:
    # Un mois précis : une valeur par année
    st.line_chart(df_filtered.set_index("year")["passengers"])

    # 4c. Heatmap Seaborn (case à cocher)
st.divider()

if st.checkbox("Afficher la heatmap des passagers par année et par mois"):
    st.subheader("Répartition des passagers par année et par mois")

    pivot = df_filtered.pivot(index="month", columns="year", values="passengers")
    # Remettre les mois dans l'ordre chronologique (sinon tri alphabétique)
    pivot = pivot.reindex([m for m in months_order if m in pivot.index])

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(pivot, annot=True, fmt="d", cmap="YlOrRd", ax=ax)
    ax.set_xlabel("Année")
    ax.set_ylabel("Mois")
    st.pyplot(fig)