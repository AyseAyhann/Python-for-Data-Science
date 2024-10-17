# Apply & Lambda
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width',500)
df=sns.load_dataset('titanic')
print(df.head())


df["age2"]=df["age"]*2

df["age"]=df["age"]/10
print((df["age2"]/10).head())

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())


for col in df.columns:
    if "age" in col:
        df[col]=df[col]/10

print(df.head())


# apply & lambda

print(df[["age","age2"]].apply(lambda x:x/2).head())
print(df.loc[:,df.columns.str.contains("age")].apply(lambda x: x/10).head())

#standardization
print(df.loc[:,df.columns.str.contains("age")].apply(lambda x: (x-x.mean())/x.std()).head())

def standart_scaler(col_name):
    return (col_name-col_name.mean()) /col_name.std()

print(df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head())

#df.loc[:,["age","age2"]]=df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head()
df.loc[:,df.columns.str.contains("age")]=df.loc[:,df.columns.str.contains("age")].apply(standart_scaler).head()
print(df.head())