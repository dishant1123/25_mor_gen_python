import pandas as pd 

df = pd.read_csv('mckinsey.csv')
# print(df)

"""
print(df.sort_values(by="life_exp").head(20))  # asc to desc 
print(df.sort_values(by="life_exp",ascending=False).head(20))  # desc to asc 
"""

# multi row sort  : 

"""
print(df.sort_values(by=["life_exp","year"],ascending=[False,True]).head(20))
print(df.sort_values(by=["life_exp","year"],ascending=False).head(20))
"""

# joins :
users =pd.DataFrame({"userid":[1,2,3],"name":["satyam","jainish","devang"]})
msgs=pd.DataFrame({"userid":[1,2,3],"msg":["hi","hello","how are you"]})
# print(users)
# print(msgs)

# concat :
"""print(pd.concat([users,msgs]))
print(pd.concat([users,msgs],axis=1))
"""
# merge : 
c=pd.merge(users,msgs,on="userid")  # inner join  
# print(c)

# print(users.merge(msgs))
users =users.rename(columns={"userid":"id"})
# print(users.merge(msgs,left_on="userid",right_on="userid"))

a =users.merge(msgs,left_on="id",right_on="userid",how="left")
b =users.merge(msgs,left_on="id",right_on="userid",how="right")
c =users.merge(msgs,left_on="id",right_on="userid",how="outer")

# print(a)
# print(b)
print(c)