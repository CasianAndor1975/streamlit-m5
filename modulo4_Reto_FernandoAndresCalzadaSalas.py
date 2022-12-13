import codecs
import streamlit as st
import pandas as pd
#import numpy as np

st.title('Netflix app')

DATE_COLUMN = 'released'
DATA_URL = ('Employees.csv')



@st.cache
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data1 = pd.read_csv(doc, nrows=nrows)
    #lowercase = lambda x: str(x).lower()
    return data1

def filter_by_hometown(hometown):
    filtered_data_hometown = data[data['Hometown'] == hometown]
    return filtered_data_hometown


data_load_state = st.text('Loading cicle nyc data...')
data = load_data(1000)
#data_load_state.text("Done! (using st.cache)")

st.title('Reto del Módulo 4')

sidebar = st.sidebar
sidebar.title("Funcionalidades")

st.header("Fernando Andrés Calzada Salas")

#if sidebar.checkbox('Mostrar dataframe'):
#    chart_data = st.dataframe(data)
#    st.write("Informacion de la app")
#    st.dataframe(chart_data)

    

selected_hometown = st.sidebar.selectbox("Seleccionar Residencia (Hometown)", data['Hometown'].unique())
btnFilterbyHometown = st.sidebar.button('Filtrar Hometown ')

if (btnFilterbyHometown):
    filterbyhome = filter_by_hometown(selected_hometown)
    count_row = filterbyhome.shape[0]  # Gives number of rows
    st.write(f"Total filmes : {count_row}")

st.dataframe(filterbyhome)