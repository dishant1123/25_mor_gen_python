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

print(total_revenue_and_year_per_director)

# task :3 Average vote of movies per director, only movies with > 5000 votes.