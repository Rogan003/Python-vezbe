import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('Static files/TransferLista.xlsx')

print(df.describe())

nesto = input()

lige = list(set(df["Liga"]))
print(lige)
cene = [0,0,0,0,0]
for i in range(5):
    cene[i] = sum(df.loc[df['Liga'] == lige[i],['Cena(u milionima)']]['Cena(u milionima)'])

print(cene)

fig,ax = plt.subplots()
ax.set_title("Vrednosti fudbalera u razlicitim ligama")
ax.set_xlabel("Lige")
ax.set_ylabel("Cene(u milionima)")
ax.bar(lige,cene)
fig.show()

nesto = input()

fig,ax = plt.subplots()
ax.set_title("Vrednosti fudbalera")
ax.set_xlabel("Fudbaleri")
ax.set_ylabel("Cene(u milionima)")
ax.bar(df['Ime'],df['Cena(u milionima)'])
fig.show()

nesto = input()