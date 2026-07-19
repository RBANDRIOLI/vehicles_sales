import pandas as pd
import plotly.express as px
import streamlit as st

# Leitura dos dados
car_data = pd.read_csv('/Users/rodolfo/Projetos/vehicles_sales/vehicles.csv')

# Cabeçalho principal
st.header('Análise Anuncio vendas - Vehicles')

# Checkbox para histograma
build_histogram = st.checkbox('Criar histograma')

if build_histogram:# se o botão for clicado
     st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
     fig = px.histogram(car_data, x="odometer")
     st.plotly_chart(fig, use_container_width=True)

# Checkbox para gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:# se o botão for clicado
     st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
     fig = px.scatter(car_data, x="odometer", y="price")
     st.plotly_chart(fig, use_container_width=True)
