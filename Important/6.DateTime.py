import datetime
import pytz 

date1 = datetime.date(2022, 5,25)
print(date1)

today = datetime.date.today()
print(today.day)
print(today.weekday())  # 0-6
print(today.isoweekday())  # 1-7

#time deltas

tDelta = datetime.timedelta(days = 7)

print(today + tDelta) # date1 -+ date2 = timedelta

time= datetime.datetime(2017, 6,7, 12,54,30,1000) # all details y-d-m h-m-s

print(time) 

#  use pytz
