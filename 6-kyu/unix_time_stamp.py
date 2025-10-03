def time_stamp(date):
    year, month, day, hour, minute, second = date
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    for y in range(1970, year):
        total_days += 365
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            total_days += 1
    
    for m in range(1, month):
        total_days += month_days[m-1]
        if m == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            total_days += 1
    
    total_days += day - 1
    total_seconds = total_days * 86400 + hour * 3600 + minute * 60 + second
    return total_seconds
