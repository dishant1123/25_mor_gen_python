# task  :1 
"""
input  : [[1,2] , [2,0],[9,3]]  sort the  list  second  element. 
output  : [[2,0],[1,2], [9,3]]

explain : 

input  : [[1,2] , [2,0],[9,3]]  === >  len  ==> 3 

0 == > row [1,2] ==< 1 index number  ==>0 2 index number ==> 1
1 == > row [2,0] ==< 2 index number  ==>0 0 index number ==> 1
2 == > row [9,3] ==< 9 index number  ==>0 3 index number ==> 1

"""

l1 = [[1,2],   # 1,2   == > 0 , 2 ==>1   (0,0) ==>1 (0,1) ==>2 
      [9,0],  #                          (1,0) ==>2  (1,1) ==>0
       [2,3]] #                          (2,0) ==>9  (2,1) ==>3
# print(sorted(l1))  # 1 element  sort 

"""for i in  l1:
    print(i)

print(len(l1))  # 3 6 
"""

"""for i in range(len(l1)):   # 0 1 2 
    for j in range(len(l1)-1):   # 0 1     2     >  0
        if l1[j][1]  > l1[j+1][1] :  # l1[0][1] > l1[1][1]
            l1[j] , l1[j+1]  = l1[j+1] , l1[j]
print(l1)
"""

# lambda : 

"""a =sorted(l1,key=lambda x :x[0])
print(a)
"""
"""
1. Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""