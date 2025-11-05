# pandas :  data  cleaning ==> SQL like  operation  ==> join,filter, group by,merge,sort   

import pandas as pd 

data = pd.read_csv("mckinsey.csv")
# print(data)

"""
b= data.head(20)  # ==> sql  fetch  ==> first  20 rows only 
print(b)

c =data.tail(5)  # sql offset ==> last  5 rows only
print(c)
"""
"""d=data["country"]
print(d)
print(type(d))
"""
"""e=data["population"].head(10)
print(e)
print(type(e))

f =data.info()
print(f)
"""
# shape : 
print(data.shape)

# create dataframe  manually :

"""t1 =pd.DataFrame([
    ["A",23,30000], 
    ["B",25,40000],
    ["C",27,50000],
    ["D",30,60000]
],columns=["name","age","salary"])

print(t1)
"""
t2=pd.DataFrame({
    "name":["purvesh","yash","satyam","sita"],
    "age":[23,21,20,22],
    "salary":[30000,40000,50000,60000]
})

# print(t2)
t2=t2.rename(columns={
    "name" : "Name",
    "age" : "Age",
    "salary" :"income",
    
})
"""print(t2)
t2["Gender"]=["M","M","M","F"]
print(t2)
"""
t2 =t2.drop(["Age"],axis =1)
print(t2)