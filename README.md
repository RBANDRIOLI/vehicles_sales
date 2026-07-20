# Vehicles_sales
Este Projeto baseia-se na análise de anúncios de vendas de carros.

## Descrição do projeto

Este projeto realiza uma análise exploratória de dados (EDA) sobre um conjunto de dados 
de anúncios de venda de veículos. O objetivo é identificar padrões, distribuições e 
relações entre variáveis como preço, quilometragem (odômetro), ano do veículo, entre outras.

O projeto inclui:
- Um notebook Jupyter (`notebooks/EDA.ipynb`) com a exploração inicial dos dados.
- Um aplicativo web interativo desenvolvido com Streamlit (`app.py`), que permite 
  visualizar os dados de forma dinâmica através do navegador.

  ## Funcionalidades do aplicativo web

O aplicativo web, criado com `streamlit`, oferece as seguintes funcionalidades:

- **Histograma interativo**: exibe a distribuição da quilometragem (`odometer`) dos 
  veículos anunciados.
- **Gráfico de dispersão interativo**: exibe a relação entre a quilometragem (`odometer`) 
  e o preço (`price`) dos veículos.
- Os gráficos são gerados sob demanda, através de caixas de seleção (ou botões) 
  disponíveis na interface.

  ## Tecnologias utilizadas

- Python
- Pandas
- Plotly Express
- Streamlit

## URL do Aplicativo online

O aplicativo está disponível online através do Render: https://vehicles-sales.onrender.com