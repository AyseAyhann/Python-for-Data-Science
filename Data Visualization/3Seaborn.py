##########################################
# SEABORN
##########################################
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
df=sns.load_dataset("tips")
print(df.head())

# categorical
# df["sex"].value_counts().plot(kind="bar")
# plt.show()
print(df["sex"].value_counts())
sns.countplot(x=df["sex"],data=df)
plt.show()

# numerical
sns.boxplot(x=df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()