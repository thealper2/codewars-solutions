def days_represented(trips):
    represented_days = set()
    for arrival, departure in trips:
        represented_days.update(range(arrival, departure + 1))
        
    return len(represented_days)
