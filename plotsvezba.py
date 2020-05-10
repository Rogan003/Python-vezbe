import matplotlib.pyplot as plt
import numpy as np

visine = np.random.randint(150,200,size = 50) + np.random.random()
mase = np.random.randint(60,100,size = 50) + np.random.random()

print(np.corrcoef(visine,mase)[0,1])

plt.bar(visine,mase)
plt.show()

asdasdsad = input()