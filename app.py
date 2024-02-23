import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Estadística de goles de Messi")

# Cargar los datos desde la página web
pagina = 'https://players.fcbarcelona.com/es/jugador/548-messi-lionel-andres-messi-cuccitini'
tablas = pd.read_html(pagina)

# Crear la aplicación web con Streamlit
st.write(tablas[0].head(5))

# Mostrar estadística gráfica
st.write("Estadística gráfica")

# Obtener los datos para el gráfico
y = tablas[0]['674Goles']
x = tablas[0]['18TEMPORADAS']

# Crear el histograma
fig, ax = plt.subplots()
ax.hist(y, bins=50)

# Mostrar el gráfico en la aplicación web
st.pyplot(fig)
