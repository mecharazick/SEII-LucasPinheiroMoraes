import numpy as np

# np.loadtxt, np.genfromtxt
data = np.loadtxt('spambase.csv', delimiter=",",dtype=np.float64)
data = np.genfromtxt('spambase.csv', delimiter=",",dtype=np.float64)
print(data)
print(data.shape)