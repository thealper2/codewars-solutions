def round_and_round(n, a, b):
    total = (a + b) % n
    if total == 0:
        return n
    
    return total
