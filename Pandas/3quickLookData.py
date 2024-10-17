# pandas + seaborn quick look at data

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.columns)
print(df.index)
print(df.describe().T)
# print(df.describe())
# df.isnull().values.any() #ask for any null value
print(df.isnull().values.any())
print(df.isnull().sum())
print(df["sex"].head())
print(df["sex"].value_counts())