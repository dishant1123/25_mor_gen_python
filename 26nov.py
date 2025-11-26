import numpy as np
import  pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("sample_superstore1 copy.csv")
# print(df)

# profit by category : 

"""
plt.figure()
df.groupby("Category")["Profit"].sum().plot(kind="bar")
plt.xlabel("category")
plt.ylabel("Total profit")
plt.title("Profit by category")
plt.show()
"""
# top 10 staes by sales : 

"""plt.figure()
df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10).plot(kind="pie")
plt.title("Top 10 states by sales")
plt.show()
"""

# task :1 profit by segment :
# task :2 city wise  profit :
