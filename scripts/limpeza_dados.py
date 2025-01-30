import pandas as pd
import numpy as np
import requests

# Função para coletar os dados da API
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao acessar a API: Código {response.status_code}")
        return None

# Função para processar e limpar os dados
def process_data(data):
    # Transforma o dicionário JSON em um DataFrame
    df = pd.DataFrame.from_dict(data, orient="index")

    # Filtra apenas países (descarta continentes e valores agregados)
    df = df[df["continent"].notna()]  # Remove entradas sem continente (ex: "World", "Asia", "Europe")

    # Seleciona apenas algumas colunas relevantes
    selected_columns = ["location", "total_cases", "total_deaths", "total_vaccinations"]
    df = df[selected_columns]

    # Converte as colunas numéricas para float, ignorando "location"
    numeric_columns = ["total_cases", "total_deaths", "total_vaccinations"]
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

    # Remove valores negativos, substituindo por NaN
    for col in numeric_columns:
        df[col] = df[col].apply(lambda x: np.nan if x < 0 else x)

    # Remove países com menos de 100 vacinados (valores podem estar errados)
    df = df[df["total_vaccinations"] >= 100]

    # Preenche valores ausentes com a média da coluna
    df.fillna(df[numeric_columns].median(), inplace=True)  # Média pode ser afetada por outliers, então usamos a mediana

    return df

def main():
    api_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.json"
    raw_data = fetch_data(api_url)

    if raw_data:
        print("✅ Dados coletados com sucesso!")
        cleaned_data = process_data(raw_data)
        print("\n📊 **Resumo dos Dados Processados:**")
        print(cleaned_data.head())  # Exibe as primeiras linhas do DataFrame

        # Exibe estatísticas gerais
        print("\n📈 Estatísticas básicas:")
        print(cleaned_data.describe())

if __name__ == "__main__":
    main()
