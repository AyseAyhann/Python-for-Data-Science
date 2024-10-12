#IMPORTANT
import seaborn as sns
df= sns.load_dataset("car_crashes")
print(df.columns)

num_cols=[col for col in df.columns if df[col].dtype !="O"]
print(num_cols)

dict={}
agg_list=["mean","min","max","sum"]

for col in num_cols:
    dict[col]=agg_list

print(dict)

new_dict={col:agg_list for col in num_cols}
df[num_cols].head()
aggdf=df[num_cols].agg(new_dict)
print(aggdf)