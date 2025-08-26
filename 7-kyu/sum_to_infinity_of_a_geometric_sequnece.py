def sum_to_infinity(sequence):
    if len(sequence) < 2:
        return "No Solutions"
    
    a = sequence[0]
    r = sequence[1] / sequence[0]
    
    if not (-1 < r < 1):
        return "No Solutions"
    
    sum_inf = a / (1 - r)
    return round(sum_inf, 3)
