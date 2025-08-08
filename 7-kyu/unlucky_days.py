import datetime

def unlucky_days(year):
    return sum(datetime.date(year, month, 13).weekday() == 4 for month in range(1, 13))
