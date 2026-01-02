# pip install matplotlib
"""
data visualization
"""
import matplotlib.pyplot as plt

"""x=[1,2,3,4]
y=[10,20,30,40]

plt.plot(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Line Plot")
plt.show()
"""

# bar chart : 
"""subjects =["Maths","Science","English","History"]
marks = [90,80,70,60]

plt.bar(subjects,marks)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Subjects Marks")
plt.show()
"""

# pie chart :

labels =["python","java","c++","c"]
sizes =[30,20,10,5]

plt.pie(sizes,labels=labels)
plt.title("Programming languges Version")
plt.show()