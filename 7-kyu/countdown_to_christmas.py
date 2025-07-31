import datetime


def days_until_christmas(current_date):
    year = current_date.year
    christmas = datetime.date(year, 12, 25)
    delta = christmas - current_date
    if delta.days < 0:
        christmas = datetime.date(year + 1, 12, 25)
        delta = christmas - current_date

    return delta.days
