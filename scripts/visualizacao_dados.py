import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests

# 🔹 Função de Coleta de Dados
def collect_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.json"
    response = requests.get(url)
    data = response.json()

    # Criar DataFrame a partir dos dados coletados
    df = pd.DataFrame(data).transpose()
    return df

# 🔹 Função de Processamento e Limpeza de Dados
def process_data(df):
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

# 🔹 Função de Visualização dos Dados
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

    # 📌 Gráfico 2️⃣: Relação entre Casos e Mortes (dispersão) para os 20 maiores países
    plt.figure(figsize=(12, 8))

    # 🔹 Ajustar a coluna de 'total_cases' e 'total_deaths' para milhões
    df['total_cases_millions'] = df['total_cases'] / 1_000_000
    df['total_deaths_millions'] = df['total_deaths'] / 1_000_000

    # 🔹 Filtrar os 20 países com mais casos para o gráfico
    top_20_countries = df.nlargest(20, 'total_cases')

    # 🔹 Ajuste de zoom: aumentando o intervalo de valores para "dar mais espaço" entre os pontos
    plt.xlim(0, top_20_countries['total_cases_millions'].max() * 1.3)  # Ajusta a escala do eixo x
    plt.ylim(0, top_20_countries['total_deaths_millions'].max() * 1.3)  # Ajusta a escala do eixo y

    # 🔹 Plotando um gráfico de dispersão com rótulos de países
    scatter_plot = sns.scatterplot(data=top_20_countries, x='total_cases_millions', y='total_deaths_millions',
                                   alpha=0.7, s=100, color='b', hue='location', legend=False)

    # 🔹 Adicionando rótulos para cada ponto (apenas os top 20 países)
    for i, row in top_20_countries.iterrows():
        scatter_plot.text(row['total_cases_millions'], row['total_deaths_millions'],
                          row['location'], fontsize=9, ha='right', va='bottom', color='black', alpha=0.7)

    # 🔹 Melhorando o título e rótulos
    plt.xlabel("Total de Casos (milhões)")
    plt.ylabel("Total de Mortes (milhões)")
    plt.title("Relação entre Casos e Mortes de COVID-19 (Top 20 Países)")

    plt.grid(True)
    plt.show()

# 🔹 Função principal
def main():
    # Coleta os dados
    df = collect_data()
    print("Dados coletados com sucesso!")

    # Exibe as primeiras linhas dos dados para verificação
    print(df.head())

    # Processa os dados
    df = process_data(df)

    # Visualiza os dados
    visualize_data(df)

# 🔹 Executar o código
if __name__ == "__main__":
    main()
