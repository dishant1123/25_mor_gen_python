"""
file handling  : txt  

1. read : r ==> exiting  file  open  only  
2. write : w ==>new file create  +  write  + exiting  file  ==> overwrite  
3 .append :a==>new file create  +  write  + exiting  file  ==> append in last.

open  ==>  with open  
close ==> file.close()
"""
# write  : 
"""
with  open("satyam.txt","w") as file: 
    file.write("hello  satyam.\n")
    file.write('live in ahmedabad.\n')
    file.write("study in J.G.\n")
    file.write("food lover.\n")
    file.close()
"""

# write  mode  ==> open  exiting file  

"""
with  open("satyam.txt","w") as file:
    file.write("my brother name is  shivam.\n")
    file.write("study in indus clg")
"""

# append mode  : 
"""
with  open("purvesh.txt","a") as file: 
    file.write("hello  purvesh.\n")
    file.write('live in ahmedabad.\n')
    file.write("study in GNU.\n")
    file.write("IPO lover.\n")
    file.close()
"""
# append mode  ==> exiting  file  : 

"""with  open("purvesh.txt","a") as file: 
    file.write("dream to meet donald trump.\n")
    file.write('huge  property .\n')
    file.close()
"""

# read mode  : 

with open("purvesh.txt","r") as file:
    # context = file.read()  # all context read 
    # context = file.readline()  # only  first  line  read 
    context =file.readlines()
    print(context)

# task  : 
"""
ask user  to enter the  string  and print  the  seprate  file of vowel  and consonant.
input  :  my name is  satyam.
output  : 

vowel.txt = ae i aa 
consonant.txt = my n s stym


"""
