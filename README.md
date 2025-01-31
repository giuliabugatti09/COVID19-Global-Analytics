**Análise de Dados da COVID-19 com IA**

📊 Sobre o Projeto

Este projeto tem como objetivo analisar a evolução dos casos de COVID-19 ao redor do mundo, correlacionando com medidas de controle, como lockdowns e campanhas de vacinação. A análise foi realizada utilizando Python e bibliotecas de ciência de dados e visualização, como Pandas, Matplotlib e Seaborn.

📒 Dados Utilizados

Os dados utilizados foram extraídos do repositório oficial do Our World in Data, garantindo informações atualizadas e confiáveis.

🔧 ##Tecnologias Utilizadas

Python

Pandas

Matplotlib

Seaborn

Google Colab (para execução dos notebooks)

**Dicionário das variáveis**

- `aged_65_older`: Parcela da população com 65 anos ou mais, ano mais recente disponível
- `aged_70_older`: Parcela da população com 70 anos ou mais em 2015
- `cardiovasc_death_rate`: Taxa de mortalidade por doença cardiovascular em 2017 (número anual de mortes por 100.000 pessoas)
- `continent`: Continente da localização geográfica
- `date`: Data da observação
- `diabetes_prevalence`: Prevalência de diabetes (% da população de 20 a 79 anos) em 2017
- `extreme_poverty`: Percentual da população que vive em extrema pobreza, ano mais recente disponível desde 2010
- `female_smokers`: Proporção de mulheres que fumam, ano mais recente disponível
- `gdp_per_capita`: Produto interno bruto em paridade de poder de compra (dólares internacionais constantes de 2011), ano mais recente disponível
- `handwashing_facilities`: Percentagem da população com instalações básicas de lavagem das mãos nas instalações, ano mais recente disponível
- `hospital_beds_per_thousand`: Camas hospitalares por 1.000 pessoas, ano mais recente disponível desde 2010
- `hosp_patients`: Número de pacientes com COVID-19 no hospital em um determinado dia
- `hosp_patients_per_million`: Número de pacientes com COVID-19 no hospital em um determinado dia por 1.000.000 de pessoas
- `human_development_index`: Um índice composto que mede o desempenho médio em três dimensões básicas do desenvolvimento humano – uma vida longa e saudável, conhecimento e um padrão de vida decente.
- `icu_patients`: Número de pacientes com COVID-19 em unidades de terapia intensiva (UTIs) em um determinado dia
- `icu_patients_per_million`: Número de pacientes com COVID-19 em unidades de terapia intensiva (UTIs) em um determinado dia por 1.000.000 de pessoas
- `iso_code`: Código do país de três letras
- `life_expectancy`: Expectativa de vida ao nascer em 2019
- `location`: Localização geográfica
- `male_smokers`: Proporção de homens que fumam, ano mais recente disponível
- `median_age`: Idade média da população, projeção da ONU para 2020
- `new_cases`: Novos casos confirmados de COVID-19. As contagens podem incluir casos prováveis, quando relatados.
- `new_cases_per_million`: Novos casos confirmados de COVID-19 por 1.000.000 de pessoas. As contagens podem incluir casos prováveis, quando relatados.
- `new_cases_smoothed`: Novos casos confirmados de COVID-19 (suavizado de 7 dias). As contagens podem incluir casos prováveis, quando relatados.
- `new_cases_smoothed_per_million`: Novos casos confirmados de COVID-19 (suavizado em 7 dias) por 1.000.000 de pessoas. As contagens podem incluir casos prováveis, quando relatados.
- `new_deaths`: Novas mortes atribuídas ao COVID-19. As contagens podem incluir mortes prováveis, quando relatadas.
- `new_deaths_per_million`: Novas mortes atribuídas ao COVID-19 por 1.000.000 de pessoas. As contagens podem incluir mortes prováveis, quando relatadas.
- `new_deaths_smoothed`: Novas mortes atribuídas ao COVID-19 (suavizado de 7 dias). As contagens podem incluir mortes prováveis, quando relatadas.
- `new_deaths_smoothed_per_million`: Novas mortes atribuídas ao COVID-19 (suavizado de 7 dias) por 1.000.000 de pessoas. As contagens podem incluir mortes prováveis, quando relatadas.
- `new_people_vaccinated_smoothed`: Número diário de pessoas que recebem sua primeira dose de vacina (suavizado de 7 dias)
- `new_people_vaccinated_smoothed_per_hundred`: Número diário de pessoas que recebem sua primeira dose de vacina (suavizado de 7 dias) por 100 pessoas na população total
- `new_tests`: Novos testes para COVID-19 (calculado apenas para dias consecutivos)
- `new_tests_per_thousand`: Novos testes para COVID-19 por 1.000 pessoas
- `new_tests_smoothed`: Novos testes para COVID-19 (suavizado de 7 dias). Para países que não relatam dados de teste diariamente, assumimos que os testes mudaram igualmente diariamente em todos os períodos em que nenhum dado foi relatado. Isso produz uma série completa de números diários, que são então calculados em uma janela contínua de 7 dias
- `new_tests_smoothed_per_thousand`: Novos testes para COVID-19 (suavizado de 7 dias) por 1.000 pessoas
- `new_vaccinations`: Novas doses de vacinação COVID-19 administradas (calculadas apenas para dias consecutivos)
- `new_vaccinations_smoothed`: Novas doses de vacinação COVID-19 administradas (suavizado por 7 dias). Para países que não relatam dados de vacinação diariamente, assumimos que a vacinação mudou igualmente diariamente em todos os períodos em que nenhum dado foi relatado. Isso produz uma série completa de números diários, que são então calculados em uma janela contínua de 7 dias
- `new_vaccinations_smoothed_per_million`: Novas doses de vacinação COVID-19 administradas (suavizadas em 7 dias) por 1.000.000 de pessoas na população total
- `new_vaccinations_smoothed_per_thousand`: Novas doses de vacinação


