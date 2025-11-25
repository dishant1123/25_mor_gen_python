# pip install matplotlib

import matplotlib.pyplot as plt 
import numpy as np
"""
graphical view of the data  : bar chart , line , histogram,pie etc 
"""
# line  plot :
"""x=[1,2,3,4,5]
y=[10,20,15,25,30]

plt.plot(x,y)  # line plot  ==> 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.grid(True)
plt.show()
"""

# bar plot :

"""x=["A","B","C","D","E"]
y=["apple","banana","orange","grape","watermelon"]
plt.bar(x,y)
plt.xlabel("seris")
plt.ylabel("fruit")
plt.title("Bar Plot")
plt.show()
"""

#histogram :

"""data =np.random.randn(1000)
plt.hist(data,bins=20,color="red")
plt.xlabel("value")
plt.ylabel("frequency")
plt.title("Histogram")
plt.grid(True)
plt.show()
"""

# pie chart :

data = [10,20,30,40,50]

plt.pie(data,labels=["apple","banana","orange","grape","watermelon"])
plt.title("Pie Chart")
plt.show()