# tuple :  immutable sequence  ==> can't be changed

"""
t1 =(1,2,3,4,5,6,"ram",89.90,6j)
print(t1)
print(type(t1))
"""

"""
t2=1,2,3,4,5,6,"ram",89.90,6j
print(t2)
print(type(t2))
"""

# built in function  :   len  min max sorted sum 

"""
t2=1,2,3,4,5,6,9.9,6
print(len(t2))
print(min(t2))
print(max(t2))
print(sorted(t2))
print(sum(t2))
"""

# slicing  : 
"""
t1=1,2,3,4,5,6,9.9,6

print(t1[6])

# t1[3]="manit"  # error bcz  tuple is immutable 
# print(t1)

print(t1[2:5])
print(t1[ :5])
print(t1[ 1: ])
print(t1[2:5 :2])
print(t1[ : : -1])
"""

#method : 


"""
t1=1,2,3,4,5,6,9.9,6
#  0 1 2 3 4 5 6   7 
print(t1.count(6))
print(t1.index(6))
print(t1.index(6,6,10))
"""

# adv : 

# convert tuple  into the list  : 
"""
input t1 =1,2,3,4,5,6,9.9,6
output  =  1,2,3,4,5,6,9.9,6 ,"manit"
"""
"""t1 =1,2,3,4,5,6,9.9,6
l1 =list(t1)
l1.append("manit")
print(tuple(l1))
"""

# tuple  in list  :

t1 =(1,2,3,[6,7,"manit"],99,100)

# t1 => 1 ==> index number 0 
#t1 =>2 ==> index number 1
#t1 =>3 ==> index number 2
#t1 =>[6,7,"manit"] ==> index number 3 ==>6 ==>index 0 7 ==>1  ==> manit 2
#t1 =>99 ==> index number 4
#t1 =>100 ==> index number 5

"""t1[3].append("devang")
print(t1)"""
"""t1[2].append(100)
print(t1)"""

t1[3][2]="satyam"
print(t1)
# dev  sat  div  har  jain 
#  2     2     2    2   2  
# 1.[6,7,"satyam","manit"]   2. [6,7,"satyam"]