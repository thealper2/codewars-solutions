def pofi(n):
    remainder = n % 4
    if remainder == 0:
        return '1'
    elif remainder == 1:
        return 'i'
    elif remainder == 2:
        return '-1'
    else:
        return '-i'
