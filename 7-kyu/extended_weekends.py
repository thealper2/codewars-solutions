import calendar
from datetime import date


def solve(start_year, end_year):
    extended_months = []
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if calendar.monthrange(year, month)[1] == 31:
                if date(year, month, 1).weekday() == 4:
                    extended_months.append((year, month))
    
    if not extended_months:
        return ("", "", 0)
    
    extended_months.sort()
    first = extended_months[0]
    last = extended_months[-1]
    first_month_name = month_names[first[1] - 1]
    last_month_name = month_names[last[1] - 1]
    count = len(extended_months)
    
    return (first_month_name, last_month_name, count)
