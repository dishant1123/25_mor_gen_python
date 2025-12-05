import  numpy as  np 

a= np.array([
    [1,2,3,4,5],  # 0 
     [6,7,8,9,10],  # 1 
    [11,12,13,14,15], # 2
    [16,17,18,19,20], # 3 
    [21,22,23,24,25]  # 4 
])

a[0] =[45,67,89,23,89]
# print(a)

"""print(a)
print(a[0])
print(a[0][1:3])
print(a[[0],[1]])
print(a[0][0:3])
print(a[[0,1,2,3],[1,2,3,4]])
"""
        # row  # col 
# print(a[1:3 ,1:4])
# print : 
"""
output  : 
[[4,5],
[19,20],
[24,25]]

[[7,8,9],
[12,13,14],
[22,23,24]]
"""
# print(a[[0,3,4],3:5])

"""
b=np.ones((3,3),dtype=int)
print(b)

c=np.zeros((3,3),dtype=int)
print(c)
"""
"""
task :1 
[[1,1,1,1,1],
[1,0,0,0,1],
[1,0,9,0,1],
[1,0,0,0,1],
[1,1,1,1,1]]

"""
# random  : 
import  random 

# a=np.random.random((3,4))  # 0-1 float 
# print(a)

# b=np.random.randint(low=-10,high=10,size=12).reshape(4,3)
# print(b)

# c=np.random.sample((5,))
# print(c)

# a=np.random.randint(low=-10,high=100,size=16).reshape(4,4)
# b=np.random.randint(low=-10,high=100,size=16).reshape(4,4)
# print("a matrix :\n",a)
# print("b matix :\n",b)  

# print("addition of two matrix :\n",a+b)
# print("sub of two matrix :\n",a-b)

# print("multiplication of two matrix :\n",a*b)  # not  matrix multiplication

# print(np.matmul(a,b))

"""
x=np.random.randint(low=-30,high=30,size=16).reshape(4,4)
print(x)
print(x.size)
print(x.shape)
print(x.ndim)
print(x.itemsize)
print(x.T)
"""
# mathematical operation  : 
"""
axis =0 column wise 
axis =1 row wise
"""
"""x=np.random.randint(low=-30,high=30,size=16).reshape(4,4)
print(x)
print(x.sum())
print(x.sum(axis=0)) # col wise  sum 
print(x.sum(axis=1)) # row wise  sum 
"""

"""
c= np.random.randint(low=-10,high=10,size=10)

print(c)
print(np.where(c>0))

print(np.count_nonzero(c))
print(np.nonzero(c))
"""
# vstack :

"""c= np.random.randint(low=-10,high=10,size=10).reshape(2,5)
d= np.random.randint(low=-10,high=10,size=10).reshape(2,5)
"""
# print(np.vstack((c,d)))
# print(np.hstack((c,d)))


# load from txt : 

"""a= np.loadtxt("manit_info.txt",dtype=str,delimiter="\t")
print(a)
"""

# gen from txt :

a=np.genfromtxt("manit_info.txt",dtype=None,delimiter=",",filling_values=-1,encoding="UTF-8",names=True)
print(a)