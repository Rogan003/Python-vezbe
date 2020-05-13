import pandas as pd

df = pd.read_excel('Static files/TransferLista.xlsx')

print(df)
print(df["Ime"])
print(df.sort_values("Cena(u milionima)", ascending = False))

df["Cena(posle Covid-19)"] = df["Cena(u milionima)"] * 95 / 100

print(df)

print(df.loc[df["Cena(posle Covid-19)"] > 150])

naziv = float(input())

print(df.loc[df["Cena(posle Covid-19)"] == naziv])

print(df.describe())

df = df.drop(columns = ["Cena(posle Covid-19)"])

print(df)

nesto = input()