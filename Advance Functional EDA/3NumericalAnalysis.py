##########################################
# 3. Analysis of Numerical Variables
##########################################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)
df=sns.load_dataset('titanic')

print(df.head())
print(df.dtypes)

print(df[["age","fare"]].describe().T)

cat_cols=[col for col in df.columns if str(df[col].dtypes) in ["object","category","bool"]]
print(cat_cols)

num_but_cat=[col for col in df.columns if ((df[col].nunique()<10)& (str(df[col].dtypes) in ["int64","float64"])) ]
print(num_but_cat)


cat_cols=cat_cols+ num_but_cat

# numeric columns
# num_cols=[col for col in df.columns if (df[col].dtypes in ["int64","float64"]) and (df[col].nunique()>10)]
# print(num_cols)
num_cols=[col for col in df.columns if col not in cat_cols]
print(num_cols)

def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60]
    print(dataframe[numerical_col].describe(quantiles).T)


num_summary(df,"age")

for col in num_cols:
    num_summary(df,col)

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)



num_summary(df,"age",plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)