import numpy as np

lista = [[1,2,3],[4,5,6]]
niz = np.array(lista)

print(niz)

print(niz.sum())

niz2 = np.ones((2,3),dtype = int)

print(niz+niz2)

niz2[0,0] = 6
niz2[1,2] = 5

print(niz2)

print(np.mean(niz2))

kosdsodfk = input()