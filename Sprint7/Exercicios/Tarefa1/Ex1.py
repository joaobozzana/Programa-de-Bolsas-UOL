import pandas as pd

df = pd.read_csv('actors.csv')

soma = df.groupby('Actor')['Number of Movies'].sum()
ator = soma.idxmax()
filmes = soma.max()

print(f'O ator com a maior numero de filmes é {ator} com um total de {filmes}.')
