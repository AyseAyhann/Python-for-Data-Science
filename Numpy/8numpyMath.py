import numpy as np
v=np.array([1,2,3,4,5])

print(v/5)
print(v**2)
print(v-1.2)
print(v*3/2)


print(np.subtract(v,1))
# v=np.subtract(v,1) new v array
np.add(v,1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
print(np.var(v))

arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[12,13,14,15,16]])
print("1.dimension 2.element:", arr[0,1])

###
# 5*x0 + x1=12
# x0 + 3*x1=10

a=np.array([[5,1],[1,3]])
b=np.array([12,10])

results=np.linalg.solve(a,b)
print(results)

