#constructor  :  automatically called when  object is  created. 
"""
1. deafult constructor
2. parameterized constructor
3. non parameterized constructor
"""
# default constructor :
"""
class person : 
    def __init__(self):   # def  ==> func  __init__ ==> special  method , construtor 
        print("today is  manit day because he is coming  offline  today.")
        print("he  is going to  work  on  his  project  today.")
p=person()
"""

#non parameterized constructor :

"""class person : 
    def __init__(self):
        self.name ="manit"
        self.age=20
        self.clg="J.G"
    def show(self):
        print("name is  : ",self.name)
        print("age is  :",self.age)
        print("clg is  :",self.clg)
p=person()
p.show()
print(p.name)
print(p.age)
print(p.clg)
"""

# parameterized constructor :

"""class person : 
    def __init__(self,name,age,clg):
        self.name=name
        self.age=age
        self.clg=clg
    
    def show(self):
        print("name is  : ",self.name)
        print("age is  :",self.age)
        print("clg is  :",self.clg)

name=input("enter name  : ")
age=int(input("enter age  : "))
clg=input("enter clg  : ")
p=person(name,age,clg)
p.show()
"""

# constructor overloading :

"""class student :
    def __init__(self):
        print("hello student ")
    def __init__(self):
        print("hello employee ")
    def show(self):
        print("hello ")
    def show(self):
        print("hello  maaaaaanit")

s=student()
s.show()
"""

"""class calculator :
    def add(self,a=5 ,b=5,c=5):
        return a+b+c
    
c=calculator()
print(c.add())   #0 
print(c.add(10,12))#
print(c.add(10,12,13))
"""
# s 0 0 35   m  d 0 0 30  di   pur  jai 0 22 35 

# bank  : 

class bank : 
    def __init__(self,name,accno,branch):
        self.name=name
        self.accno=accno
        self.branch=branch
        self.balance=25000
    
    def deposit(self,amt):
        self.balance+=amt
        print("deposited  :",amt)
    
    def withdraw(self,amt):
        if self.balance -amt >=10000:
            self.balance-=amt
            print("withdrawn  :",amt)
        else:
            print("insufficient  funds")
    
    def check_balance(self):
        print("balance is  :",self.balance)

b=bank("manit",1234455,"SBI") 
b.deposit(10000)
b.withdraw(1000)
b.check_balance()

#task  : 1
""" 
1 login  :   ==> user name  password   ==>check 
or : 
pin  : correct ==> deposit  withdraw  ==> check balance   max attempt 3 : 
"""
