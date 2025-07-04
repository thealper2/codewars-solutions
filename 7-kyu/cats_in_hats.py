def height(n):
    a = 2000000
    r = 1 / 2.5
    sum_series = a * (1 - r ** (n + 1)) / (1 - r)
    return "{0:.3f}".format(sum_series)
