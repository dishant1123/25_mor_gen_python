# function  : 
"""
1. no arg no return  
2. with arg no return  
3. no arg  with return 
4. with arg  with return
"""
"""a=10
b=20 
print(a+b)
"""

# no arg  no return : 

"""def sum():  # def key word  sum () ==> function  name  
    a=int(input("enter a number"))
    b=int(input("enter a number"))  # function  intialization
    print(a+b)
sum()  # function calling  
sum()
print("manit")
sum()
"""

# with arg  no return  : 

"""
def sum(a,b):
    c=a+b
    print(c)
x=int(input("enter a number"))
y=int(input("enter a number"))  # function  intialization
sum(x,y)  
"""

# no arg with return  : 

"""
def sum():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=a+b
    return c 
print(sum())
"""

# with arg with return  :

"""
def sum(a,b):
    c=a+b
    return c 
print(sum(12,14))
"""

# *args , **kwargs: 

# *args :

"""
def sum1(*args):
    return sum(args)   # sum ==> built  in function   
print(sum1(14,12,14,12,45,67,89,90.87,55,55))
"""
# *args : it take only number arg  and also  allowed to decimal. 


"""def d(*x):
    sum =0 
    for  i in x : 
        sum =sum +i
    print(sum)
d(1,2,3,4,5,6,7,8,888,88,99)
"""

# **kwargs: take any keyword args : 

"""
def d1(**kwargs):
    for i , j in  kwargs.items():
        print(f"{i} : {j}")
d1(name="manit",age=21,gender="male")
"""

# prime  : 

"""
def prime(n):
    count =0 
    for i in range(1,n+1):
        if n % i==0:
            count +=1
    if count ==2:
        return  1   # ture ==>1
    else:
        return 0  # false ==>0
x =int(input("enter a number"))
if prime(x) ==1:
    print(x,"is prime")
else :
    print(x,"not prime")
"""

# emp manag system : 
"""
1.add 
2.delete
3.search
4.update
5.display
"""

"""d1={}

def add():
    id=int(input("enter id : "))
    name=input("enter name : ")
    salary=int(input("enter salary : "))
    d1[id] =[name,salary]
    print("data added successfully")

def update():
    id =int(input("enter the  id you want to update : "))
    if id in d1:
        name=input("enter new name : ")
        salary=int(input("enter new salary : "))
        d1[id]=[name,salary]
        print("data updated successfully")
    else :
        print("data not found")

def delete():
    id =int(input("enter the  id you want to delete: "))
    if id in d1:
        del d1[id]
        print("data deleted successfully")
    else :
        print("data not found")
add()
add()
update()
delete()
print(d1)"""
"""
d1 ={
    id   name   salary 
    1:["manit",1000],
    2:["manish",2000],
    3:["manish",3000]
}
emp  manag  system

1. add 
2. delete
3. search
4. update
5. display  
6. exit 
"""

"""i = 0
while i < 3:
    print(i)
    i += 1
else:
        print(0)
"""
# for i in range(10):
#     # if i == 5:
#     #     break
#     print(i)
# else:
#     print("Here")

print(18 //4)

