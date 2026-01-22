import pandas as pd

"""
df=pd.read_csv("mckinsey.csv")
# print(df)

year= df["country"]
# print(year)

year_country =df[["country","population"]]
# print(year_country)

year_country =df[["country","population"]].head(20)
# print(year_country)

year_country =df[["country","population"]].tail(20)
print(year_country)

"""

# create manually dataframe : 

"""
a=pd.DataFrame([
    [1,"manit",20,70000],
    [2,"dipak",31,71000],
    [3,"deep",24,72000],
    [4,"mahesh",34,73000],
    [5,"suresh",45,75000]
],columns=['id','name','age','salary']) 

# print(a)
# print(a.head(2))
# print(a.tail(2))
result =a[["name","salary"]]
print(result)
"""

df=pd.read_csv("mckinsey.csv")
print(df.info())
