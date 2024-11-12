##########################################
# 2.2. Analysis of Categorical Variables
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

print(df["embarked"].value_counts())
print(df["sex"].unique())
print(df["class"].nunique())

# cat_cols=[col for col in df.columns if ((df[col].dtype=="object") | (df[col].dtype=="category") | (df[col].dtype=="bool") )]
# print(cat_cols)
cat_cols=[col for col in df.columns if str(df[col].dtypes) in ["object","category","bool"]]
print(cat_cols)

df["sex"].dtypes
str(df["sex"].dtypes)
print(str(df["sex"].dtypes) in ["object"])

num_but_cat=[col for col in df.columns if ((df[col].nunique()<10)& (str(df[col].dtypes) in ["int64","float64"])) ]
print(num_but_cat)

cat_but_car=[col for col in df.columns if (str(df[col].dtypes) in ["object","category"]) and (df[col].nunique()>20)]
print(cat_but_car)

cat_cols=cat_cols+ num_but_cat
print(cat_cols)

cat_cols=[col for col in cat_cols if col not in cat_but_car]
print(cat_cols)

print(df[cat_cols].nunique())

print([col for col in df.columns if col not in cat_cols])


def cat_summary(dataframe, col_name, plot=False):
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * df[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name],data=dataframe)
            plt.show(block=True)


"""
cat_summary(df, "sex", plot=True)
for col in cat_cols:
   if df[col].dtype == "bool":
       print("xxxxxxxxxxxxxx")
   else:
     cat_summary(df,col,plot=True)
"""

# df["adult_male"]=df["adult_male"].astype(int)

cat_summary(df, "sex", plot=True)
for col in cat_cols:
   if df[col].dtype == "bool":
     df[col]= df[col].astype(int)
     cat_summary(df, col, plot=True)
   else:
     cat_summary(df,col,plot=True)

# bu değişken (adult_male) en başında bool'dan integer'a çevirilebilir ya da bu şekilde döngü ile yapılabilir


