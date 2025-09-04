#twin number  : 
"""
123 : 
each sum  = 1+2+3 =6 
each mul  = 1*2*3 =6
sum == mul  ==> twin  
"""
"""n=int(input("enter the number  : "))
sum =0 
mul =1 
digit =len(str(n))
for i in range(1,digit+1):
    r= n %10 
    sum =sum +r 
    mul = mul *r 
    n = n//10 
if sum == mul :
    print("twin number")
"""

# strong number  : 
"""
145 : 
each  factorial  : 1 = 1  4! = 4*3*2*1=24  5! = 5*4*3*2*1=120
sum = 1+120+24 =145 

"""
"""n=int(input("enter the  number  : "))  #145 
sum =0
digit =len(str(n))  # 3 
temp =n
for i in range (1,digit +1):  # 3,4   
    r = n %10   # r = 1 %10 =1 
    fact =1     # 1 
    for  j in range (1,r+1):  # 1,5
        fact =fact *j     #fact =1   
    sum =sum +fact     # sum =144 +1=145 
    n = n//10          # n =1 //10 =0 
if sum ==temp :
    print("strong number")
"""

# nested  loop  : 
"""
2 range  :  start 20  end  :100  

perfect number in range  : 
"""
"""start =int(input("enter the start  : "))  # 20
end =int(input("enter the end  : "))  # 100

for i in range(start,end+1):  # 20 ,101 
    count =0    # 0 
    for j in range(1,i+1):   # 1,21 
        if i % j ==0 :
            count +=1 
    if  count ==2 :
        print(i,end=" ")
"""