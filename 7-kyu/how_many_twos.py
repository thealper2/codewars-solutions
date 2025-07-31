def two_count(n):
    count = 0
    while n % 2 == 0 and n != 0:
        count += 1
        n = n // 2

    return count
