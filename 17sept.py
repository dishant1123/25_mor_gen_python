# abstaction  : 
"""
abstraction  is  process of hiding the detalis and showing  only essietial details/ features of object.

1.abstract  base class ==> ABC  ==> abstact base class 
2. @abstactmethod ==> decorator  
"""

from abc import ABC, abstractmethod 

class vehicle(ABC):

    @abstractmethod
    def start(self):
        pass 
    
    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def start(self):
        print("car started")
    
    def stop(self):
        print("car stopped")

class bike(vehicle):
    def start(self):
        print("bike started")
    
    def stop(self):
        print("bike stopped")
b=bike()
c=car()
b.start()
b.stop()

c.start()
c.stop()

"""
cpp : 
class vehicle 
{
    public : 
        string name; 
    virtual void start()=0;   ==> pure virtual function  
};
"""



