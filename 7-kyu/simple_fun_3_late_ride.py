def late_ride(n):
    hours = n // 60
    minutes = n - (hours * 60)
    return sum([int(d) for d in str(hours)]) + sum([int(d) for d in str(minutes)])
