import streamlit as st
import pandas as pd
import xarray as xr
import pygwalker as pyg
import streamlit.components.v1 as components

from pages.02_Importation import df

def EDA(df):
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

if not df:
    print("Importez les données")
else:
    EDA(df)