# iloc & loc: integer based selection & label based selection

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df=sns.load_dataset("titanic")
df.head()


# iloc
print(df.iloc[0:3])  # 0 1 2. index, except 3
print(df.iloc[0,0])

print(df.loc[0:3])   # 0 1 2 3. index, include 3

df.iloc[0:3, 0:3]
df.loc[0:3,"age"] #label based

col_names=["age","embarked","alive"]
print(df.loc[0:3,col_names])
