def total_bill(s):
    red_plates = s.count('r')
    free = red_plates // 5
    total = (red_plates - free) * 2
    return total