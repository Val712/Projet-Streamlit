import streamlit as st
st.subheader("Galerie Mascottes (3 images par ligne)")
# Liste des images d'exemple
image_urls = [
"https://static.streamlit.io/examples/cat.jpg",
"https://static.streamlit.io/examples/dog.jpg",
"https://static.streamlit.io/examples/owl.jpg"
]
# Affichage côte à côte sur 3 colonnes
cols = st.columns(3)
for index, url in enumerate(image_urls):
    with cols[index % 3]:
        st.image(url, width="stretch", caption=f"Photo {index +1}")