def rounding(n, m):
    lower = (n // m) * m
    upper = lower + m

    diff_lower = n - lower
    diff_upper = upper - n

    if diff_lower < diff_upper:
        return lower
    elif diff_upper < diff_lower:
        return upper
    else:
        return n
