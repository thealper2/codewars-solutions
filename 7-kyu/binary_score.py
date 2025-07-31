def score(n):
    if n == 0:
        return 0

    bit_length = n.bit_length()
    return (1 << bit_length) - 1
