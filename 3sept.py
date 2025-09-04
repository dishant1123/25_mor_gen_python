# oop  : object  oriented programming
"""
pillar : 
1.inheritance  : 5 type  : single   multiple  multi level heirarchy hybrid 
2.polymorphism : 2 method  :  1.  method  overloading  2.  method overriding
3.encapsulation : 2 method  : 1. get  2. set
4.abstraction  : abstact method 

class : blue print  of object 
object :  instance  of  class , real world entity 

fruits :   class 
    apple  kiwi  banana   == > object 

class : 
    public : accessible from anywhere
    private  : within  class only  
    protected : within  class only and  derived class
"""

"""class student :  # student  class 
    print("hello")

s=student()   #  s is object of class student

"""

# method : by default  public  ==> not mentioned any where  

"""class student : 
    name ="manit"  # name  age  clg ==> class data member 
    age=20 
    clg ="J.G"

s=student()
print(s.name)
print(s.age)
print(s.clg)
s.name="satyam"
s.age=21
s.clg="AU"
print(s.name)
print(s.age)
print(s.clg)
"""

# function in class : 
# self : key word ==> function  ==> access  class data member

"""class employee : 
    name="manit"
    age=20
    salary =90000
    def show(self):
        print("name is  : ",self.name)
        print("age is  :",self.age)
        print("salary is  :",self.salary)
s=employee()
s.show()
"""

# private class : 

"""
class vehicle :
    __name ="audi"  # name  , age  ==> private class data member
    __model="a3" 

    def show(self):
        print("name is  : ",self.__name)
        print("model is  :",self.__model)
v=vehicle()
# print(v.__name)  # not directly accessible beacuse  private
# print(v.__model)
v.show()
"""

# user : 

"""class emp :
    def scan(self): 
        self.name =input("enter name  : ")
        self.age =int(input("enter age  : "))
        self.salary =int(input("enter salary  : "))

    def show(self):
        print("name is  : ",self.name)
        print("age is  :",self.age)
        print("salary is  :",self.salary)
e=emp()
e.scan()
e.show()
"""

"""
bank  :  name  ,branch  , accno  , balance  

deposit  
withdraw
balance  
"""
