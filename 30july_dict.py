#dict : mutable  ==> changes in dict , ==> key value  pair 

"""
d1={"phy":90, "maths":78}
# phy  key  90 value  , maths key  value 78 
print(d1)
print(type(d1))
"""

"""
d2 ={90:78, "maths":90}
print(d2)
print(type(d2))
"""

# to add  in dict : 

"""
d1={"phy":90, "maths":78}
d1["che"]=99
d1["phy"]=67
print(d1)
"""

# built in function  :  len min max sorted sum 

"""
d1={"phy":90, "maths":78}
print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
"""

# slicing  : 

"""
d1={"phy":90, "maths":78}
print(d1[0])  # not possible in dict ==>slicing  
"""

# method  :
# d1={"phy":90, "maths":78}

"""d1.clear()
print(d1)
"""
"""
d2 =d1.copy()
print(d2)
"""

"""print(d1.keys())
print(d1.values())
print(d1.items())

for  i  in d1.keys():
    print(i)

for x   in  d1.values():
    print(x)

for  x,y in d1.items():
    print(x,y)
"""

"""l1=["devnag","manit"]
d2=dict.fromkeys(l1,100)
d2["manit"]=2
print(d2)
"""

d1={"phy":90, "maths":78,"che":99}

# print(d1.get("maths"))
"""
d2={"manit":2,"devang":3}
d1.update(d2)
print(d1)
"""

"""
d1.pop("maths")
print(d1)
"""
"""
d1.popitem()
print(d1)
"""

"""
d1.setdefault("s.s",100)
print(d1)
"""

"""
task  : 1 

ask user to enter the name and marks  of 5 students and store in to the dict.. 
input  : manit 90  devang 89  satyam  88  harshil 99 ram 67 
output  : d1 = {"manit":90, "devang":89, "satyam":88, "harshil":99, "ram":67}
"""

"""
d1={}
for i  in range(3) :
    name =input("enter the name  : ")
    marks= int(input("enter the marks : "))
    d1[name] =marks
print(d1)   # d1 = {"manit":90, "devang":89, "satyam":88, "harshil":99, "ram":67}
"""
# task :2   sorted marks  : 

"""
sorted_values = sorted(d1.values())
print(sorted_values)  # [88, 92, 99]
d2={}
for i in sorted_values:
    for  name , marks in d1.items(): # {"manit" :99, "devang" :88, "satyam" :92} 
        if i ==marks :
            d2[name]=marks 
print(d2)
"""

#task :3 
"""
ask user to enter the string  and count of the letter and  store  in  to the  dict . 
input  : "mississappi" 
output  : {"m":1 , "i" :3 ,"s" :4 , "a" :1 , "p" :2}
"""