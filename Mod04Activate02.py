import pandas as pd
import streamlit as st

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data


# names_link = 'dataset.csv'
names_data = pd.read_csv('superstore.csv')

st.title('Módulo 4, Actívate 02')
sidebar = st.sidebar 
sidebar.title("Datos Adicionales.") 
sidebar.write("Parámetros de entrada.") 

st.dataframe(names_data)