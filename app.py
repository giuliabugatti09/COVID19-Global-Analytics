import streamlit as st
import sys
import os

# Adiciona a pasta "scripts" ao caminho do Python
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))

# Importando os módulos de coleta, limpeza e visualização de dados
from coleta_dados import collect_data
from limpeza_dados import process_data
from visualizacao_dados import visualize_data

def main():
    st.title("Análise Global da COVID-19")
    st.write("Este aplicativo exibe insights sobre os casos de COVID-19 ao redor do mundo.")
    
    # Botão para carregar os dados
    if st.button("Carregar Dados"):
        with st.spinner("Coletando dados..."):
            df = collect_data()
            df = process_data(df)
            st.session_state.df = df  # Armazena os dados na sessão
        st.success("Dados carregados com sucesso!")
    
    # Exibir os dados
    if "df" in st.session_state:
        st.subheader("Prévia dos Dados")
        st.dataframe(st.session_state.df.head())
        
        # Visualização dos gráficos
        st.subheader("Visualização dos Dados")
        visualize_data(st.session_state.df)  # Chama a função para gerar os gráficos

if __name__ == "__main__":
    main()
