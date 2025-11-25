# group by , join , filter  : 

import pandas as pd
import  numpy as np 


# task:1.Total Revenue Earned by Each Director :

movies =pd.read_csv('movies.csv')
directors = pd.read_csv('directors.csv')

df =movies.merge(directors,left_on="director_id",right_on="id",how="left")
# print(df)

"""
revenue_by_director =df.groupby("director_name")['revenue'].sum().head(20)
print(revenue_by_director)
"""

# task :2 Total revenue per director (only movies after 2010) 

# total_revenue_after_2010 =(df[df['year']>2010].groupby("director_name")['revenue'].sum().reset_index())
# print(total_revenue_after_2010)

"""total_revenue_per_director_oneliner = (
    df[df['year'] > 2010]
    .groupby('director_name')['revenue']
    .sum()
    .reset_index(name='Total_Revenue_Post_2010')
)

print(total_revenue_per_director_oneliner)
"""

recent_movies_df = df[df['year'] > 2010]
total_revenue_and_year_per_director = recent_movies_df.groupby('director_name').agg(
    Total_Revenue_Post_2010=('revenue', 'sum'),
    Latest_Movie_Year=('year', 'max')
).reset_index()

# print(total_revenue_and_year_per_director)

# task :3 Average vote of movies per director, only movies with > 5000 votes.

#task  :4. Total budget per month (only high-budget movies > 200M) 

# task  :5 Count of movies per director (only directors with ≥ 3 movies)  

# task :6 Directors sorted by total revenue (highest first) 

# task  :7 Directors with total revenue > 1B sorted descending


#task  :4. Total budget per month (only high-budget movies > 200M) 

"""
result = (df[df["budget"]>200000000].groupby('month')['budget'].sum())
print(result)
"""

# task  :5 Count of movies per director (only directors with ≥ 3 movies)  

"""
movie_count = df.groupby("director_name")['title'].count().reset_index()
# print(movie_count)
result = movie_count[movie_count['title']>5]
print(result)
"""
# task:5.1 ==>count  of movies  per director  for  only male or female  

# task :6 Directors sorted by total revenue (highest first) 

result = df.groupby("director_name")["revenue"].sum().reset_index().sort_values(by="revenue",ascending=False)
print(result)
