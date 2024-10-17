# count() first() last() mean() median() min() max() std() var() sum() -pivot table
# groupby()
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df=sns.load_dataset('titanic')
print(df.head())


print(df["age"].mean())
print(df.groupby("sex")['age'].mean())
df.groupby("sex").agg({"age":["mean","sum"]})
print(df.groupby("sex").agg({"age":["mean","sum"]}))
print(df.groupby("sex").agg({"age":["mean","sum"],
                             "survived":"mean"}))

print(df.groupby(["sex","embark_town"]).agg({"age":["mean","sum"],
                                       "survived":"mean"}))



print(df.groupby(["sex","embark_town","class"],observed=False).agg({
    "age": "mean",
    "survived":"mean",
    "sex":"count",
}))

