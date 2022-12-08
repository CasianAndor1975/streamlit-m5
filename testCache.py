import pandas as pd
import streamlit as st

st.title('Hola con Caché')
DATA_URL = ('dataset.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

dataLoadState = st.text('Loading..')
data = load_data(1000)

dataLoadState.text('Ya usamos caché..!')
st.dataframe(data)