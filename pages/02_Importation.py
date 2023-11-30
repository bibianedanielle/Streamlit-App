import streamlit as st
import pandas as pd
import xarray as xr
import pygwalker as pyg
import streamlit.components.v1 as components


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
