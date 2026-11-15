import streamlit as st
# Ajout d'éléments dans la barre latérale 3 par Salma AZIZ
st.sidebar.title("Configuration")
user_role = st.sidebar.selectbox("Rôle :", ["Analyste", "Manager",
"Admin"])
# Utilisation du bloc 'with' pour grouper des composants dans lasidebar
with st.sidebar:
    st.divider()
    st.write("Connecté en tant que : **Alexandre**")
    if st.button("Déconnexion"):
        st.success("Déconnecté !")