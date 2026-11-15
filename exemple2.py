import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
st.subheader("Distribution par espèce (Seaborn)")
# 1. Création explicite de la figure
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(data=df_iris, x="species", y="sepal_length", ax=ax, palette="viridis")
ax.set_title("Longueur moyenne des sépales par espèce")
# 2. Rendu dans Streamlit
st.pyplot(fig)