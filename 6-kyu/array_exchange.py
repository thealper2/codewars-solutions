def exchange_with(a, b):
    new_a = list(reversed(b))
    new_b = list(reversed(a))
    a[:] = new_a
    b[:] = new_b