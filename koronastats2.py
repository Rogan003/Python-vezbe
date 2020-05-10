import matplotlib.pyplot as plt
import numpy as np

velicina = []
godine = []

fig,ax = plt.subplots()
ax.set_title("Odnos broja velicine grada i broja godina")
ax.set_xlabel("Velicina grada")
ax.set_ylabel("Broj godina")

for i in range(10):
    broj = input("Novi slucajevi: ")
    
    for j in broj:
        x = input("Velicina grada: ")
        y = input("Broj godina: ")
        velicina.append(x)
        godine.append(y)
    
    grad = np.array(velicina)
    god = np.array(godine)
    ax.scatter(grad,god)
    fig.show()

nista = input()