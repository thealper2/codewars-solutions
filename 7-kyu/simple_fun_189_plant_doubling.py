def plant_doubling(n):
    if n == 0:
        return 0

    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = n // 2

    return count
