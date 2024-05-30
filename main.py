import pandas as pd

df = pd.read_excel('dados_parte_interessada.xlsx')
df = df.drop(0)

df['ano'] = df['data de início'].dt.year
df['mes'] = df['data de início'].dt.month

df['lucro'] = df.apply(lambda x : x['valor final da obra'] * 0.03, axis=1)
df['preço cobrado'] = df.apply(lambda x : x['valor final da obra'] + x['lucro'], axis=1)

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

frequencia_geral(df,'mes')              # Quantas obras foram realizadas em cada mês
frequencia_anual(df,'mes')              # Quantas obras foram realizadas em cada mês de cada ano
frequencia_anual(df, 'clientes')        # Quantas vezes cada cliente contratou os serviços da empresa por ano
maior_media_por_ano(df,'lucro')         # Mês com maior média de lucro do ano
menor_media_por_ano(df, 'lucro')        # Mês com menor média de lucro do ano
moda(df,'clientes')                     # Calcula a moda
moda_mensal(df,'clientes')              # Calcula a moda mensal
maior_media_por_mes(df,"classificação")
menor_media_por_mes(df,'lucro')
