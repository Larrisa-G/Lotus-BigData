import pandas as pd

df = pd.read_excel('dados_parte_interessada.xlsx')
df = df.drop(0)

df['ano'] = df['data de início'].dt.year
df['mes'] = df['data de início'].dt.month

df['lucro'] = df.apply(lambda x : x['valor final da obra'] * 0.03, axis=1)
df['preço cobrado'] = df.apply(lambda x : x['valor final da obra'] + x['lucro'], axis=1)

def maior_media(df,coluna):
    media = df.groupby(['ano', 'mes'])[coluna].mean().reset_index()
    return media.loc[media.groupby('ano')[coluna].idxmax()]

def menor_media(df,coluna):
    media = df.groupby(['ano', 'mes'])[coluna].mean().reset_index()
    return media.loc[media.groupby('ano')[coluna].idxmin()]

def frequencia_geral(df,coluna):
    return df[coluna].value_counts().reset_index()

def frequencia_anual(df, coluna):
    return df.groupby('ano')[coluna].value_counts().reset_index()


frequencia_geral(df,'mes')  #Quantas obras foram realizadas em cada mês
frequencia_anual(df,'mes')  #Quantas obras foram realizadas em cada mês de cada ano
maior_media(df,'lucro')
menor_media(df, 'lucro')