import seaborn as sns
import pandas as pd

# 17
df=sns.load_dataset("tips")
print(df.head())

# 18
new_aggr=df.groupby("time", observed="True").agg({"total_bill":["sum","min","max","mean"]})
print(new_aggr)

# 19
new_aggr2=df.groupby(["day", "time"], observed="True").agg({"total_bill": ["sum", "min", "max", "mean"]})
print(new_aggr2)

#20
filtered_df=df[(df["sex"]=="female")&(df["time"]=="Lunch")]
if not filtered_df.empty:
    new_aggr3=filtered_df.groupby("day").agg({"total_bill": ["sum","min","max","mean"]})

    print(new_aggr3)

# 21  size<3 total_bill>10 mean
mean_loc=df.loc[(df["size"]<3)& (df["total_bill"]>10),"total_bill"].mean()
print(mean_loc)

# 22
df["total_bill_tip_sum"]=df["total_bill"]+df["tip"]
print(df.head())

# 23
df.sort_values(by="total_bill_tip_sum",inplace=True)
print(df.head())
new_df=df.head(30)
print(new_df.head())