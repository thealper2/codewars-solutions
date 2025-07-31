def three_powers(n):
    if n < 3:
        return False

    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = n // 2
    return count <= 3
