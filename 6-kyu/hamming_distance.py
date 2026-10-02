def hamming(a,b):
    return sum(c1 != c2 for c1, c2 in zip(a, b))