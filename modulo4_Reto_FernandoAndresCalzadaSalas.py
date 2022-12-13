import codecs
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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

# ########################## PASO 13  #######################################
st.markdown("___")
fig, ax = plt.subplots()
ax.hist(data.Age)
st.header("Edad de los empleados")
st.pyplot(fig)

# ########################## PASO 14  #######################################
st.markdown("___")
fig, ax2 = plt.subplots()
plt.xticks(rotation=90)
ax2.hist(data.Unit)
st.header("Frecuencia por Unidad")
st.pyplot(fig)


# ########################## PASO 15  #######################################
st.markdown("___")
fig3, ax3 = plt.subplots()
ax3.scatter(data.Hometown, data.Attrition_rate)
ax3.set_xlabel("Ciudad")
ax3.set_ylabel("Deserción")
st.header("Índice de deserción por ciudad")
st.pyplot(fig3)


# ########################## PASO 16  #######################################
st.markdown("___")
fig4, ax4 = plt.subplots()
ax4.scatter(data.Age, data.Attrition_rate)
ax4.set_xlabel("Edad")
ax4.set_ylabel("Deserción")
st.header("Edad Vs. Índice de deserción")
st.pyplot(fig4)

# ########################## PASO 17  #######################################
st.markdown("___")
fig5, ax5 = plt.subplots()
ax5.scatter(data.Time_of_service, data.Attrition_rate)
ax5.set_xlabel("Tiempo")
ax5.set_ylabel("Deserción")
st.header("Tiempo de servicio Vs. Índice de deserción")
st.pyplot(fig5)