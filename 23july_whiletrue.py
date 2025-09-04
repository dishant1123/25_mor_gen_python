#while  true  : 
"""
syntax : 

i=intial value 

while True :
    print statement
    inc/dec 
    break
"""

"""i=1 
while True : 
    print(i)
    i+=1
    if  i==10:
        break
"""
#match  : 

"""a=int(input("enter the number  : "))
b=int(input("enter the number  : "))

print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
print("6. new number ")


choice =int(input("enter the choice : "))

match choice:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a//b)
    case 5:
        print(a%b)
    case _ :
        print("exit")
"""        
# data type  : 

# 1.  list  :  mutable  ==>  changes in list, ordered 

"""
l1=[1,2,3,4,5,"manit",2j,12.56]
print(l1)
print(type(l1))
"""

"""
l1=[1,2,3,4,5,"manit",2j,12.56]
# index : start  0  ==> pos index ==> l to r 
# neg index : r to  l  ==> start  -1 
print(l1[0])
print(l1[-2]) 
"""

#built in function  : len  min max sorted sum 
"""
l1=[1,2,3,4,60,90,88]
print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1)) # asc to desc 
print(sum(l1))
"""

# slicing  : 

l1=[1,2,3,4,60,90,88]
print(l1[1])
print(l1[1 :5])  #1 start index 5 end index

print(l1[2 :-2])
print(l1[1 :-4])
print(l1[ :-1])  # start  by default  0 

print(l1[2 :5 :2])  # step size  :2 