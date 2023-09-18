import numpy as np

a = np.arange(1,7)
print(a)
print(a.shape)

b = a.reshape((2,3)) # returns an error if shape cannot be used
print(b)
print(b.shape)

b = a.reshape((3,2)) # returns an error if shape cannot be used
print(b)
print(b.shape)

b = a[np.newaxis, :]
print(b)

b = a[:, np.newaxis]
print(b)