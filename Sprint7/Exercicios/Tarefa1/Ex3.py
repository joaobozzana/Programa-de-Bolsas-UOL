import pandas as pd

df = pd.read_csv('actors.csv')
ator_maior_media = df.loc[df['Average per Movie'].idxmax()]['Actor']

print(f'O ator com a maior média por filme é {ator_maior_media}.')
