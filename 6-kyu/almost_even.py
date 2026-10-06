def split_integer(num, parts):
    base = num // parts
    remainder = num % parts
    return [base] * (parts - remainder) + [base + 1] * remainder