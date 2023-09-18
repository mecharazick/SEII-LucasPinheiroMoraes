import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)

b = a[0,1:3]
print(b) # row slicing

b = a[:, 0]
print(b) # column slicing

b = a[-1,-1]
print(b) # Backwards indexing

a = np.array([[1,2],[3,4],[5,6]])
print(a)

bool_indx = a > 2
print(bool_indx)
print(a[bool_indx])
print(a[a > 2]) # Boolean indexing

b = np.where(a > 2, a, -1)
print(b)

a = np.array([10,19,30,41,50,61])
print(a)

b = [1,3,5] 
print(a[b]) # Fancy indexing

even = np.argwhere(a % 2 == 0).flatten()
print(a[even])