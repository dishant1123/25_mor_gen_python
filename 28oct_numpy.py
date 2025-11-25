import numpy as np 

# function  : zeros(),ones(),one()

"""a= np.arange(10)
print(a)

b =np.zeros((3,5),dtype=int)  # print  0 array  size will  3,5
print(b)

c=np.ones((2,4),dtype=int)  # print  1 array  size will 2,4 
print(c)

d=np.full((2,4),22,dtype=int)  # print  22 array  size will 2,4
print(d)
"""
"""e= np.array([
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [21,22,1,23,44,56,76],
    [12,13,14,21,22,1,23]
])"""
# print(e)
"""
f= np.full(e.shape,88,dtype=int)  # print  88 array  size will 3,5
print(f)
"""
"""g=np.full_like(e,100)
print(g)
"""
"""h=np.reshape(e,(4,7))
print(h)
"""
"""
k=np.arange(10).reshape(2,5)     # 0-9 
print(k)
"""

# using  random  module  : 

import  random  as  r 

"""a =np.random.randint(low=10,high=50,size=(3,4))
print(a)
"""
"""b=np.random.random((4,4))  # 0-1 value  
print(b) 
"""

"""
c=np.random.randint(low=0,high=10,size=9).reshape(3,3) 
print(c)
"""


# task  :1 
"""
Get the following array using intrinsic methods and slicing:
1 1 1 1 1  
1 0 0 0 1 
1 0 9 0 1   # 2,2=9
1 0 0 0 1
1 1 1 1 1 

# hint  :  function  ones(), slicing   
"""
# solution  :
"""
x=np.ones((5,5),dtype=int)
x[1:4,1:4]=np.zeros((3,3),dtype=int)
x[2,2]=9
print(x)
"""

"""c=np.random.randint(low=0,high=10,size=9).reshape(3,3) 
print(c)

print(c.shape)   # array size  ==> row  col 
print(c.ndim)    # array dimention  ==> one d , 2 d 
print(c.size) 
print(c.itemsize)

print(c.T)  # traspose 
print(c.sum())
print(c.sum(axis=0) ) #axis  =0   ==>row wise
print(c.sum(axis=1) ) #axis  =1   ==>col wise

# aithematic : + - * / % 
print(c+10)
"""

"""a= np.zeros((3,5))  # print  0 array  size will  3,5
b=np.ones((2,4))  # print  1 array  size will 2,4

c= np.full((2,4),fill_value=10)
print(a)
print(b)
print(c)
"""
