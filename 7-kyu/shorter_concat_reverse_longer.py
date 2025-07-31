def shorter_reverse_longer(a, b):
    n_a, n_b = len(a), len(b)
    if n_a >= n_b:
        return b + a[::-1] + b

    return a + b[::-1] + a
