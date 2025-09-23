# file  : 
"""
1.  r+ : read and write  both  == > write ==> letter  overwrite  
2.  w+ : write  and read both 
3.  a+ : append and read both  
"""

# r+ : exiting  file  open  only

"""
with  open("purvesh.txt","r+") as file:
    file.write("jainish patel.\n")
    file.write("study in JG.")
    file.seek(0)  # cursor  at  the  start  of  file
    context =file.read()
    print(context)
    file.close() 
"""    
# jainish patelrvesh. 
# w+ : new file 
"""
with open("jainish.txt","w+") as file:
    file.write("jainish patel.\n")
    file.write("study in JG.\n")
    file.write("football lover.")
    file.seek(0) 
    context =file.read()
    print(context)
    file.close()
"""

# w+ : exiting  file 

"""with open("satyam.txt","w+") as file:
    file.write("study in ROYAL.\n")
    file.write("live in nikol.\n")
    file.write("food lover.\n")
    file.seek(0)  # move  cursor  to  the  start  of  file
    file.write("best friend name is manit.\n")
    # context =file.read()
    # print(context)
    
    file.close()
"""    
   
# a+ : 

"""with open("jainish.txt","a+") as file:
    file.write("best friend name is satyam.\n")
    file.seek(0)
    file.write("he is  very intelligent.\n")
    file.seek(0)
    context =file.read()
    print(context)
    file.close()
"""

"""
task  :1 

bank  : 
start :25000 
1. deposit   : 10000 
2. withdraw  : 15000 
3. balance

purvesh.txt 
                    STATE BANK OF INDIA 
BRANCH : NIKOL                          ACCNO :7292000014352 
DATE : 25 SEPT 2020                     PAN   : AWSDS2345A 

                    TRANSACTIONS
DATE-TIME     AMOUNT      DR       CR       BALANCE 
23-9-2025                                   25000 
23-9-2025     10000               10000     35000 
23-9-2025     15000      15000              20000

date -time  module 
"""