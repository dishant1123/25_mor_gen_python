# while loop  : 
"""
syntax : 

i=intial value 

while  con :
    print()
    inc/dec i+=1 

"""
# break ,continue , pass 

#break : 
"""
for i in range(1,10):
    if i==5 :
        break 
    print(i)
"""

# continue :

"""
for i in range(1,10):
    if i==5 :
        continue 
    print(i)
"""
#pass :
"""
for i in range(1,10):
    if i==5 :
        pass 
    print(i)
"""

# 1-100 : 

"""i=0 
while i <=100 :
    print(i,end=" ")
    i+=2
"""

# prime  perfect amg  pelindrome twin perfect strong  : 

#strong : 
"""
145 : 
each  digit  :   1! =1  4! =24  5! =120 
sum  = 1+24 +120 =145

"""
"""n=int(input("enter the  number : ")) 
sum =0 
digit = len(str(n))
temp =n 
while n >0 :  # 145 > 0 
    r=  n %10     # 145 %10 =5 
    fact =1 
    while r >0 :  # 
        fact = fact *r
        r-=1  
    sum = sum +fact 
    n= n//10 

if sum ==temp :
    print("strong")
    
"""

# prime  perfect amg  pelindrome twin perfect strong    nested  while : 

"""start=  int(input("enter the start : "))  #100 
end =  int(input("enter the end : "))  #1000 

i=start  # i =100 

while i<=end :   # 100 <=1000 
    sum =0 
    digit = len(str(i))
    temp =i 
    while  temp >0 :
        r= temp %10 
        sum = sum + pow(r,digit)
        temp= temp//10
    if  sum == i : 
        print(i)
    i+=1
"""

# pattern  using while  : 
"""
        *               * 
       * *             * *
      * * *           *   *
     * * * *         *     *
    * * * * *       *       *
     * * * *         *     *
      * * *           *   *
       * *             * *
        *               *   
"""

"""i =1 
while i<5 :
    k=5
    while  k>i:
        print(" ",end="")
        k-=1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1
i =1 
while i<=5 :
    k=1
    while  k<i:
        print(" ",end="")
        k+=1
    j=5
    while j>=i:
        print("*",end=" ")
        j-=1
    print()
    i+=1
"""