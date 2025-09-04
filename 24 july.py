# list  :  mutable  ==>  changes in list 
# slicing : 

"""
l1=     [1,2,3,4,5,89,90,91,45,66,77,88]
#index:  0 1 2 3 4 5   6
print(l1[2:5])  # 2 start index  5 ending index 

print(l1[2:7:2])  # 2 start index  5 ending index  2 step
print(l1[ : : -1])   # 
"""

# method  : 
l1= [91,2,3,4,5,89,90,91,45,66,77,88]

"""l1.append(130)
print(l1)
"""
"""l1.insert(2,"satyam")
print(l1)"""

"""l1.clear()
print(l1)
"""

"""
l2 = l1.copy()
print("l2=",l2)
"""

"""
l2 =["banana","apple","mango","orange","pineapple"]
l1.extend(l2)
print(l1)
"""

"""
print(l1.index(91))
print(l1.index(91,1,10))
"""

# print(l1.count(91))

"""l1.pop(5)  # index num wise remove 
print(l1)
"""
"""l1.remove(3)
print(l1)
"""

"""l1.sort()
print(l1)
"""

"""
l1.reverse()
print(l1)
"""
"""
task  : 1
ask user to enter the list element and store in to list  and  print  odd even sum. 

5 
1 2 3 4 5 
l1=[1,2,3,4,5]  


"""

"""n =int(input("enter the number of elements"))
odd=0
even=0
l2=[]
for i in range(n):
    num=int(input("enter the element  : "))
    l2.append(num)
print(l2)  # [1,2,3,4,5,6]

for i in l2 : 
    if i % 2==0:
        even+=i 
    else :
        odd+=i
print("odd sum is  : ",odd)
print("even sum is  : ",even)
"""

#task 2 : 
"""
ask user to enter the list element and store in to list  and  printsecond largest element in list. 

input : l1 = [1,2,4,55,6,7,99,5]
second largest : 55
"""

