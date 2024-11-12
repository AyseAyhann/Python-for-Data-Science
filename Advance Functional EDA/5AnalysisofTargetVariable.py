##################################
# 4. Analysis of Target Variables
##################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)
df = sns.load_dataset('titanic')
print(df.head())
print(df.info())


# docstring
def grab_col_names(dataframe, cat_th=10, car_th=20):
  """
  Returns categorical, numeric, and cardinal variables in the data frame

  Parameters
  ----------
  dataframe: dataframe
     is the dataframe from which variable names are to be taken.
  cat_th: int, float
     Class threshold value for numeric and categorical variables
  car_th: int, float
     Class threshold value for categorical and cardinal variables

  Returns
  -------
  cat_cols: list
     categorical variables list
  num_cols: list
     numeric variables list
  cat_but_car: list
     List of cardinal variables in categorical view

  Notes
  -------
  cat_cols + num_cols + cat_but_car= total number of variables
  cat_cols includes num_but_cat
  The sum of 3 returned lists is equal to the total number of variables: cat_cols + num_cols + cat_but_car

  """
  cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["object", "category", "bool"]]
  num_but_cat = [col for col in df.columns if
                 ((df[col].nunique() < 10) & (str(df[col].dtypes) in ["int64", "float64"]))]
  cat_but_car = [col for col in df.columns if
                 (str(df[col].dtypes) in ["object", "category"]) and (df[col].nunique() > 20)]

  cat_cols= cat_cols+ num_but_cat
  cat_cols=[col for col in cat_cols if col not in cat_but_car]

  num_cols=[col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
  num_cols=[col for col in num_cols if col not in cat_cols]

  print(f"Observations: {dataframe.shape[0]}")
  print(f"Variables: {dataframe.shape[1]}")
  print(f"cat_cols: {len(cat_cols)}")
  print(f"num_cols: {len(num_cols)}")
  print(f"cat_but_car: {len(cat_but_car)}")
  print(f"num_but_cat: {len(num_but_cat)}")

  return cat_cols, num_cols, cat_but_car

# help(grab_col_names)
grab_col_names(df)
cat_cols, num_cols, cat_but_car = grab_col_names(df)


# bonus
df=sns.load_dataset("titanic")
df.info()
for col in df.columns:
    if df[col].dtypes == "bool":
        df[col]=df[col].astype(int)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * df[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in cat_cols:
    cat_summary(df,col, plot=True)

for col in num_cols:
    num_summary(df,col, plot= True)


print(df.head())

df["survived"].value_counts()
#cat_summary(df,"survived")


print(df.groupby("sex")["survived"].mean())

cat_cols, num_cols, cat_but_car = grab_col_names(df)
df = sns.load_dataset('titanic')

# Analysis of target variables with categorical variables
def target_summary_with_cat(dataframe,target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}))

target_summary_with_cat(df,"survived", "sex")

for col in cat_cols:
    target_summary_with_cat(df,"survived",col)


# Analysis of target variables with numerical variables
print(df.groupby("survived")["age"].mean())
df.groupby("survived").agg({"age": "mean"})

def target_summary_with_num(dataframe, target, numerical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(numerical_col)[target].mean()}))

for col in num_cols:
    target_summary_with_num(df,"survived",col)