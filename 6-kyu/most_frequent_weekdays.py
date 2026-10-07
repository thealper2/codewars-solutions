import datetime


def most_frequent_days(year):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    counts = [0] * 7
    d = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    while d <= end:
        counts[d.weekday()] += 1
        d += datetime.timedelta(days=1)
    
    m = max(counts)
    return [days[i] for i in range(7) if counts[i] == m]