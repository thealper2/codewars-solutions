import datetime


def count_days(d):
    now = datetime.datetime.now()
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if d.year == now.year and d.month == now.month and d.day == now.day:
        return "Today is the day!"
    t = d - now
    if t.days < 0:
        return "The day is in the past!"
    x = 24 * 60 * 60
    k = 1 if t.seconds > x / 2 else 0
    return f'{t.days + k} days'