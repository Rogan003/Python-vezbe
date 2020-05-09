import numpy as np

visine = np.random.random(100) + 1.2
masa = np.random.random(100) + np.random.randint(45,110,size =100)
plata = np.random.randint(250,900,size = 100)
godine = np.random.randint(85,size = 100)

print(np.mean(visine))
print(np.mean(masa))
print(np.mean(plata))
print(np.mean(godine))

print('\n')

print(np.median(visine))
print(np.median(masa))
print(np.median(plata))
print(np.median(godine))

print('\n')

print(np.corrcoef(visine,masa))
print(np.corrcoef(plata,godine))


print('\n')

print(np.std(visine))
print(np.std(masa))
print(np.std(plata))
print(np.std(godine))

aoadjosoja = input()