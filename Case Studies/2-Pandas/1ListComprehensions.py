import seaborn as sns
import pandas as pd
df=sns.load_dataset("car_crashes")
print(df.columns)

"""
cols=[]
for col in df.columns:
    cols.append(col.upper())
    if pd.api.types.is_numeric_dtype(df[col]):
        cols.append("NUM_"+col.upper())

print(cols)
"""

#1
columns=["NUM_"+col.upper() if pd.api.types.is_numeric_dtype(df[col]) else col.upper() for col in df.columns]
print("1: ")
print(columns)


#2
flag_list=[col.upper()+"_FLAG" if "no" not in col else col.upper() for col in df.columns]
print("2: ")
print(flag_list)


#3
exclude_cols=["total","speeding","alcohol","not_distracted","ins_premium","ins_losses"]
new_cols=[col for col in df.columns if col not in exclude_cols]
new_df=df[new_cols]
print("3: ")
print(new_df.columns)
