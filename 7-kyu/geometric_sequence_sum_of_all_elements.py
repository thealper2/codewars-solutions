def geometric_sequence_sum(a, r, n):
    return sum(a * (r**i) for i in range(n))
