import pandas as pd

df = pd.read_excel('dados_parte_interessada.xlsx')

df['ano'] = df['data de início'].dt.year
df['mes'] = df['data de início'].dt.month

#reset_index - para garantir o padrão dos index
media_classificação = df.groupby(['ano', 'mes'])['classificação'].mean().reset_index()

meses_maior_satisfação = media_classificação.loc[media_classificação.groupby('ano')['classificação'].idxmax()]
print(meses_maior_satisfação)

meses_menor_satisfação = media_classificação.loc[media_classificação.groupby('ano')['classificação'].idxmin()]
print(meses_menor_satisfação)