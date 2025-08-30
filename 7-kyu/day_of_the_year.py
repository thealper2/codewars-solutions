import datetime


def to_day_of_year(date):
    day, month, year = date
    return datetime.date(year, month, day).timetuple().tm_yday
