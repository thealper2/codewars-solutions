def candles(m, n):
    total = 0
    leftovers = 0
    current = m

    while current > 0:
        total += current
        leftovers += current
        current = leftovers // n
        leftovers %= n

    return total
