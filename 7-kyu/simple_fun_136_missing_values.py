from collections import defaultdict


def missing_values(seq):
    freq = defaultdict(int)
    for num in seq:
        freq[num] += 1

    x = None
    y = None
    for num, count in freq.items():
        if count == 1:
            x = num
        elif count == 2:
            y = num

    return x * x * y
