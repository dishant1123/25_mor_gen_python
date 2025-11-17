import pandas as pd
import numpy as np

# group by  : 

# df = pd.read_csv('directors.csv')
# print(df)

# df.drop(columns="Unnamed: 0",inplace=True)
# print(df)

# Count how many movies each director has directed
"""
print(df.groupby("director_name").size().head(20))
"""
# Group directors by gender and count :

"""
print(df.groupby(["gender"])["director_name"].count().head(20))
"""

#Group by gender and list all directors in each group
"""
print(df.groupby(["gender"])["director_name"].apply(list).head(5))
"""

# Group by gender and filter groups with more than 200 directors

"""
print(df.groupby(["gender"]).filter(lambda x : len(x) >200))
# female  : 150  male  : 1574 
"""

#Group by director_name and filter directors who appear more than once.

movies=pd.read_csv('movies.csv')
directors=pd.read_csv('directors.csv')
# print(df.groupby(["year"]).count())

df = movies.merge(directors, left_on="director_id", right_on="id", how="left")

titles = df.groupby("director_id")["title"].apply(list)
names = df.groupby("director_id")["director_name"].first()

result = titles.to_frame().join(names).head(20)
print(result)
