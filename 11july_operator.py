# operators : 
"""
1. airthematic  : +  -  *  /  %  //   ==>  floor  division 
2. comparison : < > <= >= == != 
3. logical : and  ,or,  is not  ==> and  both  con true 
4. assignmnent : +=  -=  *=  /=  %=  //=
5. relational : in , not in 

"""
"""
a=["apple","kiwi","mango","banana"]
print("chiku" not  in a)
"""

# conditional statement : 
"""
if  else : 

syntax : 
if condition :
    print
else :
    print 
"""

"""
a=int(input("enter the number 1:"))
b=int(input("enter the number  2 :"))

if a>b:
    print("a is  big")
else :
    print("b is big")
"""

"""
a=int(input("enter the number 1:"))
b=int(input("enter the number  2 :"))

if a>b:
    print("a is  big")
if b>a :
    print("b is big")
"""

# ladder : 
"""
syntax : 

if (con) :
    print
elif (con):
    print
else :
    print

"""

"""
a=int(input("enter the number 1:"))
b=int(input("enter the number  2 :"))

if a>b: 
    print("a is  big")
elif b>a :
    print("b is big")
else :
    print("a and b are same")
"""

# nested  : 
"""
syntax :
if (con):
    if (con):
        print
    else :
        print
elif (con):
    if(con):
        print
    else :
        print
else :
    print 
"""

"""
a=int(input("enter the number 1:"))
b=int(input("enter the number  2 :"))
c=int(input("enter the number  3 :")) 

if a>b :
    if  a>c  :
        print("a is big")
    else :
        print("c is big")
elif b>a:
    if  b>c:
        print("b is  big.")
    else :
        print("c is big")
else :
    print("same.") """

"""
task :1 
ask user to enter the salary and  calculate the gross salary. 

range             HRA    DA 

salary < 10000    20%    80% 
10000 -20000      25%    85%
20000 above       30%    90%

gross salary  = salary  + hra +da 

hint  :
user  = 9000 
hra =  salary  * 0.20 =1800 
da = salary  * 0.80 =7200 
gross  salary =9000 + 1800 +7200 =18000

task :2 
ask user to enter the character and  convert  into  the upper  case and lower case 
and vice versa . 

input  : a   output  :A 
hint  : ascii value , ord() function  :  
A =acii value   ==>  65   a acii  value  = 97  diff ==> 32 
"""
# ord ==>  ascci value  print 
"""ch =input("enter the character : ")

if (ch >='a' and  ch<='z'):   # lower character ==> lower upper  : a =97 A =65 diff =32
    ch = ord(ch)- 32 
else :
    ch = ord(ch)+32
print(chr(ch))
"""

"""
task : 4 

ask usert to enter the  3 number  and  print small  medium  big 

a =10 b= 20 c =30   a small  b mdium  c big
"""

