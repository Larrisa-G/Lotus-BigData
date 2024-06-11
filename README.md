# Big data

<p>Trabalho extencionista para a diciplina de Tópicos de Big Data em Python</p>

## Requisitos 



- Visual Studio (com Python Development Workload)
- Python 3.x
- Pandas
- openpyxl
- typing (incluído na biblioteca padrão do Python)


## Funções


**1** `frequencia_geral(df, coluna)` : Calcula frequência de uma colunaespecífica do DataFrame.

Exemplo de uso : Descobrir quantas obras foram realizadas em cada cliente desde a fundação da empresa.

**2.** `frequencia_anual(df,coluna)` : Calcula a frequência anual de um evento em uma coluna. 

Exemplo de uso : Mensurar quantas obras foram realizadas em cada mês de cada ano.

**3.** `maior_media_por_ano(df, coluna)` : Calcula a média por mês de uma coluna e mostra qual foi a maior média do ano. 

Exemplo de uso : Indicar qual o mês em que as obras formam mais bem avaliadas, e sua média de classificação.

**4** `menor_media_por_ano(df, coluna)` : Calcula a média por mês de uma coluna e mostra qual foi a menor média anual. 

Exemplo de uso : Mostrar o mês com menor média de lucro do ano.

**5** `moda(df,coluna)` : Calcula a moda de uma coluna específica. 

Exemplo de uso : Mostrar o cliente que mais contratou a empresa desde sua fundação.

**6** `moda_mensal(df,coluna)` : Calcula a moda mensal de uma coluna. 

**7** `maior_media_por_mes(df,coluna)` : Calcula a média por mês e mostra qual foi a maior.

Exemplo de uso : Mostrar o mês que teve mais lucro ao longo dos anos

**8** `maior_media_por_mes(df,coluna)` : Calcula a média por mês de uma coluna específica e mostra qual foi a menor.

Exemplo de uso : Mostrar o mês que teve o menor lucro ao longo dos anos

**9** `calcular_inflacao_acumulada(ipcas_anuais : List[float])` : Calcula a inflação acumulada a partir de uma lista de percentuais anuais do IPCA.

Exemplo de uso : Calcular a inflação acumulada dos anos que não foram informados os dados na tabela.

**10** `previsao(df,coluna, ipcas : List[float])` : Aplica a inflação acumulada para prever valores em uma coluna.

Exemplo de uso : Prever o valor do material para o ano de 2024 tendo como referência a coluna com os valores do ano de 2020