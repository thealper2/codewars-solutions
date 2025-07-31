def split_numbers(n: int) -> tuple[int, int]:
    a = 0
    b = 0
    bit_pos = 0
    count = 0

    while n > 0:
        if n & 1:
            if count % 2 == 0:
                a |= 1 << bit_pos
            else:
                b |= 1 << bit_pos
            count += 1
        n >>= 1
        bit_pos += 1

    return (a, b)
