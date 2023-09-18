import numpy as np

a = np.array([[1,2],[3,4]])
print(a)
print(a.shape)

print(a[0]) #accesses the first row of the multidim array

# To print a specific value, all the coordinates to the position must
# be informed as in a[0][0] or as below
print(a[0,0])

# The syntax below returns the elements of all rows and the first(0) column
print(a[:,0])
# Similarly, the syntax below returns all the elements of the first(0) row
print(a[0,:])

print(a.T) #Transposes the array

print(np.linalg.inv(a)) # Returns the inverse of the matrix

print(np.diag(a)) # Returns the diagonal matrix to a
