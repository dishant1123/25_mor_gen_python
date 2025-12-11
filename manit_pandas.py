import pandas as pd 

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
print(b.drop(columns=["Age","Gender"]))