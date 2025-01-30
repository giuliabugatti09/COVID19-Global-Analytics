import streamlit as st
import pandas as pd
from scripts.coleta_dados import collect_data
from scripts.limpeza_dados import process_data
from scripts.visualizacao_dados import plot_bar_chart, plot_scatter_plot

# Configuração inicial do Streamlit
st.set_page_config(page_title="Análise da COVID-19", layout="wide")

st.title("📊 Análise de Dados da COVID-19 com IA")

# 🔹 Coleta os dados
st.write("🔄 Coletando dados...")
df = collect_data()

# 🔹 Processa os dados
st.write("⚙️ Processando dados...")
df = process_data(df)

# 🔹 Exibe os primeiros dados
st.write("🔍 Visualizando os primeiros dados:")
st.dataframe(df.head())

# 🔹 Gráfico de barras
st.write("📊 **Top 20 países com mais casos**")
plot_bar_chart(df)

# 🔹 Gráfico de dispersão
st.write("📌 **Relação entre casos e mortes por país**")
plot_scatter_plot(df)
