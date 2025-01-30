import requests

def fetch_data(url):
    # Envia uma solicitação GET para a URL da API
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida (código 200)
    if response.status_code == 200:
        return response.json()  # Retorna a resposta em formato JSON
    else:
        print(f"Erro ao acessar a API: Código de resposta {response.status_code}")
        return None

def main():
    # URL da API (dados mais recentes da COVID-19)
    api_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.json"

    # Coleta os dados
    data = fetch_data(api_url)

    if data:
        print("Dados coletados com sucesso!")
        # Accessing the first two countries' data using a loop and keys
        # Assuming countries are stored with their country codes as keys.
        # Replace "country_code1", "country_code2" with actual country codes.
        for i, country_code in enumerate(["OWID_AFR", "OWID_ASI"]):  # Replace with actual country codes
            if i >= 2:
                break # break after printing two records
            print(data[country_code])

if __name__ == "__main__":
    main()