# encapsulation  : 
"""
1. data hiding
2. security  
3. private  variable  access directly  using ==> get  , set method   

get method :  get variable value ,  print  
set method  :  new value set 
"""
class bank : 
    def __init__(self,name ,accno):
        self.__name = name     # name  accno balance  ==> private variable
        self.__accno = accno
        self.__balance = 25000
    def deposit(self,amount):
        self.__balance += amount
        print(f"balance after  depsoit {amount} is  : {self.__balance}")
    def withdraw(self,amount):
        self.__balance -=amount
        print(f"balance after  withdraw {amount} is  : {self.__balance}")
        
    def get_name(self):
        return self.__name
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,new_balance):
        self.__balance = new_balance

b=bank("satyam",4567890)
print("==========without using set method ======== ")
b.deposit(1000)
b.withdraw(500)
print("your final balance is  :",b.get_balance())

print("==========using set method ======== ")
b.set_balance(90000)
b.deposit(10000)
b.withdraw(50000)
print("your final balance is  :",b.get_balance())
