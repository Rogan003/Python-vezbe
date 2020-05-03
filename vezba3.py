from math import sqrt as koren
import random
def randomLista(x):
    lista=[]
    for i in range(x):
        lista.append(random.randint(5,15))
    return lista
unos=int(input("Unesite neki broj: "))
lista=randomLista(unos)
print("Koren iz sume random liste je: "+str(koren(sum(lista))))