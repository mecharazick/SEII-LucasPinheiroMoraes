import numpy as np

a = np.array([[1,2],[3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

# print(eigenvalues)
# print(eigenvectors) #column vector

# e_vec = e_val = A * e_vec
b = eigenvectors[:,0] * eigenvalues[0]
print(b)

# b = eigenvectors[:,0] @ a
# print(b)

c = a @ eigenvectors[:,0]
print(b)
print(b==c)

print(np.allclose(b,c))

A = np.array([[1,1],[1.5,4.0]])
b = np.array([2200,5050])
x = np.linalg.inv(A).dot(b)
print(x)

x = np.linalg.solve(A,b)
print(x)