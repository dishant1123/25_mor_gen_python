# spilt , partition , index , find 

s1="my name is manit shah."

"""
print(s1.count("a"))
print(s1.count("a",6,20))
"""

"""
s2="happy vasuli divas"  # 9 aug 
print(s2)
print(s2.center(50,"@"))
print(s2.ljust(50,"#"))
print(s2.rjust(50,"#"))
"""

s1="my name is manit shah."

"""
print(s1.split())  #given ans in list .
print(s1.split("a")) 
print(s1.split("is")) 

# diff between split and rsplit : 
print(s1.rsplit("a"))
"""

"""print(s1.partition("a")) # 3 parts 
print(s1.partition("is")) 

print(s1.rpartition("a"))
"""

# index rindex find  rfind : 
s1="my name is manit shah."

"""print(s1.index("y"))
print(s1.index("a"))
print(s1.index("a",5,15))
print(s1.index("a",13,20))

print(s1.index("is"))
print(s1.index("name"))

print(s1.find("a"))
print(s1.find("is"))
"""

"""
print(s1.rindex("a"))  # method 
# print(s1[-3])  #slicing 
print(s1.rindex("is")) 

print(s1.rfind("a"))
"""

"""
task :1 

input  : i am going to goa next month. 
output : first "o" index :6
        second "o" index :12
        third "o" index :15 
        fourth "o" index :24 
      
"""
"""s2 ="the lion in the cage."
print(s2.replace("lion","tiger"))
print(s2.replace("the",""))
print(s2.replace("the","",1))
"""

"""
task :2 
hint : replace +slicing 
input  : restart 
output : resta@t
"""

"""
task :3 
hint : replace + slicing 
ask user to enter the string  and replace first space and last spce with "_". 

input : my name is satyam patel. 
output : my_name is satyam_patel.
"""
s1 ="my name is satyam patel."

modify_string=s1.replace(" ","_",1)[::-1].replace(" ","_",1)[: : -1]
print(modify_string)
