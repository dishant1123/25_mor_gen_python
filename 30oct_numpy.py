import  numpy as np 

"""
c=np.random.randint(low=-10,high=10,size=10)
print(c)
"""
"""
b= c[np.where(c>5)]  # condition  
print(b)
"""
"""d =np.count_nonzero(c)  # it is  count  of non-zero element.  
print(d)
"""
# vstack ,hstack  : 
"""
c=np.random.randint(low=-10,high=10,size=10)
d=np.random.randint(low=-10,high=10,size=10)

print(c)   # 1 d array  
print(d)
"""
"""e=np.vstack((c,d))   # vertical  ==> 2 d array 
print(e)
"""
"""t=np.hstack((c,d))   # horizontal  ==> 1 d array
print(t)
"""

# repeat : 

# c=np.random.randint(low=-10,high=10,size=10).reshape(5,2)

"""f= np.repeat(c,2,axis=1)  #1 2 3  ==> 1 1 1  2 2 2 3 3 3    
print(f)
"""

"""g=np.repeat(c,2,axis=None)
print(g)
"""

# matrix multiplication :
"""
A           B
[[1 2 3],     [[4,9,6]              
 [4 5 6],       [4,5,5],
 [7 8 9]]      [7,8,9]]
 
"""

"""
a=np.random.randint(low=5,high=20,size=9).reshape(3,3)
b=np.random.randint(low=5,high=20,size=9).reshape(3,3)

print("a=",a)
print("b=",b)

# s=np.matmul(a,b)  
s=np.dot(a,b)
print("multiplication of  matrix :\n")
print(s)
"""

# statistical methods :

a=np.array([
    [1,2],
    [3,4],
])

"""
b=np.identity(4)
print(b)
"""

# mean mode  : 

a=np.array([
    [1,2],
    [9,4],
])

"""mean_of_a=np.mean(a)
print(mean_of_a)

median_of_a=np.median(a)  # [[1,2,4,9]]
print(median_of_a)

std_of_a=np.std(a)
print(std_of_a)

x=np.var(a)
print(x)
"""

"""a=np.array([
    [1,2],
    [9,4],
])
print(a)
print(np.min(a))
print(np.min(a,axis=0))
print(np.min(a,axis=1))
"""

# next : loadfromtxt , genfromtxt : 