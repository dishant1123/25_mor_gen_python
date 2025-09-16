# inheritance ,  poli , encap  : 

class account :
    def __init__(self,accno,name,balance=0):
        self.__accno=accno
        self.__name=name
        self.__balance=balance

    #encp get set : 
    def get_accno(self):
        return self.__accno
    def get_name(self):
        return self.__name
    def get_balance(self):
        return self.__balance
        
    def deposit(self,amount) :
        self.__balance+=amount
        print(f"amount deposited : {amount} current balance : {self.__balance}")

    def withdraw(self,amount) :
        if self.__balance - amount >=10000 :
            self.__balance-=amount
            print(f"amount withdrawn : {amount} current balance : {self.__balance}")
        else :
            print("Insufficient funds you  have  to min balance  10000 rs.")
    # poli : 
    def account_type(self):
        return "general account"

class savings_account(account):
    def __init__(self, accno, name,interest_rate, balance=0):
        super().__init__(accno, name, balance)
        self.interest_rate=interest_rate
    
    def account_type(self):
        return "savings account" 

    def add_interest(self):
        interest =  self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print(f"interest added : {interest} current balance : {self.get_balance()}")

class current_account(account):
    def __init__(self, accno, name,overdraft=5000 ,balance=0):
        super().__init__(accno, name, balance)
        self.overdraft=overdraft
    
    def account_type(self):
        return "current account"

    def withdraw(self, amount):# bal :30000 
        if amount <=self.get_balance() +self.overdraft:
            new_balance =self.get_balance()-amount
            self.account_balance = new_balance
            print(f"amount withdrawn : {amount} current balance : {self.account_balance}")
        else :
            print("Insufficient funds you  have  to min balance  10000 rs.")

s=savings_account(1234,"satyam",5,25000)
c=current_account(56789,"jainish",20000)

print("account type: ")
print(s.get_name(),s.account_type())   # poli 
print(c.get_name(),c.account_type())

# deposit : 
s.deposit(10000)
s.add_interest()

# withdraw :
c.withdraw(12000)
# c.withdraw(20000)
print(c.get_balance())



