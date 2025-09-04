# date time  module  : 

import  datetime as dt 


"""a= dt.datetime.now()
print(a)

b=dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(b)

c =dt.datetime.today()
print(c)
"""
"""d=dt.datetime(2015,9,2,4,45,30,2345)
print(d)
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)

f=dt.datetime.astimezone(d)
print(f)
"""
import time as t 

"""print(t.time())
print(t.asctime((2025, 9, 2, 10, 30, 0, 1, 245, -1)))
print(t.localtime())
"""
"""for i in range(10):
    t.sleep(1)
    print(i)
"""
import calendar as cal

# print(cal.calendar(2025))
# print(cal.month(2025,9))

from datetime import timedelta as td 

"""a =dt.datetime.now()
b=a+ td(days=5, hours=2, minutes=30, seconds=45)
print(b)
"""
"""
today_date =dt.datetime.today()
future_date =today_date+ td(days=365)

print(future_date)
"""

# packages : collection of modules

from package2 import calculations as cal ,satyam as sat 

print(cal.sum(90,34))
sat.s()
