def min_value(digits):
    unique_digits = sorted(list(set(digits)))
    return int(''.join(map(str, unique_digits)))