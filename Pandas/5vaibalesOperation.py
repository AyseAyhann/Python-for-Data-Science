import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df=sns.load_dataset("titanic")
df.head()

"age" in df
df["age"].head()
df.age.head()
print(type(df["age"].head()))
print(type(df[["age"]].head()))
print(df[["age","alive"]])

col_names=["age","adult_male","alive"]
print(df[col_names])


df["age2"]=df["age"]**2
print(df.columns)
# col_names.append("age2")
# print(df[col_names])

# df.drop("age2",axis=1,inplace=True)
# print(df.columns)

# df.drop(col_names, axis=1,inplace=True)
# print(df.columns)

###
# delete obtain value from each column
# loc used for selection in dataframe
###
print(df.loc[:,df.columns.str.contains("age")].head()) # select related with "age"
print(df.loc[:,~df.columns.str.contains("age")].head())  # select except "age"




