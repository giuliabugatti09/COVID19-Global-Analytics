import streamlit as st
import pandas as pd
import sys
import os

# 🔹 Adicionando o diretório 'scripts' ao path para importar os módulos
sys.path.append(os.path.abspath("scripts"))

# 🔹 Importando as funções dos módulos
from scripts.coleta_dados import collect_data
from scripts.limpeza_dados import process_data
from scripts.visualizacao_dados import visualize_data

# 🔹 Configuração do título do app no Streamlit
st.title("Análise Global da COVID-19 📊")

# 🔹 Botão para carregar e processar os dados
if st.button("Carregar Dados"):
    with st.spinner("Coletando e processando os dados..."):
        df = collect_data()
        df = process_data(df)
        st.session_state["df"] = df  # Salvando o DataFrame na sessão
    st.success("Dados carregados com sucesso!")

# 🔹 Se os dados já foram carregados, exibir visualizações
if "df" in st.session_state:
    df = st.session_state["df"]
    
    # 📊 Mostrar os primeiros registros
    st.subheader("Visualização dos Dados")
    st.write(df.head())

    # 📌 Criar os gráficos de análise
    visualize_data(df)
else:
    st.warning("Clique no botão acima para carregar os dados.")
