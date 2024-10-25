import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)

df = sns.load_dataset("titanic")
print(df.head())

####################
# plot
####################

x=np.array([1,8])
y=np.array([0,150])
plt.plot(x,y)
plt.show()
plt.plot(x,y,'o')
plt.show()

x=np.array([2,4,6,8,10])
y=np.array([1,3,5,7,9])
plt.plot(x,y)
plt.show()

plt.plot(x,y,'o')
plt.show()

####################
# marker
####################

y=np.array([13,28,11,100])
plt.plot(y,marker='o')
plt.show()
plt.plot(y,marker='*')
plt.show()
plt.plot(y,marker='x')
plt.show()


####################
# line
####################

y=np.array([13,28,11,100])
plt.plot(y,linestyle="dashed")
plt.show()
plt.plot(y,linestyle="dotted")
plt.show()
plt.plot(y,linestyle="dashdot",color="r")
plt.show()


####################
# Multiple lines
####################
x=np.array([13,18,31,10])
y=np.array([13,28,11,100])
plt.plot(x)
plt.plot(y)
plt.show()

####################
# Labels
####################

x=np.array([80,85,90,95,100,105,110])
y=np.array([240,250,260,270,280,290,300])
plt.plot(x,y)

# Title
plt.title("This is the main title")

# label x
plt.xlabel("x")

# label y
plt.ylabel("y")

plt.grid()
plt.plot(x, y, color="b")
plt.show()

####################
# Subplots
####################
x=np.array([80,85,90,95,100,105,110])
y=np.array([240,250,260,270,280,290,300])
plt.subplot(1,3,1) # 1 row 2 column
plt.title("1")
plt.plot(x,y)
plt.show()

# plot-2
x=np.array([8,8.5,9,9.5,10,10.5,11])
y=np.array([240,250,260,270,280,290,300])
plt.subplot(1,3,2) # 1 row 2 column
plt.title("2")
plt.plot(x,y)
plt.show()

# plot-3
x=np.array([80,85,90,95,100,105,110])
y=np.array([240,250,260,270,280,290,300])
plt.subplot(1,3,3) # 1 row 2 column
plt.title("3")
plt.plot(x,y)
plt.show()

