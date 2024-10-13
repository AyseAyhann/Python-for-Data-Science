# Conditions on numpy
import numpy as np
array=np.array([1,2,3,4,5])

# loop
new_array=[]
for a in array:
    if a<3:
        new_array.append(a)

print(new_array)

# numpy
print(array<3)
#array[array<3]
na=array[array<3]
print(na)

array[array>3]
array[array!=3]
array[array==3]
array[array>=3]



