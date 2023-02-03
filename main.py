import pandas as pd


df = pd.read_csv("contratos.csv", encoding="latin-1",sep=";")
print(df.head())
