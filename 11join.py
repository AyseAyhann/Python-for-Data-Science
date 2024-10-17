# Join: merge, concat

import numpy as np
import pandas as pd
m=np.random.randint(1,30,size=(5,3))
df1=pd.DataFrame(m, columns=["var1","var2","var3"])
df2=df1+99

# concat
print(pd.concat([df1,df2], ignore_index=True))

# merge
df1=pd.DataFrame({"employees":["john","dennis","mark","maria"],
                  "group":["accounting","engineering","engineering","hr"]})

df2=pd.DataFrame({"employees":["mark","john","dennis","maria"],
                  "start_date":[2010,2009,2014,2019]})


#df3=pd.merge(df1,df2)
#print(df3)

df3=pd.merge(df1,df2,on="employees")

# manager of each employee

df4=pd.DataFrame({"group":["accounting","engineering","hr"],
                  "manager":["Eva","Maria","Feyza"]})

df5=pd.merge(df3,df4)
print(df5)
df5=pd.merge(df3,df4,on="group")