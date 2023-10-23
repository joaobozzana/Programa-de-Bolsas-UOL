import pandas as pd

df = pd.read_csv('actors.csv')

frequencia_filmes = df['#1 Movie'].value_counts()

print(frequencia_filmes.head(5))