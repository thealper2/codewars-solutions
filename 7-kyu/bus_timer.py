def bus_timer(time):
    h, m = map(int, time.split(':'))
    if h < 6:
        if h == 5 and m > 55:
            return 70 - m
        
        return 355 - m - 60 * h
    else:
        if h == 23 and m > 55:
            return 415 - m
        
        if m <= 10:
            return 10 - m
        elif m <= 25:
            return 25 - m
        elif m <= 40:
            return 40 - m
        elif m <= 55:
            return 55 - m
        else:
            return 70 - m
