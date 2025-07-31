def count_zeros(x):
    zero_count = 0
    for number in range(1, x + 1):
        zero_count += str(number).count("0")
    return zero_count
