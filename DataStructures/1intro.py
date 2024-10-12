#conda is used for virtual environment and package managing
#pip is used for package managing

import numpy as np
import pandas as pd

#Python Collections

#list
x=["btc","eth","xrp"]
print(type(x))

#dictionary
y={"name":"Peter","age":21}
print(type(y))

#tuple
z=("python","ml","dl")
print(type(z))

#set
w={"python","ml","dl"}
print(type(w))


long_str="studying Data structure is really joyful"
print("data" in long_str)
print("Data" in long_str)

#reaching all string methods
print(dir(str))
print(type(len))

print("ayse".upper())
print("AYSE".lower())

hi="Hello AI Era"
#hi=hi.replace('l','b')
print(hi.replace('l','b'))

print(hi.split())

no=" 538 784 "
print(no.strip())
print(no.strip("8"))