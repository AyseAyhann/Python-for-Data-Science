# changing variable's name in a data set
#list1=['total','speeding','alcohol','not_distracted','no_previous','ins_premium','ins_losses','abbrev']
#new_list=[]
'''
for name in list1:
    new_list.append(name.upper())
print(new_list)

[new_list.append(name.upper()) for name in list1]
print(new_list)
'''

#print([name.upper() for name in list1])

import seaborn as sns
df=sns.load_dataset("car_crashes")
print(df.columns)

cols=[]
#for col in df.columns:
    #print(col.upper())
    #cols.append(col.upper())

columns=[col.upper() for col in df.columns]
print(columns)



#if name includes "INS" add FLAG else add NO_FLAG
flag_columns=[]
for c in columns:
    if "INS" in c:
        flag_columns.append("FLAG_"+c)
    else:
        flag_columns.append("NO_FLAG_"+c)

print(flag_columns)

flag_cols=[]
[flag_cols.append("FLAG_"+c) if "INS" in c else flag_cols.append("NO_FLAG_"+c) for c in columns]
print(flag_cols)

print(["FLAG_"+c if "INS" in c else "NO_FLAG_"+c for c in columns])



