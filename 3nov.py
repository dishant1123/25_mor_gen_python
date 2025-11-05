import  numpy as np
# loadtxt() :  clean 

"""
marks = np.loadtxt("marks.txt",dtype=int)
print("students marks  :\n",marks)

avg = np.mean(marks[:,1: ],axis =1)
print("average marks  :\n",avg)
"""

# genfromtxt() : 

"""
student= np.genfromtxt("student.csv",delimiter=",",skip_header=1,filling_values= 0,dtype=float)
print("student data  :\n",student)

avg =np.mean(student[:,1 :],axis=1)
print("average of names  :\n",avg)
"""
a=np.genfromtxt("fitbit_user.txt",dtype=None,delimiter=",")
print(a)
# print(len(a))
# print(np.ndim(a))
# print(a.shape)
# print(np.array(a))

# print(a[0 : 5])

"""
Print number of days user was sedantary (< 5000 steps), low active (5000 to 7499 steps), somewhat active (7500 to 9999 steps) and active (10k to 12499 steps).
"""

# print(a[: ,1])

# a= np.array(a)
# print(a[:,1])
# steps = a[:,1]
# print(steps)
