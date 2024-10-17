# selection in Pandas
import seaborn as sns
df=sns.load_dataset("titanic")

print(df.head())

print(df.index)
print(df[0:13])
print(df.drop(0,axis=0).head()) #deletes 0.index' value

delete_indexes=[0,1,2,3]
print(df.drop(delete_indexes,axis=0).head()) #starts from 4

#permanent operation
#1 # df=df.drop(delete_indexes,axis=0)
#2 # df.drop(delete_indexes, axis=0,inplace=True)

###
# convert varibale to index
###
df["age"].head()
df.age.head()

df.index=df["age"]
df.drop("age",axis=1).head()
df.drop("age",axis=1,inplace=True)
print(df.head())

###
# convert index to variable
###

#1
df.index
df["age"]=df.index
print(df.head())
df.drop("age",axis=1,inplace=True)

#2
df=df.reset_index()
print(df.head())
