"""
polimorphsim : many  forms 

1.method  over  loading 
2.method  over  riding  
"""

# method over loading  with default  argument  : 

"""class calculator  : 
    def sum(self,x=0,y=0,z=0) :
        return x+y+z
    
c=calculator()
print(c.sum(23))
print(c.sum(12,12,34))
print(c.sum(12,23))
"""

# method over  riding  : 

"""class animal: 
    def speak(self):
        print("animal can speak")

class cat(animal):
    def speak(self):
        print("cat can speak")

class dog(animal):
    def speak(self):
        print("dog can speak")


c=[dog(),cat()]
for i in c :
    i.speak()
"""

# loading + riding : 

class shape:
    def area (self,a=0,b=0):
        return a*b     # method  over  loading with defualt  argument
    
class square(shape):
    def area(self,a=0,b=0):
        return a*a     # method  over  riding

class rectangle(shape):
    pass  

s=square()
r=rectangle()

print("square  area is  : ",s.area(4))  # over ride 
print("rectangle  area is  : ",r.area(4,5))  # inheirtance 