def number_increasing(n):
    return n % 5 != 0 and (n > 22 or not (n % 5 == 2 or n == 4))