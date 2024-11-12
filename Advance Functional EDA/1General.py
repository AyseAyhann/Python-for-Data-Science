##########################################
# ADVANCED FUNCTIONAL EDA
##########################################
"""
1. General
2. Analysis of Categorical Variables
3. Analysis of Numerical Variables
4. Analysis of Target Variables
5. Analysis of Correlation
"""
##########################################
# 1. General
##########################################
import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)
df=sns.load_dataset('titanic')

print(df.head())

df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

def check_df(dataframe, head=5):
    print("########## SHAPE ##########")
    print(dataframe.shape)
    print("########## DATA TYPES ##########")
    print(dataframe.dtypes)
    print("########## INFO ##########")
    print(dataframe.info())
    print("########## ISNULL ##########")
    print(dataframe.isnull().sum())
    print("########## HEAD ##########")
    print(dataframe.head())
    print("########## TAIL ##########")
    print(dataframe.tail())
    print("########## QUANTILES ##########")
    print(dataframe.describe([0,0.05,0.50,0.95,0.99,1]).T)

check_df(df)

df=sns.load_dataset('iris')
check_df(df)

df=sns.load_dataset('penguins')
check_df(df)
