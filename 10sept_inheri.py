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

class vehicle : 
    def __init__(self):
        self.__type ="4 wheeler"
        self.__capacity_seat =5 
    def gettype(self):
        return self.__type
    def getcapacity(self):
        return self.__capacity_seat

class car(vehicle):
    def __init__(self,name,model):
        super().__init__()
        self.name =name 
        self.model =model
    
    def show(self):
        print("type is  : ",self.gettype())
        print("capacity is  :",self.getcapacity())
        print("name is  : ",self.name)
        print("model is  :",self.model)

c=car("audi","A3")
c.show() 