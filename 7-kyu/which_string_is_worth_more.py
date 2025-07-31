def highest_value(a, b):
    a_sum = sum([ord(c) for c in a])
    b_sum = sum([ord(c) for c in b])
    return a if a_sum >= b_sum else b
