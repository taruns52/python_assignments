"""
9. Take two datetimes from user start_time and end_time. 
Calculates the difference between start_time and end_time by removing night intervals (12 AM to 6 AM). 
(Hint: You can use python intervals module)         
"""

'''
Approach:

We will get two inputs as start time timestamp and end time timestamp,

So lets divide this time interval in three parts :

1)Start Day
2)Intermediate Days
3)Last Days

Here calculation for intermediate days is pretty straight forward as we just have to subtract 6 hours from every intermedite day
For Start we have to check and count the valid hours same goes for Last Day
At last the summation of start day hrs, last day hrs, intermediate days hrs will give us desired result.
'''


from datetime import datetime, timedelta

# function to convert days to hours and reduce it to 75%
# as 6 hrs are to be removed from a 24 hour interval and cout only 18 hrs from a full day
# and 18 hrs are 75% of 24 hrs
def days_to_hours(diff, i):
    x = (
        timedelta(days=(diff.days - i)).total_seconds() / 3600
    )  # days to hours conversion
    y = timedelta(hours=x * 0.75)
    return y


# Demo input : 2023-08-25 11:09
start_time = datetime.strptime(
    input(
        "Enter Start time in format of YYYY-MM-DD hh:mm : ",
    ),
    "%Y-%m-%d %H:%M",
)
end_time = datetime.strptime(
    input(
        "Enter End time in format of YYYY-MM-DD hh:mm : ",
    ),
    "%Y-%m-%d %H:%M",
)
start_date = start_time.date()
end_date = end_time.date()

diff = end_date - start_date  # timedelta object
print("Difference between two days", diff)

# Start time after exluding date from input start timestamp
start_time = timedelta(
    hours=int(start_time.time().hour),
    minutes=int(start_time.time().minute),
    seconds=int(start_time.time().second),
    microseconds=int(start_time.time().microsecond),
)

# end time after exluding date from input end timestamp
end_time = timedelta(
    hours=int(end_time.time().hour),
    minutes=int(end_time.time().minute),
    seconds=int(end_time.time().second),
    microseconds=int(end_time.time().microsecond),
)

# required variables
night_end = timedelta(hours=6)
night_start = timedelta(hours=0)
day_end = timedelta(hours=23, minutes=59, seconds=59, microseconds=999999)

# if total diffrence between input start and end time stamp is less than 24 hrs
if diff.days < 1:
    if start_date == end_date:
        if start_time > night_end:
            result = end_time - start_time
        else:
            result = end_time - night_end

    else:
        if start_time > night_end:
            day_first = day_end - start_time
        else:
            day_first = day_end - night_end

        if end_time > night_end:
            day_last = end_time - night_end
        else:
            day_last = night_start

    z = days_to_hours(diff, 0) + day_first + day_last
    print("Final Result :-> ", z)

# if total diffrence between input start and end time stamp is <= 2
elif diff.days <= 2:
    if start_time > night_end:
        day_first = day_end - start_time
    else:
        day_first = day_end - night_end

    if end_time > night_end:
        day_last = end_time - night_end
    else:
        day_last = night_start

    z = days_to_hours(diff, 1) + day_first + day_last
    print("Final Result :-> ", z)

# if total diffrence between input start and end time stamp is > 2
elif diff.days > 2:
    if start_time > night_end:
        day_first = day_end - start_time
    else:
        day_first = day_end - night_end

    if end_time > night_end:
        day_last = end_time - night_end
    else:
        day_last = night_start

    z = days_to_hours(diff, 2) + day_first + day_last
    print("Final Result :-> ", z)
