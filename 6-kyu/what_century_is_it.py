def what_century(year):
    y = int(year)
    century = (y - 1) // 100 + 1
    if 11 <= century % 100 <= 13:
        suffix = 'th'
    elif century % 10 == 1:
        suffix = 'st'
    elif century % 10 == 2:
        suffix = 'nd'
    elif century % 10 == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    return f"{century}{suffix}"