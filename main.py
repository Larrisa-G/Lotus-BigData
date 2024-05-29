import pandas as pd

df = pd.read_excel('dados_parte_interessada.xlsx')

df['ano'] = df['data de início'].dt.year
df['mes'] = df['data de início'].dt.month

media_classificação = df.groupby(['ano', 'mes'])['classificação'].mean
print(df)