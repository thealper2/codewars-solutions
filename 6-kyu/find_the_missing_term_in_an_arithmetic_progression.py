def find_missing(sequence):
    n = len(sequence)
    g1 = sequence[1] - sequence[0]
    g2 = sequence[2] - sequence[1]
    if abs(g1) <= abs(g2):
        d = g1
    else:
        d = g2
        
    for i in range(n - 1):
        if sequence[i + 1] - sequence[i] != d:
            return sequence[i] + d
        
    return None