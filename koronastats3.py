import matplotlib.pyplot as plt
import numpy as np
from random import randint as rand

plt.ion()

rez = [0]
pom = 0
lista = [pom]
zbir = 0

for i in range(300):
    plt.xlabel("Vreme")
    plt.ylabel("Zarazeni")
    plt.title("Odnos zarazenih vremenom")
    plt.plot(lista,rez, color = 'red')
    plt.fill_between(lista,rez,0,color = 'red')
    plt.show()
    plt.pause(0.0001)
    if i != 299:
        plt.clf()
    pom += 1
    lista.append(pom)
    b = rand(1,10)
    if len(rez) <= 50 or len(rez) >= 280:
        if b > 8:
            a = 0
        else:
            a = rand(1,5)
    else:
        if b > 3:
            a = 0
        else:
            a = rand(1,4)
    zbir += a
    rez.append(zbir)

nesto = input()