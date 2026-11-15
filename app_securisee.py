import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# --- 1. INITIALISATION DE LA SESSION ---
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
# --- 2. FONCTION DE VÉRIFICATION DES IDENTIFIANTS ---
@st.cache_data
def load_accounts():
    return pd.read_csv("accounts.csv")


def authenticate(username_input, password_input):
    accounts_df = load_accounts()
    user_match = accounts_df[
        (accounts_df["name"] == username_input)
        & (accounts_df["password"] == password_input)
    ]
    return not user_match.empty
# --- 3. PAGE DE CONNEXION OBLIGATOIRE ---
if not st.session_state["logged_in"]:
    st.title("Connexion")
    st.subheader("Veuillez vous identifier pour accéder à l'application")

    username_input = st.text_input("Nom d'utilisateur")
    password_input = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        if authenticate(username_input, password_input):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username_input
            st.rerun()
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")

else:
    # --- BARRE LATÉRALE : bienvenue, déconnexion et menu ---
    with st.sidebar:
        st.write(f"Bienvenue, **{st.session_state['username']}** !")
        if st.button("Se déconnecter"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.rerun()
        st.divider()

        selected_page = option_menu(
            menu_title="Menu principal",
            options=["Accueil", "Galerie Photos"],
            icons=["house", "images"],
            default_index=0,
        )

    # --- CONTENU DES PAGES ---
    if selected_page == "Accueil":
        st.title("Page d'Accueil")
        st.write("Bienvenue dans l'application sécurisée.")

    elif selected_page == "Galerie Photos":
        st.title("Galerie Photos")
        st.write("Galerie de photos d'animaux, sur 3 colonnes :")

        # Remplacez ces adresses par les images de l'animal de votre choix
        image_urls = [
            ("Images/loutre.png", "Loutre"),
            ("Images/Dauphin.png", "Dauphin"),
            ("Images/python.png", "Python"),
        ]

        cols = st.columns(3)
        for index, (path, name) in enumerate(image_urls):
            with cols[index % 3]:
                st.image(path, caption=name, width="stretch")