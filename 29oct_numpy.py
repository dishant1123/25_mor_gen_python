import numpy as np 
# task :2 
"""
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25
26 27 28 29 30

print  only below  this element  : 

11 12 
16 17 
"""

# task  :3 
"""
1 2 3 4 5           # index ==> 0   ==> 1 2 3 4 5  ==>  index num 0 1 2 3 4 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25
26 27 28 29 30


print  only below  this element  :

output : [2,8,14,20]
"""

"""
a= np.arange(1,31).reshape(6,5) 
print(a)
#        r   c 
print(a[[0,1,2,3],[1,2,3,4]])
"""
# task :4 
"""
1 2 3 4 5 
6 7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25
26 27 28 29 30

print  only below  this element  :

ouptut  : [[4,5],
           [24,25],
           [29,30]]
"""


# a= np.arange(1,31).reshape(6,5) 
# print(a)
# print(a[0,3:])
# print(a[4,3:])
# print(a[5,3:])

# print(a[[0,4,5],3:])


c =np.random.randint(low=0,high=10,size=10)
print(c)

print(np.where(c>5))
# print(d)