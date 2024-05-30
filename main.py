import pandas as pd

df = pd.read_excel('dados_parte_interessada.xlsx')
df = df.drop(0)

df['ano'] = df['data de início'].dt.year
df['mes'] = df['data de início'].dt.month

#reset_index - para garantir o padrão dos index
media_classificação = df.groupby(['ano', 'mes'])['classificação'].mean().reset_index()

meses_maior_satisfação = media_classificação.loc[media_classificação.groupby('ano')['classificação'].idxmax()]
meses_menor_satisfação = media_classificação.loc[media_classificação.groupby('ano')['classificação'].idxmin()]

df['lucro'] = df.apply(lambda x : x['valor final da obra'] * 0.03, axis=1)
df['preço cobrado'] = df.apply(lambda x : x['valor final da obra'] + x['lucro'], axis=1)

df_meses_menor_lucro = df.loc[df.groupby('ano')['lucro'].idxmin()] 
df_meses_maior_lucro = df.loc[df.groupby('ano')['lucro'].idxmax()]

df_clientela = df['clientes'].value_counts().reset_index()
