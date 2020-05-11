import matplotlib.pyplot as plt
import numpy as np
from random import randint as rand

class Swimmer:

    worldRecord = 20.91

    def __init__(self,medals,age,wr):
        self.medals = medals
        self.age = age
        self.wr = wr

    def predstavljanje(self):
        print("Godine: "+ str(self.age))
        print("Broj medalja: "+ str(self.medals))
        print("Svetski rekordi: "+ str(self.wr))
        print("----------")

    def ostari(self):
        self.age += 1
    
    def dodajMedalju(self):
        self.medals += 1

    def oboriRekord(self):
        self.wr += 1

    @classmethod
    def pocetnik(cls,age):
        return cls(0,age,0)
    
    @classmethod
    def noviSvetski(cls,rekord):
        cls.worldRecord = rekord
    
    @staticmethod
    def olimpijada(godina):
        if godina % 4 == 0:
            return True
        else:
            return False

ja = Swimmer.pocetnik(17)
adampeaty = Swimmer(2,25,11)

ja.predstavljanje()
adampeaty.predstavljanje()

ja.ostari()
ja.dodajMedalju()

ja.predstavljanje()

adampeaty.oboriRekord()
adampeaty.predstavljanje()

print(ja.worldRecord)

adampeaty.noviSvetski(20.58)

print(ja.worldRecord)

if ja.olimpijada(2019):
    print("Jeste")
else:
    print("Nije")

print("----------")

godine = []
rekordi = []
medalje = []

for i in range(100):
    y = rand(15,35)
    x = rand(0,7) + y - 25
    z = rand(0,5) + y - 25
    if z<0: z = 0
    if x<0: x = 0
    primer = Swimmer(x,y,z)
    godine.append(primer.age)
    rekordi.append(primer.wr)
    medalje.append(primer.medals)

godine = np.array(godine)
rekordi = np.array(rekordi)
medalje = np.array(medalje)

print(np.mean(godine))
print(np.mean(rekordi))
print(np.mean(medalje))

fig,ax = plt.subplots()
ax.set_title("Odnos godina i rekorda")
ax.set_xlabel("Rekordi")
ax.set_ylabel("Godine")
ax.scatter(rekordi,godine)
fig.show()

fig,ax = plt.subplots()
ax.set_title("Odnos godina i rekorda")
ax.set_ylabel("Rekordi")
ax.set_xlabel("Godine")
ax.bar(np.sort(godine),rekordi)
fig.show()

nista = input()

fig,ax = plt.subplots()
ax.set_title("Odnos godina i medalja")
ax.set_xlabel("Medalje")
ax.set_ylabel("Godine")
ax.scatter(medalje,godine)
fig.show()

fig,ax = plt.subplots()
ax.set_title("Odnos godina i medalja")
ax.set_ylabel("Medalje")
ax.set_xlabel("Godine")
ax.bar(np.sort(godine),medalje)
fig.show()

nista = input()

plt.hist(godine, bins = 10)
plt.show()
plt.hist(rekordi, bins = 10)
plt.show()

nista = input()