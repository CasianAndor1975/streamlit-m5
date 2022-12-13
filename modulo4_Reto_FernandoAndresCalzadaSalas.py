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

def filter_by_unit(unit):
    filtered_data_unit = data[data['Unit'] == unit]
    return filtered_data_unit

def filter_by_emp_id(emp):
    filtered_data_emp = data[data['Employee_ID'].str.upper().str.contains(emp)]
    return filtered_data_emp

def filter_by_educ_level(level):
    filtered_data_level = data[data['Education_Level'] == level]
    return filtered_data_level


data_load_state = st.text('Loading cicle nyc data...')
data = load_data(1000)
#data_load_state.text("Done! (using st.cache)")

st.title('Reto del Módulo 4')

sidebar = st.sidebar
sidebar.title("Funcionalidades")

st.header("Fernando Andrés Calzada Salas")

if sidebar.checkbox('Mostrar dataframe'):
#    chart_data = st.dataframe(data)
    st.write("Informacion de la app")
    st.dataframe(data)

# ########################## PASO 9  #######################################
# --- EMPLOYEE ID
empId = st.sidebar.text_input('ID del empleado :')
btnEmpId = st.sidebar.button('Buscar empleado')

if btnEmpId:
    data_emp_id = filter_by_emp_id(empId.upper())
    count_row = data_emp_id.shape[0]  # Gives number of rows
    st.write(f"Total empleados mostrados : {count_row}")
    st.write(data_emp_id)

# --- HOMETOWN
selected_hometown = sidebar.radio("Select Class", data['Hometown'].unique())
btnFilterbyHometown1 = st.sidebar.button('Filtrar Hometown 1')

if btnFilterbyHometown1:
    filterbyhome = filter_by_hometown(selected_hometown)
    count_row = filterbyhome.shape[0]  # Gives number of rows
    st.write(f"Total empleados : {count_row}")
    st.dataframe(filterbyhome)

# --- UNIT


# ########################## PASO 10  #######################################

selected_level = st.sidebar.selectbox("Seleccionar Nivel Educativo", data['Education_Level'].unique())
btnFilterbyLevel = st.sidebar.button('Filtrar Nivel')

if btnFilterbyLevel:
    st.write(f"NIVEL ELEGIDO : {selected_level}")
    filterbylevel = filter_by_educ_level(selected_level)
    count_row = filterbylevel.shape[0]  # Gives number of rows
    st.write(f"Total empleados : {count_row}")
    st.dataframe(filterbylevel)

# ########################## PASO 11  #######################################
selected_hometown2 = st.sidebar.selectbox("Seleccionar Residencia (Hometown)", data['Hometown'].unique())
btnFilterbyHometown2 = st.sidebar.button('Filtrar Hometown 2')

if btnFilterbyHometown2:
    filterbyhome = filter_by_hometown(selected_hometown2)
    count_row = filterbyhome.shape[0]  # Gives number of rows
    st.write(f"Total empleados : {count_row}")
    st.dataframe(filterbyhome)

# ########################## PASO 12  #######################################

selected_unit2 = st.sidebar.selectbox("Seleccionar Unidad (Unit)", data['Unit'].unique())
btnFilterbyUnit2 = st.sidebar.button('Filtrar Unidad 2')

if btnFilterbyUnit2:
    filterbyunit = filter_by_unit(selected_unit2)
    count_row = filterbyunit.shape[0]  # Gives number of rows
    st.write(f"Total empleados : {count_row}")
    st.dataframe(filterbyunit)