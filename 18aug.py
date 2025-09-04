'''"""
employess management  : 

1. add emp 
2. delete emp
3. update emp
4. search emp
5. display emp 
6. exit 
"""

"""
d1={"ram" :100,"manit":500}
d1["hari"]=90
print(d1) 
"""

d1={}

def add_emp():
    id= int(input("enter the  id : "))
    name =input("enter the name  : ")
    salary =int(input("enter the salary : "))
    d1[id] =[name,salary]
    print("emp added successfully")

def update_emp():
    id =int(input("enter the  id you want to  update : "))
    if id in d1 : 
        name =input("enter the name  : ")
        salary =int(input("enter the salary : "))
        d1[id] =[name,salary]
        print("emp updated successfully")
    else :
        print("emp not found")

def delete_emp():

    id =int(input("enter the  id you want to  delete : "))
    if id in d1 :
        del d1[id]    # del  ==> function
        print("emp deleted successfully")
    else :
        print("emp not found")

add_emp()
add_emp()
print("before  update  : ")
print(d1)

update_emp()
print("after  update  : ")
print(d1)

print("after delete : ")
delete_emp()
print(d1)

while True :
    print("1. add emp")
    print("2. update emp")
    print("3. delete emp")
    print("4. search emp")
    print("5. display emp")
    print("6. exit")
    
    choice =int(input("enter your choice : "))
    if choice==1 :
        add_emp()
    elif choice==2 :
        update_emp()
    elif choice==3 :
        delete_emp()
    elif choice==4 :
        # search_emp()
    elif choice==5 :
        # display_emp()
    else :
        break

"""
id   name    salary 
1    satyam  90000 
2    manit   89000 

"""
'''
"""17.
x = "apple"
match x:
    case "banana":
        print("Banana")
    case "apple" | "mango":
        print("Fruit")
    case _:
        print("Other")
"""


for i in range(1,5):
    for j in range(1,5):
        if (i+j) % 2 == 0:
            print(i,j)