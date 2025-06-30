def number_to_pwr(number, p):
    n = 1
    for _ in range(p):
        n *= number

    return n
