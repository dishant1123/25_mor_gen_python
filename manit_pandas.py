import pandas as pd 
import numpy as np

df =pd.read_csv("mckinsey.csv")
# print(df)

# print(df["country"])
# print(df["year"])

# print(df.head(20))
# print(df.tail(20))

# print(df.info())

# print(df[["country","population"]].head(20))

# print(df.shape)

# manually create a dataframe 

a=pd.DataFrame([
    ['a',23,70000],
    ['b',13,7000],
    ['c',43,700000],
    ['d',53,7000000],
    ['e',73,70000789]
    ],columns=['name','age','salary']
)
# print(a)

b=pd.DataFrame({
    "name":["devang","maint","nirmit","ketali"], 
    "age" :[20,19,19,21],
    "salary" :[90000,89000,95000,79000]  
})
# print(b)
# print(b.columns)
# print(b.keys())
# print(b.values)

# column name change  : 
"""b=b.rename(columns={
    "name" :"Name",
    "age" :"Age"
})
"""
# print(b)
# rename  column name  :
b.rename(
           {"name" :"First_name",
            "age" :"Age"
            },axis =1,inplace=True)

# print(b)

# add column in data frame : 
b["Gender"] =["M","M","M","F"]
# print(b)

# drop  : delete column 

# print(b.drop("Age",axis =1))
# print(b.drop(["Age","Gender"],axis =1))
# print(b.drop(columns=["Age","Gender"]))


# task  :1 year +3  
# unique : remove  duplicate  

"""
print(df["country"].unique())
print(df["country"].nunique())
print(df["country"].value_counts())
"""

"""df["GDP"] =df["population"]*df["gdp_cap"]
print(df)
"""

"""df["New_index"]=np.arange(5,1709)
print(df)
"""
"""df.index = np.arange(5,1709)
print(df)

"""

# implict , explict : 
"""
implicit ==> always start with 0.  ==>iloc 
explict ==> we can define it as we want (what is seen in output dataframe) it can be float, string whatever we want.  ==> loc 
"""

# print(df.head(20))
# print(df["country"][16])
# print(df.index[16])

"""df.index=np.arange(1,1705)
print(df)

temp =df.head(5)

temp.index =["a","b","c","d","e"]
print(temp)
"""

cont =df["country"]
# print(cont)

# print(cont.head(20))
# print(cont[13])
# print(cont[5:13])

# loc :explicit 
# iloc :implicit 

# print(cont.loc[13])
# print(cont.iloc[13])

# print(cont.loc[1])
# print(cont.iloc[1])

# slicing :

# print(cont.loc[1 :5])  #loc included both start and end. 
# print(cont.iloc[1 :5])  #iloc excluded lat value. 

# print(df.loc[2:5,"year":"continent"])
# print(df.iloc[2:5,0:4])

# print(df.loc[2:5,["country","year","gdp_cap"]])

# print(df.iloc[[1,4,6,7],[0,3,4]])

print(df.iloc[1:10:2])