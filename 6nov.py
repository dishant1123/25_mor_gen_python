# year  : 1952 +3  ==> next survey _yr 1955   

import  pandas as pd 
import numpy as np 
df = pd.read_csv("mckinsey.csv")
"""
print(df)

df["next_survey_year"] =df["year"] +3
print(df)
"""
# unique,nunique , value_counts : 

"""a=df["country"].unique()  # unique  values not  repeating value 
print(a)

b=df["country"].nunique()  # count  of unique  values 
print(b)

c=df["country"].value_counts()
print(c)

"""

"""d=df[["country","gdp_cap"]]
print(d)

df["GDP"] = df["population"] * df["gdp_cap"]
print(df)
"""

# print(df)
"""
df["new_index"]=np.arange(5,1709)
print(df)

print(df.index)
print(df.index.values)

df.index=np.arange(5,1709)
print(df)
"""