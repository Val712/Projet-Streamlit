import streamlit as st
from streamlit_option_menu import option_menu
# Placement du menu de navigation dans la barre latérale
with st.sidebar:
    selected_page = option_menu(
    menu_title="Navigation principale", # Titre du menu (ou None)
    options=["Accueil", "Dashboard Data", "Galerie Photos"], #Liste des pages
    icons=["house", "bar-chart-fill", "images"], # IcônesBootstrap (optionnel)
    default_index=0 # Page sélectionnée par défaut
    )
#4 par Salma AZIZ
# Affichage dynamique du contenu selon le choix de navigation
if selected_page == "Accueil":
    st.title(" Bienvenue sur l'Application Data")
    st.write("Sélectionnez un onglet dans le menu latéral pour démarrer l'exploration.")
elif selected_page == "Dashboard Data":
    st.title(" Dashboard d'Analyse")
    st.write("Contenu réservé à l'analyse des données...")
elif selected_page == "Galerie Photos":
    st.title(" Album Photos")
    st.write("Galerie d'images et contenus multimédias...")