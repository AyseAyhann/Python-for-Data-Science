##########################################
# Data Visualization: Matplotlib & Seaborn
##########################################
# MATPLOTLIB
##########################################
# Kategorik: sütun grafik- countplot bar
# Numerik: histogram, boxplot

# example for categorical variable visualization

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)
df = sns.load_dataset("titanic")
print(df.head())

df["sex"].value_counts().plot(kind="bar")
plt.show()

# example for numerical variable visualization
plt.hist(df["age"])
plt.show()

# example for categorical variable visualization
plt.boxplot(df["fare"])
plt.show()

