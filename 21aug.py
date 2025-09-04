# lambda function  : one liner function 
"""
syntax : 

lambda argument : expression  
""" 

"""def d():
    a=10 
    b=20 
    c=a+b
    print(c)
d()
"""

"""
x = lambda a,b : a+b
print(x(12,45))
"""

# built in function :  len  min max sorted sum 

"""
a= lambda x : sorted(x)
print(a((1,45,67,2,3,4,5)))
"""

# lambda  if  else : 

"""def big():
    a=int(input("enter the number  1: "))
    b=int(input("enter the number  1: "))
    if a>b :
        print("a is big")
    else :
        print("b is big")
big()
"""

"""
x =lambda a,b :  ("a is big")if a>b else ("b is big")
a=int(input("enter the number  1: "))
b=int(input("enter the number  1: "))
print(x(a,b))
"""

# filter: filter the  information  not  given  new  list. no changes in the original list. 

"""
phonepe ==>transaction  ==> june  transaction ==> filter ==> june 
"""

# l1=[1,2,3,4,5,6,7,8,9,10]
"""even=[]
odd=[]
for i in l1 : 
    if i%2 ==0 :
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)
"""

"""l1=[1,2,3,4,5,6,7,8,9,10]
a= list(filter(lambda x : x % 2==0,l1)) 
b= tuple(filter(lambda x : x % 2==1,l1)) 
print(a)
print(b)
"""

# map : given  a new list . 

# l1=[2,6,9,10]
"""
l2=[]

for i in l1 :
    l2.append(i**2)
print(l2)
"""

"""
l1=[2,6,9,10]
a=list(map(lambda x : x **2,l1)) 
print(a)
"""

# task  :1 
"""
input  : [[1,2] , [2,0],[9,3]]  sort the  list  second  element. 
output  : [[2,0],[1,2], [9,3]]

explain : 

input  : [[1,2] , [2,0],[9,3]]  === >  len  ==> 3 

0 == > row [1,2] ==< 1 index number  ==>0 2 index number ==> 1
1 == > row [2,0] ==< 2 index number  ==>0 0 index number ==> 1
2 == > row [9,3] ==< 9 index number  ==>0 3 index number ==> 1

"""

