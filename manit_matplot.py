# pip install matplotlib
"""
data visualization
"""
import matplotlib.pyplot as plt
import pandas as pd 

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

"""labels =["python","java","c++","c"]
sizes =[30,20,10,5]

plt.pie(sizes,labels=labels)
plt.title("Programming languges Version")
plt.show()
"""

# histogram :

"""data =[10,20,20,28,35,40,40,40,50]

plt.hist(data,bins=6)
plt.title("Histogram")
plt.xlabel("values")
plt.ylabel("frequency")
plt.show()
"""

# scatter plot :

"""x=[1,2,3,4,5]
y=[5,7,8,10,12] 

plt.scatter(x,y)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Scatter Plot")
plt.show()
"""

# pandas with matplotlib : 

# top 10 movies pandas  by revenue: 
movies = pd.read_csv("movies.csv")
directors = pd.read_csv("directors.csv")

movies.drop(columns="Unnamed: 0",inplace=True)
directors.drop(columns="Unnamed: 0",inplace=True)

df =pd.merge(
    movies,
    directors,
    left_on="director_id",
    right_on="id",
    how="left"
)

# print(df)

# top 10 directors by  number  of  movies : 

"""top_10_directors =df.groupby("director_name")["title"].count().sort_values(ascending=False).head(10)
print(top_10_directors)

plt.figure(figsize=(10,5))
top_10_directors.plot(kind="bar")
plt.title("Top 10 Directors by Number of Movies")
plt.xlabel("Directors")
plt.ylabel("Number of Movies")
plt.xticks(rotation=35)
plt.show()

"""

# miltiple  line graph  : 

year_data =df.groupby("year")[["budget","revenue"]].mean() 
# print(year_data)

plt.figure()
plt.plot(year_data.index,year_data["budget"],color="blue")
plt.plot(year_data.index,year_data["revenue"],color="red")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.title("Budget vs Revenue") 
plt.legend(["Budget","Revenue"])
plt.show()
