import pandas as pd

df = pd.read_csv('actors.csv')

media = df['Number of Movies'].mean()
print(f'A média é: {media:.2f}')
