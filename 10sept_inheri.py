# inheritance   :  to inherit  properties or  methods  from  another  class / parent class.
"""
type  inheritance : 

1. single level inheritance 
2. multiple level inheritance
3. multi level inheritance 
4. heirarchy inherirance
5. hybrid inheritance

"""

# single  level inheritance : 

"""class student : # base class  
    def display(self):
        print("student class ")

class clg(student):   # dervied class 
    def show(self):
        print("clg class ")

c=clg()
c.show()
c.display()
"""

# using constructor : 

"""class  student : 
    def __init__(self):  # non parameterized constructor
        self.rollno =1 
        self.name ="manit"
        self.age =20

class clg(student):
    def __init__(self,clg):  # paramertized constructor
        super().__init__()   # super() base class constructor  called 
        # student.__init__(self)  # calling non parameterized constructor
        self.clg=clg   
    def show(self): 
        print("rollno is  : ",self.rollno)
        print("name is  : ",self.name)
        print("age is  :",self.age)
        print("clg class ",self.clg)

c=clg("J.G")
c.show()
"""
# single level  inheritance  with encapsulation  : 

"""class vehicle : 
    def __init__(self,v_type,capacity_seat):
        self.__type =v_type
        self.__capacity_seat = capacity_seat
    def gettype(self):
        return self.__type
    def getcapacity(self):
        return self.__capacity_seat

class car(vehicle):
    def __init__(self,name,model,v_type,capacity_seat):
        super().__init__(v_type,capacity_seat)
        self.name =name 
        self.model =model
    
    def show(self):
        print("type is  : ",self.gettype())
        print("capacity is  :",self.getcapacity())
        print("name is  : ",self.name)
        print("model is  :",self.model)

c=car("audi","A3","4-wheeler",5)
c.show() 
"""

#multiple level inheritance : 
"""
class a: 

class b :

class c(a,b):

"""

class student : 
    def display(self):
        print("student class ")

class address:
    def show(self):
        print("address class ")

class clg(student,address):
    pass 

c=clg()
c.display()   # ==> student 
c.show() # ==> address 