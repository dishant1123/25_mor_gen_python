# exception/ error handling  : 

# zero division error :
"""try :
    a=int(input("enter a number : "))
    b=int(input("enter a number : "))
    result =a/b 
    print(result)
except ZeroDivisionError:
    print("you can't divide by zero")
"""
# ValueError : 
"""
try :
    a=int(input("enter a number : "))
    b=int(input("enter a number : "))
    print(a,b)
except ValueError:
    print("data type  is  inter so you can't enter the  string  or float  number.")
"""

# syntax error  : 
"""code = "if True print('Hello')"  # Missing colon after 'if True'

try:
    compiled_code = compile(code, '<string>', 'exec')
    exec(compiled_code)
except SyntaxError as e:
    print("Caught a SyntaxError!")
    print("Error message:", e)
"""

#type error  : 
"""try:
    a=input("enter a number : ")
    b=input("enter a number : ")
    print(a,b)
    # c=a/b
except TypeError:
    print("you can't divide by of  two strings")
    
"""

# name error  : 

"""
try : 
    result =sqrt(25)
    print(result)
except NameError:
    print("you have to import math library")
"""

# file is not found  : 
"""
try :
    with  open("manit.txt","r") as file : 
        file.write("manit is a good boy")
except FileNotFoundError:
    print("file is not found because of  you have  open read mode in  read mode  only exiting file open")
"""

# file handling with oop : 

class filemanager :
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None 
    
    def __enter__(self):
        self .file = open(self.filename,self.mode)
        return self.file 

    def __exit__(self,exc_type,exc_value,traceback):  # close file  automatically when  exiting the with block 
        if  self.file :
            self.file.close()

class fileoperation :
    def __init__(self,filename):
        self.filename=filename
    
    def write_file(self,content):
        with filemanager(self.filename,"w") as file:
            file.write(content)
        print("file  write  successfully")
    
    def append_file(self,content):
        with filemanager(self.filename,"a") as file:
            file.write(content)
        print("file  append  successfully")
    
    def read_file(self):
        with filemanager(self.filename,"r") as file:
            data = file.read()
            print(data)

file_oops =fileoperation("divyang.txt")
file_oops.write_file("hello divyang ..... how  are  you ?\n") 
file_oops.append_file("i am good and i enjoying  navrati.\n")
file_oops.read_file()       
        
