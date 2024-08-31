#json
[
    {"dia": 1, "valor": 22174},
    {"dia": 2, "valor": 24537.66},
    {"dia": 3, "valor": 26139.61},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.66},
    ...
]

import pandas as pd

df = pd.read_json('faturamento.json')

df_filtrado = df[df['valor'] > 0]


menor_faturamento = df_filtrado['valor'].min()
maior_faturamento = df_filtrado['valor'].max()
media_mensal = df_filtrado['valor'].mean()

dias_acima_da_media = df_filtrado[df_filtrado['valor'] > media_mensal].shape[0]


print(f'Menor valor de faturamento: {menor_faturamento}')
print(f'Maior valor de faturamento: {maior_faturamento}')
print(f'Número de dias com faturamento acima da média: {dias_acima_da_media}')
