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

top_10 =df[df["year"] ==2007].sort_values(by="gdp_cap",ascending=False).head(10)
print(top_10)

# bottom 10 countires with  lowest gdp per capita in 2002 
 