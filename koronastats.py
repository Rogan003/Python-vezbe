import numpy as np
import matplotlib.pyplot as plt
from random import randint as rand

godine = np.random.randint(15,90,size = 1000)
velicinaGrada = np.random.randint(1,10,size = 1000)
sanse = []
for i in range(1000):
    if godine[i]>40:
        sanse.append(godine[i] - 10 + rand(0,10) + velicinaGrada[i])
    elif godine[i]<30:
        sanse.append(0 + rand(0,10) - 10 + velicinaGrada[i])
    else:
        sanse.append(godine[i] - 40 + rand(0,10) + velicinaGrada[i])
sanseZaSmrt = np.array(sanse)

print(np.mean(godine))
print(np.median(godine))
print(np.std(godine))

fig,ax = plt.subplots()
ax.set_title("GODINE")
ax.set_xlabel("Vrednosti podeljene u 10 grupa")
ax.set_ylabel("Broj godina")
ax.hist(godine,bins = 10)
fig.show()

nista = input()

print(np.mean(velicinaGrada))
print(np.median(velicinaGrada))
print(np.std(velicinaGrada))

fig,ax = plt.subplots()
ax.set_title("Velicina grada")
ax.set_xlabel("Vrednosti podeljene u 5 grupa")
ax.set_ylabel("Rangirana velicina grada")
ax.hist(velicinaGrada,bins = 5)
fig.show()

nista = input()

print(np.mean(sanseZaSmrt))
print(np.std(sanseZaSmrt))

fig,ax = plt.subplots()
ax.set_title("Odnos sansi za smrt i godina")
ax.set_xlabel("Broj godina")
ax.set_ylabel("Sanse za smrt")
ax.scatter(godine,sanseZaSmrt)
fig.show()

nista = input()