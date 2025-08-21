from datetime import datetime,timedelta


def seconds_ago(s, n):
    dt = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    result_dt = dt - timedelta(seconds=n)
    year = result_dt.year
    month = result_dt.month
    day = result_dt.day
    hour = result_dt.hour
    minute = result_dt.minute
    second = result_dt.second
    return f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
