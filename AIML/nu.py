import numpy as np
# a= np.array([1,2,3,4,5]) 
# # print(type(a))
# print(a)

# A= np.array([[1],
#             [2],
#             [3],[4]])

# print(A.shape)
# print(a.shape)
# print(np.zeros((3,3))) null matrix
# print(np.ones((3,3)))  unit matrix or scalar matrix
# print(np.eye((3,3))) identity matrix
# print(np.full((3,3),9))
# print(np.eye((6)))
# print(np.random.random((3,5))) value lies between 0 and 1

# rn= np.random.random((3,5))
# print(rn)
# print(rn[:1])
# print(rn[:1:4]) row 1 col 4
# print(rn[:3,:4])
# print(rn[1:3,1:3])

# x=np.array([[1,2],[4,5]])
# y=np.array([[3,4],[5,6]])

# print((x.shape ,y.shape))
# print((x+y),(x-y),(x*y),(x/y))

# print(np.add(x,y))
# print(np.subtract(x,y))
# print(np.multiply(x,y))
# print(np.divide(x,y))

# print(np.matpul(x,y))
# print(x.dot(y))

a=np.array([[1,2,3,4,5]])
b=np.array([[1,2,3,4,5]])


# print((np.sum(a)))

print((np.sum( a , axis = 0)))

# print((np.sum( a , axis = 1))) Vectors
# print((x+y),(x-y),(x*y),(x/y))


                                                      # STACKING
# A = np.stack((a,b), axis=0)
# print(A)

B = np.stack((a,b), axis=1)
print(B)

print((B.T))

# only matrix[2 3 0 1 4] have shapes, vectors(i,j,k) dont have any shape
# continuity can be loose in Transpose, but RESHAPE maintains continuity.

