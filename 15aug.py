# recusive  function  : 
"""
function call itself  in order to slove the  problem. 
"""

# def factorial1(n):
#     if n==0 or  n==1 :
#         return 1    # true 
#     else : 
#         return n *factorial1(n-1) 
# print(factorial1(5)) 
    
"""
factorial1 (5)  :  ==> 5 * factorial1(5-1)   ==>20 
factorial1 (4)  :  ==> 4 * factorial1(4-1)   ==>24 
factorial1 (3)  :  ==> 3 * factorial1(3-1)   ==>6
factorial1 (2)  :  ==> 2 * factorial1(2-1)   ==>2

5! = 1*2*3*4*5  =120 

maths formula  : 

n= n * (n-1)! 
"""

# fibo : seris  ==>  0 ,1 ,1  2 , 3  5 8 13 ...   

"""def fibo(n):
    if n==0 :
        return  0 
    elif n==1 :
        return 1 
    else :
        return  fibo(n-1) + fibo(n-2)
    
for  i in range(7):
    print(fibo(7))
"""    

# local variable  , global variable  : 

"""
local variable  : declared inside  the function  
"""

"""
def d():
    x=100   # local variable  
    print(x)
d()
"""
# print(x)  # not accessible  outside the function  . 

# global variable  :

"""
global variable  : declared outside the function and inside the function  and also  accessible  outside the function.
""" 

"""x=100   # global variable 
def d1():
    print(x)  # inside the func print 

d1() 
print(x)  # outside func print 
"""

# global modify : 
"""
x=100 
def d2():
    global  x 
    x=900 
    print(x)
d2()
print(x)
"""

# higher order function  :

"""def mutiplier (factor):
    def multiply_by_factors(n):
        return n * factor 
    return multiply_by_factors

double = mutiplier(2)
triple =mutiplier(3)

print(double(5))
print(triple(5))
"""
# multiplier returns a new function  based on factors . 