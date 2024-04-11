import pandas as pd


url = 'https://github.com/LucasSampaioo/tep_pandas_pratica_1/blob/main/heart.csv'

# 1. Ler o conjunto de dados para um DataFrame
df = pd.read_csv(url, sep=',')
# 2. Verificar as primeiras linhas do DataFrame usando `head()`x
df.head(n=6)
# 3. Verificar as últimas linhas do DataFrame usando `tail()`
df.tail(5)
# 4. Verificar as dimensões do DataFrame usando `shape`
df.shape()
# 5. Verificar as informações sobre as colunas do DataFrame usando `info()`
df.info()
# 6. Verificar as estatísticas descritivas básicas do DataFrame usando `describe()`
df.describe()
# 7. Selecionar colunas específicas do DataFrame usando colchetes `[]` ou o método `loc[]`
df['age']
# 8. Selecionar linhas específicas do DataFrame usando o método `loc[]`
df.loc[:, ['age', 'cp']]

