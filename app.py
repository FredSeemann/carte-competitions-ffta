import streamlit as st
import folium
from streamlit_folium import st_folium

# Titre de l'application
st.title("Carte des compétitions de tir à l'arc 🎯")

# Création de la carte centrée sur la France
carte = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Liste des compétitions (latitude, longitude, nom, discipline)
competitions = [
    (48.8566, 2.3522, "Compétition à Paris", "Tir en salle"),
    (45.7640, 4.8357, "Compétition à Lyon", "Tir 3D"),
    (43.6045, 1.4442, "Compétition à Toulouse", "Tir Nature"),
]

# Dictionnaire pour associer une discipline à une icône et une couleur
styles_disciplines = {
    "Tir 3D": ("tree", "green"),
    "Tir Nature": ("paw", "brown"),
    "Tir en salle": ("bullseye", "blue"),
}

# Ajout des marqueurs sur la carte
for lat, lon, nom, discipline in competitions:
    icon_name, color = styles_disciplines.get(discipline, ("info-sign", "gray"))
    icon = folium.Icon(icon=icon_name, prefix="fa", color=color)
    folium.Marker([lat, lon], popup=nom, tooltip=discipline, icon=icon).add_to(carte)

# Affichage de la carte dans Streamlit
st_folium(carte, width=700, height=500)
