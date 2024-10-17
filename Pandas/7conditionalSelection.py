import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns',None)
df=sns.load_dataset("titanic")
df.head()


df[df["age"]>50].head()
print(df[df["age"]>50]["age"].count())

#print(df[df["age"]>50]["class"])


#females under 25 years and their age-sex-class
#USE loc
young_female=df.loc[(df["age"]<25) & (df["sex"]=="female"),["age","sex","class"]].head()
print(young_female)



#males over 50 and their age-sex-class
old_male=df.loc[(df["age"]>50) & (df["sex"]=="male"),["age","sex","class"]].head()
print(old_male)

# and embark_town= Cherbourg
new_old_male=df.loc[(df["age"]>50)&(df["sex"]=="male")&(df["embark_town"]=="Cherbourg"), ["age","sex","embark_town","class"]].head()
print(new_old_male)

# and embark_town= Cherbourg or Southampton
new_old_male2=df.loc[(df["age"]>50)
                     &(df["sex"]=="male")
                     &((df["embark_town"]=="Cherbourg") | (df["embark_town"]=="Southampton")),
                     ["age","sex","embark_town","class"]].head()
print(new_old_male2)

print(df["embark_town"].value_counts())