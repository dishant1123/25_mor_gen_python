# set : mutable  and  unordered collection of unique elements, no repeation allowed in set.

"""
s1={"ram",1,2,3,4,5,6,7,8,9,10,1,2,"manit"}
print(s1)
print(type(s1))
"""

# duplicate remove  element in list : 

"""
l1=[1,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10]
s1=set(l1)
print(list(s1))
"""

# built in function  :  len min max sorted sum 

"""
s1={112,2,3,4,5,6,7,8,9,10,1,2}
print(len(s1))
print(min(s1))
print(max(s1))
print(sum(s1))
print(sorted(s1))  # asc to desc order
"""
# slicing  : 

"""
s1={112,2,3,4,5,6,7,8,9,10,1,2}    
print(s1[5])  # no slicing  in set bcz  of  unordered collection
"""
# method : 
# s1={112,2,3,4,5,6,7,8,9,10}    

"""
s1.add(123)
print(s1)

s1.clear()
print(s1)
"""
"""s2=set()
print(s2)
print(type(s2))
"""

"""
s2 =s1.copy()
print(s2)
"""

# s1={1,2,3,4}
# s2={2,4,5}
# s3={1,2,3,4,5,6,7,8}

"""
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
"""

"""
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
"""
"""
print(s1.difference(s2))
print(s1)
s1.difference_update(s2)
print(s1)
"""

"""print(s1.symmetric_difference(s2))
print(s1)
s1.symmetric_difference_update(s2)
print(s1)
"""

# super set , disjoint set , sub-set :

"""
s1={1,2,3,4}
s2={1,2,3,4,5,6,90}
s3={1,2,3,4,5,6,7,8}
"""

# print(s1.isdisjoint(s2))  # bool
# print(s1.issubset(s2))  # bool

# print(s3.issuperset(s1))

s1={112,2,3,4,5,6,7,8,9,10}    

"""
s1.pop()
print(s1)
"""
"""s1.remove(112)
print(s1)
"""

"""s1.discard(1112)
print(s1)
"""
"""s2={"devang","manit"}
s1.update(s2)
print(s1)
"""

# frozenset : immutable  and  unordered collection of unique elements, no repeation allowed in frozenset.

fz=frozenset({"ram",1,2,3,4,5,6,7,7,"manit"})
print(fz)
print(type(fz))

# method : 

