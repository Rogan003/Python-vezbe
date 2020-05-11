import matplotlib.pyplot as plt
import numpy as np

velicina = []
godine = []

for i in range(10):
    broj = int(input("Novi slucajevi: "))
    
    for j in range(broj):
        x = int(input("Velicina grada: "))
        y = int(input("Broj godina: "))
        velicina.append(x)
        godine.append(y)
    
    grad = np.sort(np.array(velicina))
    god = np.sort(np.array(godine))
    fig,ax = plt.subplots()
    ax.set_title("Odnos broja velicine grada i broja godina")
    ax.set_xlabel("Velicina grada")
    ax.set_ylabel("Broj godina")
    ax.scatter(grad,god,color = 'red')
    fig.show()

nista = input()