# read mode csv file  open : 

import csv 

"""with open ("data.csv","r") as file :
    reader = csv.reader(file)
    for i in reader :
        print(i)
"""
"""with open ("data.csv","r") as file :
    reader = csv.DictReader(file)
    for i in reader :
        print(i)
"""

# write  mode csv file open  : 

"""
with open ("data2.csv","w",newline='') as file :
    writer =csv.writer(file)
    writer.writerow(['name','age','city'])
    writer.writerow(['satyam','20','ahm'])
    writer.writerow(['jainish','19','gandhinagar'])
    writer.writerow(['purvesh','21','delhi'])
    
"""    
    
"""with open ("data3.csv","w",newline='') as file :
    filedname=['name','age','city']
    writer = csv.DictWriter(file,fieldnames=filedname)
    
    writer.writeheader()
    writer.writerow({'name':'satyam','age':'20','city':'ahm'})
    writer.writerow({'name':'jainish','age':'19','city':'gandhinagar'})
    writer.writerow({'name':'purvesh','age':'21','city':'delhi'})
"""
# append  mode csv file open : 
with open ("data3.csv","a",newline='') as file :
    writer = csv.writer(file)
    
    writer.writerow(['raj','22','Mumbai'])

