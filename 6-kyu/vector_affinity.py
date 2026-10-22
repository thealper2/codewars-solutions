def vector_affinity(a, b):
    if len(a) == 0 and len(b) == 0:
        return 1.0

    n = max(len(a), len(b))
    matches = sum(1 for x, y in zip(a, b) if x == y)
    return matches / n