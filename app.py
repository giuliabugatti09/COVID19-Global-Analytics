import streamlit as st
import pandas as pd
import sys
import os

# 🔹 Adicionando o diretório 'scripts' ao path para importar os módulos
script_path = os.path.abspath("scripts")
sys.path.append(script_path)

# 🔹 Tentando importar as funções dos módulos de forma segura
try:
    from scripts.coleta_dados.py import collect_data
    from scripts.limpeza_dados.py import process_data
    from scripts.visualizacao_dados.py import visualize_data
except ImportError as e:
    st.error(f"Erro ao importar módulos: {e}")
    sys.exit()

# 🔹 Configuração do título do app no Streamlit
st.title("Análise Global da COVID-19 📊")

# 🔹 Função para carregar e processar os dados
def carregar_dados():
    with st.spinner("Coletando e processando os dados..."):
        df = collect_data()  # Coleta os dados
        df = process_data(df)  # Processa os dados
        st.session_state["df"] = df  # Salvando o DataFrame na sessão
    st.success("Dados carregados com sucesso!")

# 🔹 Botão para carregar os dados
if st.button("Carregar Dados"):
    carregar_dados()

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
