import datetime


def day_of_week(date):
    d, m, y = map(int, date.split('/'))
    day = datetime.datetime(y, m, d)
    return day.strftime('%A')
