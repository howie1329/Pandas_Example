import pandas as pd

df = pd.read_csv('pokemon_data.csv')

print(df.head(10))
print(df.iloc[2,1])
print(df.loc[[df['Speed'] > 75]&[df['Type 1'] == "Fire"]])