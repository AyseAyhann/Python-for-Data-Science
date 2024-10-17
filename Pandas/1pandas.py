#Pandas Series
import pandas as pd

s=pd.Series([10,77,12,4,5])
print(type(s))
print(s.index)
print(s.dtype)
print(s.size)
print(s.ndim)
print(s.values) # numpy array
print(type(s.values)) #numpy array
print(s.head(3))
print(s.tail(3))
