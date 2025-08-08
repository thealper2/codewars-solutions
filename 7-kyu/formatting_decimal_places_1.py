def two_decimal_places(number):
    n = list(str(number))
    return float(''.join(n[:n.index('.')+3]))
