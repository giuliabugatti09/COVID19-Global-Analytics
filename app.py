import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import matplotlib.dates as mdates

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

# Função de Processamento e Limpeza de Dados
def process_visual_data(df):
    # Substituindo valores negativos por NaN
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = df[numeric_columns].applymap(lambda x: x if x >= 0 else np.nan)

    # Remover países com dados ausentes (NaN)
    df = df.dropna(subset=["total_cases", "total_deaths"])

    # Preencher valores ausentes com 0
    df = df.fillna(0)

    # Remover a linha de "World" que é o total mundial
    df = df[df["location"] != "World"]

    # Remover continentes da análise
    continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
    df = df[~df["location"].isin(continents)]

    # Remover países classificados como "income countries"
    income_countries = ['High-income countries', 'Low-income countries', 'Lower-middle-income countries', 'Upper-middle-income countries']
    df = df[~df["location"].isin(income_countries)]

    # Remover a União Europeia
    df = df[df["location"] != "European Union"]

    return df

# Função de Visualização dos Dados
def visualize_data(df):
    total_cases_world = df["total_cases"].sum()  # Total de casos no mundo
    df["percentage_world"] = (df["total_cases"] / total_cases_world) * 100  # Percentual de casos por país

    # 📊 Gráfico 1: Casos totais por país (Top 20)
    plt.figure(figsize=(12, 8))
    top_countries = df.nlargest(20, "total_cases")
    ax = sns.barplot(data=top_countries, x="total_cases", y="location", palette="Blues_d")

    # 🔹 Ajustando e formatando o eixo X com "milhões" de 10 em 10 milhões
    ax.set_xlabel("Total de Casos (em milhões)")
    ax.set_xticks(np.arange(0, max(top_countries["total_cases"]), step=10000000))  # Intervalo de 10 milhões
    ax.set_xticklabels([f"{x/1e6:.1f}M" for x in ax.get_xticks()])

    # 🔹 Colocar a porcentagem dentro das barras (branca e bem posicionada)
    for i, v in enumerate(top_countries["total_cases"]):
        ax.text(v / 2, i, f"{top_countries['percentage_world'].iloc[i]:.2f}%",
                color='white', ha="center", va="center", fontweight='bold')

    plt.ylabel("Países")
    plt.title("Top 20 Países com mais Casos de COVID-19")
    plt.xticks(rotation=45, ha='right')
    plt.show()

    # 📊 Gráfico 2️⃣: Comparação de Casos e Mortes (barras) para 5 países específicos em milhões
    plt.figure(figsize=(14, 8))

    # 🔹 Selecionar os 5 países específicos
    countries = ['Brazil', 'India', 'United States', 'Russia', 'United Kingdom']
    top_countries = df[df['location'].isin(countries)]

    # 🔹 Ajustar os dados para o gráfico de barras em milhões
    top_countries['total_cases_millions'] = top_countries['total_cases'] / 1_000_000
    top_countries['total_deaths_millions'] = top_countries['total_deaths'] / 1_000_000

    # 🔹 Criar gráfico de barras agrupadas
    total_cases = top_countries.set_index('location')['total_cases_millions']
    total_deaths = top_countries.set_index('location')['total_deaths_millions']
    top_countries_comparison = pd.DataFrame({'Total Cases (M)': total_cases, 'Total Deaths (M)': total_deaths})

    top_countries_comparison.plot(kind='bar', color=['blue', 'red'], figsize=(14, 8))

    plt.xlabel('Países')
    plt.ylabel('Número Total (Milhões)')
    plt.title('Comparação de Casos e Mortes de COVID-19 em 5 Países (em Milhões)')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Legenda')
    plt.grid(True)
    plt.show()

# Função de coleta de dados diários de um país específico
def collect_daily_data(country):
    url = f"https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/full_data.csv"
    response = requests.get(url)
    df = pd.read_csv(url)
    df = df[df['location'] == country]  # Filtrar pelo país específico
    return df

# Função de visual
