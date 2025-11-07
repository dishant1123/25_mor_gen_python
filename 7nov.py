import  pandas as pd
# loc : explicit
# iloc :implicit  

df = pd.read_csv("mckinsey.csv")
# print(df)

cont =df[["country","gdp_cap"]].head(20)
# print(cont)

# print(cont.loc[11])   # index ==>  value print 
# print(cont.loc[["Afghanistan"]])   # it given error bcz of  repeated value 

# print(cont.loc[11 :15])   # index ==>  value print  ==> both  point included 

# iloc : 
# print(cont.iloc[11 :15])   #  last value  excluded

# print(df.iloc[2:5,1:4])
# print(df.loc[2:5,1:4])  # not  poss in loc 

# print(df.loc[2:5,["year","gdp_cap"]])  
# print(df.loc[2:5,"year":"gdp_cap"])  

# print(df.iloc[1:10:2])
print(df.iloc[[2,7]])
