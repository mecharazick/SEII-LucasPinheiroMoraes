import numpy as np

a = np.random.random((3,2)) # random between 0-1
print(a)

a = np.random.randn(3,2) # normal/Gaussian distribution
print(a)

a = np.random.randn(1000) # normal/Gaussian distribution
print(a.mean(), a.var())

a = np.random.randint(3,10, size =(3,3))
print(a)

a = np.random.randint(10, size =(3,3)) # 0 as start value
print(a)

a = np.random.choice(5, size = 10)
print(a)

a = np.random.choice([-8,-7,-6], size = 10)
print(a)