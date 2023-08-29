"""
9. Take two datetimes from user start_time and end_time. 
Calculates the difference between start_time and end_time by removing night intervals (12 AM to 6 AM). 
(Hint: You can use python intervals module)         
2023-08-30 7:09:59.999999
"""
from datetime import datetime, time, timedelta

start_time = datetime.strptime(
    input(
        "Enter Start time in format of YYYY-MM-DD hh:mm:ss.milisecs : ",
    ),
    "%Y-%m-%d %H:%M:%S.%f",
)
end_time = datetime.strptime(
    input(
        "Enter End time in format of YYYY-MM-DD hh:mm:ss.milisecs : ",
    ),
    "%Y-%m-%d %H:%M:%S.%f",
)

t2 = timedelta(
    hours=int(start_time.time().hour),
    minutes=int(start_time.time().minute),
    seconds=int(start_time.time().second),
    microseconds=int(start_time.time().microsecond),
)

t3 = timedelta(
    hours=int(end_time.time().hour),
    minutes=int(end_time.time().minute),
    seconds=int(end_time.time().second),
    microseconds=int(end_time.time().microsecond),
)


diff = end_time - start_time  # timedelta object



if diff.days < 1:
    
    if t2 > timedelta(hours=6, minutes=0, seconds=0, microseconds=0):
        day_first = timedelta(hours=23, minutes=59, seconds=59, microseconds=999999) - t2 
    else:
        day_first = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)

    print('day_first',day_first)
    
    if t3 > timedelta(hours=6, minutes=0, seconds=0, microseconds=0):
        day_last = t3 - timedelta(hours=6, minutes=0, seconds=0, microseconds=0)
    else:
        day_last = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)

    print('day_last',day_last)        

    # if the difference is less than a day then we need to check for hour and minute differences as well
    x = timedelta(days=(diff.days )).total_seconds()/3600
    print('x',x)
    y = timedelta(hours=x * 0.75)
    print('y',y)
    z = y + day_last + day_first
    print('z',z)

elif diff.days > 2:
    diffTime_1 = timedelta(hours=23, minutes=59, seconds=59, microseconds=99999) - t2
    print("diffTime_1", diffTime_1)
    if diffTime_1 < timedelta(hours=18, minutes=0, seconds=0, microseconds=0):
        print("diffTime_1", diffTime_1)
        day_first = diffTime_1
    else:
        day_first = timedelta(hours=18, minutes=0, seconds=0, microseconds=0)


    if t3 > timedelta(hours=6, minutes=0, seconds=0, microseconds=0):
        day_last = t3 - timedelta(hours=6, minutes=0, seconds=0, microseconds=0)
    else:
        day_last = timedelta(hours=0, minutes=0, seconds=0, microseconds=0)


    day_diff = day_first + day_last
    print("day_diff", day_diff.days)
    print(day_first, day_last)

    print(timedelta(days=(diff.days - 2)).total_seconds()/3600)

    x = timedelta(days=(diff.days - 2)).total_seconds()/3600

    print('x',x)
    y = timedelta(hours=x * 0.75)
    print('y',y)
    z = y + day_first + day_last
    print('z',z)

