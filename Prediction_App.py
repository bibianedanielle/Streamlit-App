import streamlit as st
import pandas as pd
import xarray as xr
import pygwalker as pyg
import streamlit.components.v1 as components

# Configuration initiale de la page
st.set_page_config(
    page_title="Flood Prediction Platform",
    page_icon=":droplet:",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Fonction pour la page d'accueil
def home():
    st.image("images/flood.jpg", use_column_width=True)
    st.title("Bienvenue sur la Plateforme de Prédiction des Inondations")
    st.markdown("""
        ### Anticipez les inondations avec une précision inégalée.
        Utilisez des données avancées et des modèles prédictifs pour rester un pas devant les crues.
        """)
    st.markdown("## Fonctionnalités de la plateforme")
    st.markdown("""
            - **Importation de données** : Téléchargez vos fichiers de données dans divers formats et préparez-les pour l'analyse.
            - **Analyse Exploratoire** : Examinez vos données de manière interactive, visualisez des tendances et identifiez des patterns.
            - **Prédictions** : Utilisez des modèles prédictifs pour estimer les risques et prendre des décisions éclairées.
            - **Actualités** : Restez informé avec les dernières informations et les mises à jour sur les conditions hydrologiques.
            - **Support** : Obtenez de l'aide et des conseils pour utiliser la plateforme au maximum de son potentiel.
            """)
    st.markdown("## Comment ça marche?")
    st.markdown("""
        Découvrez en quelques clics comment notre technologie utilise des analyses de pointe pour vous aider à anticiper et à gérer les risques d'inondation.
        """)

    # st.video("chemin_vers_video_tutoriel.mp4")

    st.markdown("## Prêt à changer la donne dans la prévention des crues ?")

    # Style personnalisé pour les titres et le texte
    st.markdown("""
            <style>
            .big-font {
                font-size:30px !important;
                font-weight: bold;
            }
            </style>
            """, unsafe_allow_html=True)


def information():
    st.title("Objectifs de la plateforme")


def support():
    st.title("Tutoriel")


# Menu de navigation
st.sidebar.title("Menu")
st.sidebar.markdown("Utilisez ce menu pour naviguer entre les différentes pages de l'application.")
navigation_pages = ["Accueil", "A propos de nous", "Support"]
page = st.sidebar.radio("Aller à", navigation_pages)

# Gestion de la navigation
if page == "Accueil":
    home()
elif page == "A propos de nous":
    information()
elif page == "Support":
    support()

# Pied de page
st.markdown("---")
st.markdown("""
    © Flood Prediction Platform - Tous droits réservés.
    [Mentions légales](#) | [Politique de confidentialité](#) | [Contact](#)
    Suivez-nous sur [Facebook](#), [Twitter](#), [LinkedIn](#).
    """)
