def sum_or_product(array, n):
    a = sorted(array)
    s = sum(a[-n:])
    p = 1
    for x in a[:n]: p *= x
    return 'sum' if s > p else 'product' if p > s else 'same'
