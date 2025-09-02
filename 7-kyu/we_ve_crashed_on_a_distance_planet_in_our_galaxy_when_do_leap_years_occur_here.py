def is_leap_year(d, y):
    fractional = d - int(d)
    if fractional == 0:
        return False
    
    cycle = 1 / fractional
    return y % int(cycle) == 0
