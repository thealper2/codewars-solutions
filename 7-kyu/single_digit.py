def single_digit(n):
    while True:
        if n >= 10:
            n_c = n.bit_count()
            n = n_c
        else:
            return n