📈 Análises Realizadas

1️⃣ Média de Casos e Mortes: Brasil vs. Mundo

Arquivo: media_covid_brasil_mundo.png

Este gráfico compara a média móvel de casos e mortes por COVID-19 no Brasil com a média global, destacando tendências ao longo do tempo.

2️⃣ Porcentagem de Doses Aplicadas

Arquivo: porcentagem_doses_vacina.png

Mostra a proporção da população que recebeu pelo menos uma dose da vacina e as doses de reforço aplicadas, ajudando a entender a cobertura vacinal.

3️⃣ Percentual de Vacinados vs. Mortes

Arquivo: percentual_vacinados_mortes.png

Analisa a correlação entre a taxa de vacinação e a redução do número de mortes, evidenciando o impacto da imunização.

4️⃣ Países com Mais Casos Acumulados de COVID-19

Arquivo: paises_mais_casos_covid.png

Um ranking dos países com os maiores números de casos acumulados de COVID-19 ao longo do tempo.

5️⃣ Países com Mais Casos Atuais de COVID-19

Arquivo: paises_mais_casos_atuais_covid.png

Exibe os países com os maiores números de casos ativos no momento da análise.

6️⃣ Média de Casos e Mortes por COVID-19

Arquivo: media_casos_mortes_covid.png

Gráfico de linha mostrando a evolução das médias móveis de casos e mortes globalmente.

7️⃣ Média de Casos de COVID-19 no Brasil

Arquivo: media_casos_covid_brasil.png

Um zoom específico na média móvel de casos no Brasil, evidenciando picos e quedas da pandemia no país.

8️⃣ Matriz de Correlação: Impacto nos Idosos e Adultos

Arquivo: matriz_correlacao_idosos_adultos.png

Um heatmap que mostra a correlação entre idade e gravidade da COVID-19, analisando dados de idosos e adultos.

9️⃣ Gráfico de Dispersão: PIB vs. Mortalidade

Arquivo: grafico_dispersao_pib.png

Analisa a relação entre PIB per capita e o número total de mortes por milhão de habitantes, observando padrões entre diferentes continentes.

🔟 Relação entre Mortalidade de Idosos por COVID-19 e Continente

Arquivo: relacao_morte_idosos_covid_continente.png

Compara a taxa de mortalidade de idosos em diferentes continentes, ajudando a identificar padrões regionais na gravidade da pandemia.


🛠️ Como Executar

Clone este repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```
Instale as dependências necessárias:
```bash
pip install pandas matplotlib seaborn
```
Execute o notebook no Google Colab ou localmente:

jupyter notebook


📚 Referências

Our World in Data - COVID-19 Dataset

Johns Hopkins University COVID-19 Dashboard

Desenvolvido por Giulia. 🌟 Conecte-se comigo no LinkedIn.
