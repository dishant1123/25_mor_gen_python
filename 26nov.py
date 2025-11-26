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

# top 10 profitable  product : 
"""least_profit =df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
least_profit.plot(kind="bar")
plt.title("Top 10 profitable product")
plt.xlabel("product")
plt.ylabel("Profit")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
"""

# profit vs  discout scatter plot 

plt.figure(figsize=(10,5))
plt.scatter(df["Profit"],df["Discount"])
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.title("Profit vs Discount")
plt.show()

# task  :3  profit vs  sales scatter plot
# task :4 sub category wise  profit 

