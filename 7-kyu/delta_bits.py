def convert_bits(a, b):
    count = 0
    while a >= 1 or b >= 1:
        if a % 2 != b % 2:
            count += 1

        a //= 2
        b //= 2

    return count
