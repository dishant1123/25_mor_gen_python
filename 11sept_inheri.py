# multi level  : 
"""
class a  : 

class b (a): 

class c (b):
"""

"""class student : 
    def __init__(self):
        self.rollno =1 
        self.name ="manit"
        self.age =20

class parent(student):
    def __init__(self,father,mother):
        super().__init__()   # super() base class constructor  called
        self.father =father
        self.mother =mother

class clg(parent):
    def __init__(self, father, mother,clg):
        super().__init__(father, mother) # student.__init__(self,name,age,rollno) ,parent.__init__(self,father,mother)
        self.clg =clg 
    def show(self):
        print("rollno is  : ",self.rollno)
        print("name is  : ",self.name)
        print("age is  :",self.age)
        print("clg class ",self.clg)
        print("father is  : ",self.father)
        print("mother is  : ",self.mother)

c=clg("prafulbhai","jagrutiben","J.G")
c.show()
"""

# hierarchy inheritance :
"""
class a : 

class b (a): 

class c(a): 
"""

"""class vehicle : 
    def __init__(self,v_type,capacity_seat):
        self.__type =v_type
        self.__capacity_seat = capacity_seat
    def getv_type(self):
        return self.__type
    def getcapacity(self):
        return self.__capacity_seat
    
class car(vehicle):
    def __init__(self, v_type, capacity_seat,name,model):
        super().__init__(v_type, capacity_seat)
        self.name =name 
        self.model =model
    def show(self):
        print("type is  : ",self.getv_type())
        print("capacity is  :",self.getcapacity())
        print("car name is  : ",self.name)
        print("car model is  :",self.model)

class bike(vehicle):
    def __init__(self,v_type,capacity_seat,name,model):
        super().__init__(v_type,capacity_seat)
        self.name =name 
        self.model =model
    def show(self):
        print("type is  : ",self.getv_type())
        print("capacity is  :",self.getcapacity())
        print("bike name is  : ",self.name)
        print("bike model is  :",self.model)

c=car("4-wheeler",5,"audi","A3")
b=bike("2-wheeler",3,"suzuki","s4")
c.show()
b.show()
"""

# hybrid inheritance : 
"""
it is  combination  of  one or more  inheritance . 
"""

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class manager(employee):
    def __init__(self, name, salary, manager_name):
        employee.__init__(self, name, salary)
        self.manager_name = manager_name

class senior_manager(employee):
    def __init__(self, name, salary, sr_manager_name, department):
        employee.__init__(self, name, salary)
        self.sr_manager_name = sr_manager_name
        self.department = department


class ceo(manager, senior_manager):
    def __init__(self, name, salary, manager_name, department, ceo_name, sr_manager_name):
        manager.__init__(self, name, salary, manager_name)  # 
        senior_manager.__init__(self, name, salary, sr_manager_name, department)  # 
        self.ceo_name = ceo_name

    def show(self):
        print("name is  : ", self.name)
        print("salary is  :", self.salary)
        print("manager name is  : ", self.manager_name)
        print("sr_manager name is  : ", self.sr_manager_name)
        print("ceo name is  : ", self.ceo_name)
        print("department is  : ", self.department)


c = ceo("satyam", 100000, "purvesh", "IT", "manit", "jainish")
c.show()
