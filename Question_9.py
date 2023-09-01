"""
9. Take two datetimes from user start_time and end_time. 
Calculates the difference between start_time and end_time by removing night intervals (12 AM to 6 AM). 
(Hint: You can use python intervals module)         
"""


import portion as P
import datetime as dt


# function to convert a datetime to a number of minutes since epoch
def datetime_to_minutes(datetime):
    epoch = dt.datetime.utcfromtimestamp(0)
    return (datetime - epoch).total_seconds() / 60


# function to convert a number of minutes since epoch to a datetime
def minutes_to_datetime(minutes):
    epoch = dt.datetime.utcfromtimestamp(0)
    return epoch + dt.timedelta(minutes=minutes)


start_time_str = input("Enter start time (YYYY-MM-DD HH:MM): ")
end_time_str = input("Enter end time (YYYY-MM-DD HH:MM): ")

start_time = dt.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
end_time = dt.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

start_minutes = datetime_to_minutes(start_time)
end_minutes = datetime_to_minutes(end_time)

whole_interval = P.closed(start_minutes, end_minutes)

night_interval = P.empty()

# Loop through each day in the time span
for day in range(start_time.date().toordinal(), end_time.date().toordinal() + 1):
    date = dt.date.fromordinal(day)

    night_start = datetime_to_minutes(dt.datetime.combine(date, dt.time(0, 0)))
    night_end = datetime_to_minutes(dt.datetime.combine(date, dt.time(6, 0)))

    night_interval = night_interval | P.closed(night_start, night_end)

    daytime_interval = whole_interval - night_interval

    # Sum up the lengths of all atomic intervals in the daytime interval
    daytime_minutes = sum(
        interval.upper - interval.lower for interval in daytime_interval
    )

    daytime_delta = dt.timedelta(minutes=daytime_minutes)

print("Result ->", daytime_delta)
