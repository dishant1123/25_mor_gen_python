"""
matplotlib ==> lib use for plotting , graphs , visualization

pip install matplotlib 
"""

import matplotlib.pyplot as plt 
import pandas as pd

"""x=[1,2,3,4,5,6,7,8,9,10]
y=[20,10,25,35,89,90,23,45,67,5]

plt.figure(figsize=(5,5))  # box area 
plt.plot(x,y)   # plot  ==> line graphs 
plt.title("line graphs")  #==> heading  
plt.xlabel("x axis")  # ==> x label 
plt.ylabel("y axis")  # ==> y label
plt.show()   # show the graph
"""
# use line graphs :  strock price , temperature  over days , sales over months , website traffic.

# bar graphs : category , sales , profit , stock price  comparison : 

"""students =["manit","dipak","deep","mahesh","suresh"]
marks = [90,99,78,65,45]

plt.figure(figsize=(5,5))
plt.bar(students,marks)
plt.title("bar graphs")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()
"""

# horizontal bar graphs :

"""brands = ["apple","samsung","nokia","huawei","sony"]
sales = [90 ,45,60,35,55] 

plt.figure(figsize=(5,5))
plt.barh(brands,sales)
plt.title("horizontal bar graphs")
plt.xlabel("sales")
plt.ylabel("brands")
plt.show()
"""

# top 10  directors by  number  of  movies : 

movies = pd.read_csv("movies.csv")
directors = pd.read_csv("directors.csv")

# print(movies.head())
# print(directors.head())

movies.drop(columns="Unnamed: 0",inplace=True)
directors.drop(columns="Unnamed: 0",inplace=True)

df = pd.merge(
    movies,
    directors, 
    left_on="director_id",
    right_on="id", 
    how="left"
)

# print(df.head())


top_10_directors =df.groupby("director_name")["title"].count().sort_values(ascending=False).head(10)
print(top_10_directors)

plt.figure(figsize=(10,5))
top_10_directors.plot(kind="bar")
plt.title("Top 10 Directors by Number of Movies")
plt.xlabel("Directors")
plt.ylabel("Number of Movies")
plt.xticks(rotation=35)
plt.show()