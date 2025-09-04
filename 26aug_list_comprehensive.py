# list : mutable  squence 


"""l1=[1,2,3,4,5,6]  # 1 d array  : 
print(l1) 

""" 

# 2d : 

"""
l1=[[1,2],
    [3,4], 
    [5,6]]
"""
# print(l1)

"""
for i in l1:
    print(i)
"""

"""
l1=[[1,2,3],    # 0 
    [4,5,6],    # 1
    [7,8,9]]    # 2
"""
"""
components of list : 
 r c
(0,0)1  (0,1)2  (0,2)3
(1,0)4  (1,1)5  (1,2)6
(2,0)7  (2,1)8  (2,2)9

"""
"""
print(l1)
for i in l1:
    print(i)
"""
"""
l1=[[1,2,3,55],    # 0 
    [4,5,6,56],    # 1
    [7,8,9,58]]    # 2
"""
"""print(l1[0])
print(l1[0][1])
print(l1[1][0 :4])
print(l1[1][0 :3])
print(l1[2][1 :-1])
"""
"""print(l1[1][1 :3 :2])  # start stop step 
print(l1[2][1 :2 :-1])  # start stop step 
print(l1[2][1 :4 :-1])  # start stop step 
print(l1[2][ : :-1])  # start stop step 

print(l1[2][ -2: -4:-1])  # start stop step 
"""

# 3*3 matrix : 

l1=[[1,2,3],    # 0 
    [4,5,6],    # 1
    [7,8,9]]    # 2

# output  : 
"""
l1= [[1,4,7],
    [2,5,8],
    [3,6,9]]
"""
"""
for i  in range(3):
    for j in range(3):
        print(l1[j][i],end= " ")
"""
