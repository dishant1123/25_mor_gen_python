# prime  ,perfect, amg reverse pelindrome twin  strong number : 

"""
prime number  :  2 factors : 1 , number itself
4 factors : 1,2,4 ==> no prime 
5 factors : 1,5 ==> prime  
"""

"""
n =int(input("enter the number  : "))  # 4
count=0 

for i in range (1,n+1) :  # 5,5
    if  n % i ==0 :   # 4 % 4 ==0 
        count+=1     # count =3 
if count ==2 :
    print("prime number")
else :
    print("not prime number")
"""
# perfect  number  : 
"""
6 factors : 1,2,3,6 == > 6 excluding  : sum = 1+2+3 = 6 perfect number  
28 factors :1,2,4,7,14 ,28 ==> 28 excluding  : sum = 1+2+4+7+14 = 28 perfect number
100 factors :1,2,4,5,10,20,25,50,100 ==> 100 excluding  : sum = 1+2+4+5+10+20+25+50 =       117 not perfect number

"""
"""
n =int(input("enter the number  : "))  # 4
sum=0 

for i in range (1,n) :  # 5,5
    if  n % i ==0 :   # 4 % 4 ==0 
        sum =sum +i    # count =3 
if sum ==n :
    print("perfect number")
else :
    print("not prime number")
"""

# amg  : 
"""
153 : ==> 3 

1*1*1 =1 
5*5*5 =125
3*3*3 =27
sum = 1 +125 +27 =153

370 : 3 digit 

3*3*3 =27
7*7*7 =343 
0*0*0 =0
amg   
"""
"""
n=int(input("enter the  number : "))  #153 
digit = len(str(n))  # 3 
sum=0
temp=n   # temp =153 
for i in range (1,digit+1):  # 3,4 
    r= temp %10             # r = 1 %10 =1  
    sum = sum + pow(r,digit) # sum = 153 
    temp = temp//10         # temp  =0
if sum ==n:
    print("amg")
"""