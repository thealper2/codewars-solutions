def time_per_day(lst):
    total = 0
    for l in lst:
        total += l[0] * 45 * l[1]
            
    return round(total / (5 * 60 * 60), 2)
