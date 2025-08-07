def find_squares(num):
    for a in range(num):
        a2 = a ** 2
        b2 = (a ** 2) - num
        b = b2 ** 0.5
        if a - b == 1:
            return f'{a2}-{b2}'
