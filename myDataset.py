import pandas as pd
import streamlit as st

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data


names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)

st.title('Streamlit con Pandas')
st.dataframe(names_data)