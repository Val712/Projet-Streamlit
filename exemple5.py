import streamlit as st
st.title("Organisation en Colonnes")
# Création de 3 colonnes de largeur égale
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Métrique A")
    st.metric(label="Utilisateurs", value="1,200", delta="+5%")
with col2:
    st.header("Métrique B")
    st.metric(label="Revenu", value="45 000 €", delta="+12%")
with col3:
    st.header("Métrique C")
    st.metric(label="Conversion", value="3.2%", delta="-0.4%")