# WHY NUMPY? :
# 1- fast, holds fixtype data
# 2- provides Functional level/High level usage

import numpy as np

a=[1,2,3,4,5,6,7,8,9]
b=[1,2,3,4,5,6,7,8,9]
ab=[]

for i in range(0, len(a)):
    ab.append(a[i]*b[i])

print(ab)


#numpy array
#constant type variable
a=np.array([1,2,3,4,5,6,7,8,9])
b=np.array([1,2,3,4,5,6,7,8,9])
print(a*b)
