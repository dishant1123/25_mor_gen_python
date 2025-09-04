# string  :  immutable  sequence  of  characters. ==>  no changes  in string. 

"""
s1="my name is manit shah."

print(s1)
print(type(s1))
"""

# built in function  :  len min max sorted  sum  
# ascci value : 
"""
s1="my name is manit shah."
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
"""

# slicing  :
# pos index : 0  ==> l to r 
# neg index : -1 ==> r to l   

"""
s1="my name is manit shah."
print(s1[0])
print(s1[ 2 :5])
print(s1[  :10])
print(s1[1  :])
print(s1[2 :10 :2])  # 2 starting index  10  ending  index 2 step size 
print(s1[2 : -2])
print(s1[  :  : -2])
print(s1[  :  : -1])
"""
"""
task :1 

input  : dishant dipakkumar shah 
output  : d.d.shah 

task 2 : 
ask user to  enter the two strings and  interchange  the first three characters of both strings.

input 1 : color 
input 2 :full 

output :1 fulor
output :2 coll
"""

"""s2="dishant dipakkumar shah"
s3 =s2[0] +"." +s2[8] +"."+s2[19 : ]
# s4=s2[8]
# s5 =s2[19 :]
print(s3)
# print(s4)
# print(s5)

"""

"""s1=input("enter the string  1 : ")
s2=input("enter the string  2 : ")

# color  full 

modify_string1 =s2[ :3] + s1[3:]
print(modify_string1)
"""

# method  : 

s1="My Name is manit shah."

print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.casefold())  # string  lower case convert 
print(s1.title())



