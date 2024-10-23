# 1
import pandas as pd
import seaborn as sns
df=sns.load_dataset("titanic")
cols=df.select_dtypes(include=['object'])

print(df.head)

# 2
print(df[df["sex"]=="female"]["sex"].count())
print(df[df["sex"]=="male"]["sex"].count())

# 3
for col in cols:
    print(df[col].nunique())
# 4
print("pclass unique: ")
print(df["pclass"].nunique())

# 5
print(df["pclass"].unique() & df["parch"].nunique())

# 6
print((df["embarked"].dtype))
df["embarked"]=df["embarked"].astype("category")
print((df["embarked"].dtype))

# 7
c_embark=df.loc[df["embarked"]=="C"]
print(c_embark.head())

# 8
embark_nots=df.loc[df["embarked"]!="S"]
print(embark_nots)

# 9
young_female=df.loc[(df["sex"]=="female")& (df["age"]<30)]
print(young_female)

# 10
print(df.dtypes)
print(df.loc[df["fare"]>500])
print(df.loc[df["age"]>70])
new_list=df.loc[(df["fare"].notna()) & (df["age"].notna()) & (df["fare"]>500) & (df["age"]>70)] # there is no one fare>500 and age>70
print(new_list)


# 11
for col in df.columns:
    print(f"Empty in {col}:{df[col].isnull().sum()}")

# 12
df.drop("who",axis=1,inplace=True)
print(df.columns)


# 13
meanNum=df["deck"].mode()[0]
if df["deck"].isnull().any():
    # df=df.assign(deck=df["deck"].fillna(meanNum))
    df["deck"]=df["deck"].fillna(meanNum)
print(df["deck"].head())


# 14
medianNum=df["age"].median()
if df["age"].isnull().any():
    df["age"]=df["age"].fillna(medianNum)
print(df["age"].head())

# 15
# survived for pclass, sex -  sum, count, mean
# aggregation
new_agg=df.groupby("pclass").agg({"survived":["sum","count","mean"]})
new_agg2=df.groupby("sex").agg({"survived":["sum","count","mean"]})
print(new_agg)
print(new_agg2)

new_agg3=df.groupby(["pclass","sex"]).agg({"survived":["sum","count","mean"]})
print(new_agg3)

# 16 apply lambda
# age<30 =1     age>30 =0 age_flag
df["age_flag"]=df["age"].apply(lambda x:1 if x<30 else 0)
print(df["age_flag"].head())
print(df.head())



