def tidyNumber(n):
    i = 0
    prev = None
    while 10**i <= n:
        d = n // 10**i % 10
        if prev is not None and d > prev:
            return False

        prev = d
        i += 1

    return True
