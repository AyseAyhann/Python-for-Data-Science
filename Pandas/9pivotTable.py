# pivot table
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df=sns.load_dataset('titanic')
print(df.head())

ptable=df.pivot_table("survived","sex","embarked")
print(ptable)
ptable=df.pivot_table("survived","sex","embarked",aggfunc="std")
print(ptable)

ptable=df.pivot_table("survived","sex",["embarked","class"],observed=False)
print(ptable)
df["new_age"]=pd.cut(df["age"],bins=[0,10,18,25,40,90])  #numerical to categorical  or use qcut

print(df.pivot_table("survived","sex",["new_age","class"],observed=False))
pd.set_option('display.width', 500)