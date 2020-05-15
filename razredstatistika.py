import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('Static files/Dnevnik I-5.xlsx')

print(np.array(df.loc[df['Prosek'].notna()]['Prosek']).mean())
print(np.array(df.loc[df['Prosek'].notna()]['Prosek']).max())
print(np.array(df.loc[df['Prosek'].notna()]['Prosek']).min())
print(np.array(df.loc[df['Prosek'].notna()]['Prosek']).std())

fig,ax = plt.subplots()
ax.set_title("Odnos proseka ucenika")
ax.set_xlabel("Ucenici")
ax.set_ylabel("Proseci")
ax.bar(df.loc[df['Ime'].notna()]['Ime'],df.loc[df['Prosek'].notna()]['Prosek'])
fig.show()

nesto = input()

print(df.loc[df['Matematika'] == 5]['Ime'])

fig,ax = plt.subplots()
ax.set_title("Odnos proseka ucenika")
ax.set_xlabel("Ucenici")
ax.set_ylabel("Proseci")
ax.bar(df.loc[df['Ime'].notna()]['Ime'],df.loc[df['Matematika'].notna()]['Matematika'])
fig.show()

nesto = input()