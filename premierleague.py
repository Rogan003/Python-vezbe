import numpy as np

bodovi = []
cena = []
for i in range(3):
    bodovi.append(int(input("Unesite bodove "+ str(i+1) +". kluba:")))
    cena.append(float(input("Unesite cenu "+ str(i+1) +". kluba:")))

bodovi = np.array(bodovi)
cena = np.array(cena)

print("Bodovi:")
print(bodovi)
print("Cena:")
print(cena)
print('\n')

print("Najveci bodovi:")
print(max(bodovi))
print("Najmanji bodovi:")
print(min(bodovi))
print("Najveca cena:")
print(max(cena))
print("Najmanja cena:")
print(min(cena))
print("Razlika:")
print("Bodovi:")
print(np.std(bodovi))
print("Cena:")
print(np.std(cena))
print("Prosek:")
print("Bodovi:")
print(np.mean(bodovi))
print("Cena:")
print(np.mean(cena))
print("Medijana:")
print("Bodovi:")
print(np.median(bodovi))
print("Cena:")
print(np.median(cena))
print("Slicnost napretka kod obe:")
print(np.corrcoef(cena,bodovi)[0,1])
print('\n')

print("Ako se cena 1. poveca za 100 i broj bodova 2. za 10")

cena[0] += 100.0
bodovi[1] += 10

print("Bodovi:")
print(bodovi)
print("Cena:")
print(cena)
print('\n')

print("Najveci bodovi:")
print(max(bodovi))
print("Najmanji bodovi:")
print(min(bodovi))
print("Najveca cena:")
print(max(cena))
print("Najmanja cena:")
print(min(cena))
print("Razlika:")
print("Bodovi:")
print(np.std(bodovi))
print("Cena:")
print(np.std(cena))
print("Prosek:")
print("Bodovi:")
print(np.mean(bodovi))
print("Cena:")
print(np.mean(cena))
print("Medijana:")
print("Bodovi:")
print(np.median(bodovi))
print("Cena:")
print(np.median(cena))
print("Slicnost napretka kod obe:")
print(np.corrcoef(cena,bodovi)[0,1])

ajsajdsaj = input()