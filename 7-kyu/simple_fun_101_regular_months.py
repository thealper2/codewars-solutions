import datetime


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    else:
        return year % 400 == 0

    
def regular_months(currMonth):
    month, year = map(int, currMonth.split('-'))
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    current_month = month
    current_year = year
    while True:
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
        if current_month == 2 and is_leap_year(current_year):
            days = 29
        else:
            days = month_lengths[current_month-1]
        first_day = datetime.date(current_year, current_month, 1).weekday()
        if first_day == 0:
            return f"{current_month:02d}-{current_year}"
