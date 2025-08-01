def range_bit_count(a, b):
    return sum([item.bit_count() for item in range(a, b + 1)])
