# join  : 
"""l1=["my","name","is","manit","shah"]
# my name is manit shah.
s1=" ".join(l1)
print(s1)

"""
# strip , lstrip , rstrip :

"""s2="        happy vasuli divas        " 
print(s2)
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())
"""

s1="my name is manit shah."

"""
print(s1.startswith("my"))
print(s1.endswith("shah."))
"""
#prefix , suffix : 

"""
print(s1.removeprefix("my"))
print(s1.removeprefix("name"))
print(s1.removesuffix("shah."))
print(s1.removesuffix("manit"))
"""

# isalpha , isdigit , isalnum : 

s2="happyrakshabandhan78"
# print(s2.isalpha())  # string  ==> a to z
# print(s2.isalnum())

s3="\u3456790"
# print(s3.isdigit())  # only digit 0-9 
# print(s3.isdecimal())
# print('²'.isdigit())
# print('²'.isdecimal())  # not allowed superscripts


"""
print("123".isnumeric())
print('१२३'.isnumeric())       # True
print('½'.isnumeric())         # True
print('Ⅻ'.isnumeric())         # True (Roman numeral for 12)
print('²'.isnumeric())         # True
print('10.5'.isnumeric())   # dot/float not allowed 
"""

"""
Write a python program that take one input string and in output count the no of words,
Find No of letters in String,Find the longest word in the String.
For Example:-
Input:-This is the python program
Output:-No of Words=5
	    No of letters=26(including whitespace)
	    Longest Word=program

"""
"""
task  :2 take list from user append all element in list and print longest word in list  
         input : ["java", "python", "php","cpp","flutter"]
         output :  flutter

task  :4 take list from user append all element in list and print pelindorme word in list  
         input : ["java", "python", "php","cpp","flutter","maam"]
         output :  ['php','maam']

task  : 6 Write a Python program to count the number of strings from a given list of strings. 
	The string length is 2 or more and the first and last characters are the same.
	
	Sample List : ['abc', 'xyz', 'aba', '1221']
	Expected Result : 2

    
task  : 10 
	Write a Python program to find the length of a given list of non-empty strings.
	Input:
	['cat', 'car', 'fear', 'center']
	Output:
	[3, 3, 4, 6]
	Input:
	['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
	Output:
	[3, 3, 7, 5, 2, 4, 0]

task  : 11 Write a Python program to check, for each string in a given list, whether the 
last character is an isolated letter or not. 
Return True otherwise False.
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]


task : 12 
Write a Python program to find strings in a given list containing a given substring.
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
Input:
[(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
[]

task  : 13 
Write a Python program to find the length of a given list of non-empty strings.
	Input:
	['cat', 'car', 'fear', 'center']
	Output:
	[3, 3, 4, 6]
	Input:
	['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
	Output:
	[3, 3, 7, 5, 2, 4, 0]

"""

"""
task  :4 take list from user append all element in list and print pelindorme word in list  
         input : ["java", "python", "php","cpp","flutter","maam"]
         output :  ['php','maam']

"""

"""n=int(input("Enter the number of strings: "))

l1=[] 

for i in range(n):
    s1=input("enter the string  : ")
    l1.append(s1)
print(l1)
l2=[]
for i in l1:
    if i == i[ : : -1]:
        l2.append(i)
print(l2)
"""

l1=[('ca',('cat', 'car', 'fear', 'center'))]

for i in l1 :
    l2 =i[0]
    print(l2)
    l3=i[1]
    print(l3)
    result=[]
    for  j in l3 :
        if l2 in j :
            result.append(j)
    print(result)
