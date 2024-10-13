#IMPORTANT
import numpy as np
a=np.random.randint(10, size=10)
print(a)
a[0]
a[0:5] #slicing
a[0]=91
print(a)

m=np.random.randint(10, size=(3,5))
print(m)
print(m[0][0])
print(m[0,1])  #row,column
m[2,3]=999
print(m)

m[2,3]=9.99  #numpy is fixtype array, converts integer
print(m)

m[:,0] #all rows 0. column
print(m[:,1])
print(m[1,:])
print(m[0:2,0:3])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])
