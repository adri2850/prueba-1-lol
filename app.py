import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Estadística de goles de Messi")

# Cargar los datos desde la página web
pagina = 'https://players.fcbarcelona.com/es/jugador/548-messi-lionel-andres-messi-cuccitini'
tablas = pd.read_html(pagina)

# Crear la aplicación web con Streamlit
st.write(tablas[0].head(5))

