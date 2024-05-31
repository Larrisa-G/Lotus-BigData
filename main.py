import pandas as pd

df = pd.read_excel('dados_parte_interessada.xlsx')
df = df.drop(0)

df['ano'] = df['data de início'].dt.year
df['mes'] = df['data de início'].dt.month


def maior_media_por_ano(df,coluna):
    media = df.groupby(['ano', 'mes'])[coluna].mean().reset_index()
    return media.loc[media.groupby('ano')[coluna].idxmax()]

def menor_media_por_ano(df,coluna):
    media = df.groupby(['ano', 'mes'])[coluna].mean().reset_index()
    return media.loc[media.groupby('ano')[coluna].idxmin()]

def frequencia_geral(df,coluna):
    return df[coluna].value_counts().reset_index()

def frequencia_anual(df, coluna):
    return df.groupby('ano')[coluna].value_counts().reset_index()

def moda(df, coluna):
    df[coluna].mode()

def moda_mensal(df, coluna):
    df.groupby('mes')[coluna].apply(lambda x : x.mode()).reset_index

def maior_media_por_mes(df,coluna):
    media = df.groupby(['mes'])[coluna].mean().reset_index()
    return media.loc[media[coluna].idxmax()]

def menor_media_por_mes(df,coluna):
    media = df.groupby(['mes'])[coluna].mean().reset_index()
    return media.loc[media[coluna].idxmin()]

df1 = frequencia_geral(df,'mes')                    # Quantas obras foram realizadas em cada mês
df2 = frequencia_anual(df,'mes')                    # Quantas obras foram realizadas em cada mês de cada ano
df3 =frequencia_anual(df, 'clientes')               # Quantas vezes cada cliente contratou os serviços da empresa por ano
df4 =maior_media_por_ano(df,'classificação')        # Mês com maior média de satisfação
df5 = menor_media_por_ano(df, 'administração')      # Mês com menor média de lucro do ano
df6 = moda(df,'clientes')                           # Calcula a moda
df7 = moda_mensal(df,'clientes')                    # Calcula a moda mensal
df8 = maior_media_por_mes(df,"classificação")       # mostrar o mês que teve maior média de notas de classificação
df9 = menor_media_por_mes(df,'administração')       # mostrar o mês que menos gera lucro

df1.to_excel("obras_realizadas_desde_fundação .xlsx")
df2.to_excel("obras_realizadas_mensalmente.xlsx") 
df4.to_excel("meses_maior_satisfação.xlsx")
df5.to_excel("meses_menor_lucro.xlsx")
df8.to_excel("mês_maior_satisfação.xlsx")
df9.to_excel("mês_menor_lucro.xlsx")