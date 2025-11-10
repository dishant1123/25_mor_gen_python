import  pandas as pd 
# filter  , sort : 

#SQL  : filter  ==> where    sort ==> order by asc ,desc 

# select * from  mckinsey where continent = 'asia'

df =pd.read_csv('mckinsey.csv')
# print(df)

# print continent =asia  using  filter  

"""
asia =df[df["continent"]=="Asia"].head(50)
print(asia)
"""
# contries with  life_exp above 75 in 2007   ==> and  ==> &   or ==> | 

"""
life_exp_high =df[(df["year"]==2007) | (df["life_exp"]>75)] 
print(life_exp_high)
"""

# top 10 countires with highest GDP per capital in 2007 

"""top_10 =df[df["year"] ==2007].sort_values(by="gdp_cap",ascending=False).head(10)
print(top_10)
"""
#task  :1  bottom 10 countires with  lowest gdp per capita in 2002 
# task  :2  Countries with moderate GDP per capita between 10,000 and 20,000

# task :3 Highest GDP per capita in Africa before 1990

africa =df[(df["continent"]=="Africa") & (df["year"] < 1990)].sort_values(by="gdp_cap",ascending=False).head(10)
print(africa)


# task  :4  Sort by continent, then by GDP per capita within each continent

# task  :5 In 2007, sort countries by life expectancy

# task  :6 Top 5 Richest Asian Countries in 2007 

# task  :7 Longest-Living Countries (Global, 2007)