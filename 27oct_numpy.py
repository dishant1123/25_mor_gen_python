"""
numpy  :  array  ==> multiply ,  sub  ==> matrix 

pip install  numpy 
"""

import numpy as np   

"""a=np.array([1,2,3,4,5,6,"purvesh","satyam"])  # by default ==> 1d array  ==> string 
print(a)

b=np.array([1,2,3,4,5,6,89.90],dtype=int)
print(b)

c= np.array([12.45,78.90,34.56,23.45,12.34,56.78,89.90,12],dtype=float)
print(c)

d =np.array([[1,2,3],[4,5,90]])
print(d)

d=np.array([1,2,3,4,5,6,89.90],dtype="int 64")  #  int 64 ==> long  ==> 8 bytes
print(d)
"""

# slicing  ==>  array[start:end:step]

"""
a= np.array([
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [21,22,1,23,44,56,76],
    [12,13,14,21,22,1,23]
])
# print(a)
print(a[0,4])
print(a[1,2:4])
print(a[3, : ])
print(a[0,: : -1])
print(a[1:3,2:6])  # 1:3 

"""
# manupulating array  using index  : 
"""c= np.array([12.45,78.90,34.56,23.45,12.34,56.78,89.90,12],dtype=float)
print(c)
c[2]=12.899
print(c)
"""

# function  : arange(),reshape()

"""a=np.arange(10)
print(a)

b=np.arange(3,19)
print(b)

c=np.arange(3,20,2)  # [ 3  5  7  9 11 13 15 17 19]
print(c)

d= c.reshape(3,3)  # matrix :  2d array  
print(d)

e= b.reshape(4,4)
print(e)
"""