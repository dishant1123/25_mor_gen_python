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


"""print(df["country"].unique())
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

# cont =df["country"]
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

# print(df.iloc[1:10:2]) 

#=================
"""
sorting data frame
"""

"""
a =df.sort_values(by="year",ascending=False)
print(a)

b= df.sort_values(by="gdp_cap",ascending=True).head(20)
print(b)

c=df.sort_values(by=["year","life_exp"]).head(50)
print(c)

d=df.sort_values(by=["year","life_exp"],ascending=False).head(50)
print(d)

e=df.sort_values(by=["year","life_exp"],ascending=[True,False])
print(e)
"""

"""
join :
"""
"""
users =pd.DataFrame({
    "user_id":[1,2,3],
    "name":["devang","nirmit","ketali"]
})
print(users)

msgs =pd.DataFrame({
  "user_id":[1,1,2,4],
  "msgs":['hmm','achha','ok','yup'] 
    
})

print(msgs)"""

# result=pd.concat([users,msgs])
# result=pd.concat([users,msgs],axis=1)

# result=pd.merge(msgs,users,on="user_id")
# result=pd.merge(msgs,users,left_on="user_id",right_on="user_id",how="left")
# result=pd.merge(msgs,users,left_on="user_id",right_on="user_id",how="right")
# result=pd.merge(msgs,users,left_on="user_id",right_on="user_id",how="outer")


# print(result) 

#============================
"""
df["GDP"] =df["population"]*df["gdp_cap"]
print(df)
"""
# new  index set : 

"""df["new_index"]=np.arange(5,1709)
print(df)
"""
"""df.index = np.arange(5,1709)
print(df)

print(df.index.values)
print(df.value_counts())
"""

# implicit : start from  0
# explict :we can define it as we want 

# print(df.head(20))
# print(df["country"][11])
# print(df.index[16])

"""df.index =np.arange(1,1705,dtype=float)
print(df)

temp =df.head()
temp.index=["a","b","c","d","e"]
print(temp)
"""

"""cont =df["country"]
print(cont.head(20))

print(cont[13])
print(cont[5 :13])
"""

# print(df.loc[13])
# print(df.iloc[13])

# print(df.loc[2 :13,"country":"continent"])
# print(df.iloc[2 :13,1:3])  # last  number excluded it 

# movies =pd.read_csv("movies.csv")
# movies.drop(columns="Unnamed: 0",inplace=True)
# print(movies)

# directors =pd.read_csv("directors.csv")
# directors.drop(columns="Unnamed: 0",inplace=True)
# print(directors)

#Get me the number of directors who did not produce any movie ever.
# print(movies["director_id"].nunique())
# print(directors["id"].nunique())
# print("directors who did not produce any movie ever:",directors["id"].nunique()-movies["director_id"].nunique())


"""
Get the output similar to the following SQL query:
select * from movies where vote_average > 7
"""

# que : 
"""
Find out Active_years of each director (Active_years is for how long a particular director has been directing movies. 
"""

# df =pd.read_csv("directors.csv")
# df.drop(columns="Unnamed: 0",inplace=True)
# print(df)

# director_wise =df.groupby("director_name") 
# print(director_wise)

# print(director_wise.groups)
# print(director_wise.ngroups)

# print(director_wise.get_group("James Cameron"))

movies =pd.read_csv("movies.csv")
directors =pd.read_csv("directors.csv")

movies.drop(columns="Unnamed: 0",inplace=True)
directors.drop(columns="Unnamed: 0",inplace=True)
# print(movies)

directors_wise = pd.merge(movies,directors,left_on='director_id',right_on='id')
# print(joint)

# directors_wise =directors.groupby("director_name")

# print(directors_wise.groups)
# directors_wise.get_group("James Cameron")
# print(directors_wise)
"""
active_years = (
    directors_wise
    .groupby("director_name")["year"]
    .agg(min_year="min", max_year="max")
)

active_years["active_years"] = (
    active_years["max_year"] - active_years["min_year"]
)

print(active_years)
"""
# Get me the names & 'Active Years' of the directors who have been active in the industry for at least 30 years

