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

    #st.video("chemin_vers_video_tutoriel.mp4")

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


# Fonction pour la page d'importation de données
def importation():
    st.title("Importation de Fichiers")
    st.markdown("""
        ### Vos données, notre expertise.
        Téléchargez vos fichiers et voyez la magie opérer. Nous supportons une variété de formats pour une intégration sans effort.
        """)

    file_type = st.radio(
        "Choisissez le type de fichier à importer :",
        ('xlsx', 'csv', 'netCDF')
    )

    uploaded_file = st.file_uploader("Choisissez un fichier", type=[file_type])

    if uploaded_file is not None:
        if file_type == 'xlsx':
            df = pd.read_excel(uploaded_file)
        elif file_type == 'csv':
            df = pd.read_csv(uploaded_file)
        elif file_type == 'netCDF':
            ds = xr.open_dataset(uploaded_file)
            df = ds.to_dataframe()

        st.write("Aperçu des données :")
        st.dataframe(df)
        # Stocker les données dans la session pour y accéder plus tard
        st.session_state['data'] = df
        # Option pour passer à l'analyse exploratoire
        if st.button("Passer à l'analyse exploratoire"):
            analyse_exploratoire(df)  # Fonction à définir
    else:
        st.warning("Veuillez télécharger un fichier.")


# Fonction pour la page d'analyse exploratoire
def analyse_exploratoire(df):
    st.title("Analyse Exploratoire des Données")
    st.markdown("""
        ### Explorez vos données de manière interactive.
        Sélectionnez une variable pour commencer l'analyse.
        """)

    if 'data' not in st.session_state:
        st.error("Aucune donnée disponible. Veuillez d'abord importer des données.")
        return

    st.write("Aexploration visuelle des données ")
    # Generate the HTML using Pygwalker
    pyg_html = pyg.to_html(df)

    # Embed the HTML into the Streamlit app
    components.html(pyg_html, height=1000, scrolling=True)

    # Si des données sont disponibles, permettre à l'utilisateur de sélectionner une variable
    variable = st.selectbox("Choisissez une variable à analyser :", df.columns)
    st.write(f"Analyse de la variable {variable} :")

    # Ici, vous pouvez ajouter des graphiques et des statistiques sur la variable choisie
    # Exemple :
    st.write(df[variable].describe())




# Menu de navigation
st.sidebar.title("Menu")
st.sidebar.markdown("Utilisez ce menu pour naviguer entre les différentes pages de l'application.")
navigation_pages = ["Accueil", "Importation de données", "Analyse Exploratoire", "Prédictions", "Actualités", "Support"]
page = st.sidebar.radio("Aller à", navigation_pages)

# Gestion de la navigation
if page == "Accueil":
    home()
elif page == "Importation de données":
    importation()
elif page == "Analyse Exploratoire":
    if 'data' in st.session_state:
        analyse_exploratoire(st.session_state['data'])
    else:
        st.error("Veuillez importer des données avant de passer à l'analyse.")
# Ajouter d'autres pages ici

# Pied de page
st.markdown("---")
st.markdown("""
    © Flood Prediction Platform - Tous droits réservés.
    [Mentions légales](#) | [Politique de confidentialité](#) | [Contact](#)
    Suivez-nous sur [Facebook](#), [Twitter](#), [LinkedIn](#).
    """)
