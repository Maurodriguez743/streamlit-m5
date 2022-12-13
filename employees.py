import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.title('¿Y la deserción laboral?')
st.header('Encuesta sobre la deserción.')
st.write('En 2020 Hackathon HackerEarth realizó una encuesta para obtener información que fuera explicativa del fenómeno de deserción laboral que tanto afecta en la actualidad a las empresas y organizaciones.')
st.write('Aqui puedes ver los resultados de la encuesta.')

@st.cache
def load_data(nrows):
    data = pd.read_csv('Employees.csv', nrows=nrows)
    return data

def filter_data_by_Employee_ID(Employee_ID):
    filtered_Employee_ID = data[data['Employee_ID'].str.upper().str.contains(Employee_ID)]
    return filtered_Employee_ID

def filter_data_by_Hometown(Hometown):
    filtered_Hometown = data[data['Hometown'].str.upper().str.contains(Hometown)]
    return filtered_Hometown

def filter_data_by_Unit(Unit):
    filtered_Unit = data[data['Unit'].str.upper().str.contains(Unit)]
    return filtered_Unit

def filter_data_by_Education_Level(Education_Level):
    filtered_data_Education_Level = data[data['Education_Level'] == Education_Level]
    return filtered_data_Education_Level

def filter_data_by_Hometown_2(Hometown):
    filtered_data_Hometown_2 = data[data['Hometown'] == Hometown]
    return filtered_data_Hometown_2

def filter_data_by_Unit_2(Unit):
    filtered_data_Unit_2 = data[data['Unit'] == Unit]
    return filtered_data_Unit_2


data_load_state = st.text('Cargando información...')
data = load_data(1000)
data_load_state.text("Listo! (usando st.cache)")

if st.sidebar.checkbox('Mostrar la Base de Datos'):
    st.subheader('Base de Datos')
    st.write(data)

IDempleado = st.sidebar.text_input('ID Empleado:')
btnBuscar = st.sidebar.button('Buscar ID')

if (btnBuscar):
   data_ID = filter_data_by_Employee_ID(IDempleado.upper())
   count_row = data_ID.shape[0] 
   st.write(f"Total ID mostrados: {count_row}")
   st.write(data_ID)

NameHometown = st.sidebar.text_input('Ciudad:')
btnBuscar1 = st.sidebar.button('Buscar Ciudad')

if (btnBuscar1):
   data_Hometown = filter_data_by_Hometown(NameHometown.upper())
   count_row = data_Hometown.shape[0] 
   st.write(f"Total: {count_row}")
   st.write(data_Hometown)

NameUnit = st.sidebar.text_input('Unidad Funacional:')
btnBuscar2 = st.sidebar.button('Buscar Unidad')

if (btnBuscar2):
   data_Unit = filter_data_by_Unit(NameUnit.upper())
   count_row = data_Unit.shape[0]
   st.write(f"Total: {count_row}")
   st.write(data_Unit)

selected_Education_level = st.sidebar.selectbox("Seleccionar Nivel Educativo", data['Education_Level'].unique())
btnFilterbyEdu = st.sidebar.button('Filtrar Nivel Educativo')

if (btnFilterbyEdu):
   filterbyedu = filter_data_by_Education_Level(selected_Education_level)
   count_row = filterbyedu.shape[0]
   st.write(f"Total: {count_row}")

   st.dataframe(filterbyedu)

selected_Hometown_2 = st.sidebar.selectbox("Seleccionar Ciudad", data['Hometown'].unique())
btnFilterbyHome = st.sidebar.button('Filtrar Ciudad')

if (btnFilterbyHome):
   filterbyhome2 = filter_data_by_Hometown_2(selected_Hometown_2)
   count_row = filterbyhome2.shape[0]
   st.write(f"Total: {count_row}")

   st.dataframe(filterbyhome2)

selected_Unit_2 = st.sidebar.selectbox("Seleccionar Unidad Funcional", data['Unit'].unique())
btnFilterbyUnit = st.sidebar.button('Filtrar Unidad')

if (btnFilterbyUnit):
   filterbyunit2 = filter_data_by_Unit_2(selected_Unit_2)
   count_row = filterbyunit2.shape[0]
   st.write(f"Total: {count_row}")

   st.dataframe(filterbyunit2)

# GRÁFICAS
# Histograma por Edad

fig = px.histogram(data, x='Age', title='Empleados por Edad', nbins=8)
st.plotly_chart(fig)

#GRAFICA DE FRECUENCIAS UNIDADES
fig2 = px.histogram(data, x='Unit', title='Empleados por Unidad Funcional', color='Unit')
st.plotly_chart(fig2)

#Gráfica para visualizar la relación entre el indice de deserción y la ciudad
attrition=data['Attrition_rate']
hometown=data['Hometown']
unit=data['Unit']

fig3=px.scatter(data,
                         x=hometown,
                         y=attrition,
                         color=unit,
                         title="Relación entre el índice de deserción y la Ciudad de los empleados",
                         labels=dict(attrition="Índice de deserción", hometown="Ciudad"),
                         template="plotly_white")
fig3.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig3)

#Gráfica para visualizar la relación entre el indice de deserción y la edad
Edad=data['Age']
índice_deserción=data['Attrition_rate']
Unidad=data['Unit']

fig4=px.scatter(data,
                   x=Edad,
                   y=índice_deserción,
                   color=Unidad,
                   title="Relación entre el índice de deserción y la Edad de los empleados",
                   labels=dict(Edad="Edad", índice_deserción="índice de deserción"),
                   template="plotly_white")
fig4.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig4)

#Gráfica para visualizar la relación entre el indice de deserción y el tiempo de servicio
attrition=data['Attrition_rate']
time=data['Time_of_service']
unit=data['Unit']

fig5=px.scatter(data,
                         x=time,
                         y=attrition,
                         color=unit,
                         title="Relación entre el índice de deserción y el Tiempo de servicio de los empleados",
                         labels=dict(attrition="índice de deserción", time="Tiempo de servicio"),
                         template="plotly_white")
fig5.update_layout(plot_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig5)

#FIN