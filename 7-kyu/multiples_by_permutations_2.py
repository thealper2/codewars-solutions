def find_lowest_int(k):
    k2 = k + 1
    n = 1
    while True:
        prod1 = k * n
        prod2 = k2 * n

        if sorted(str(prod1)) == sorted(str(prod2)):
            return n

        n += 1
