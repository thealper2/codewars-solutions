def f(p, q):
    if p == 0 and q == 0:
        return None
    
    a = p / (1 - (1 - p) * (1 - q)) if (1 - (1 - p) * (1 - q)) != 0 else 0.0
    b = ((1 - q) * p) / (1 - (1 - p) * (1 - q)) if (1 - (1 - p) * (1 - q)) != 0 else 0.0
    return (a, b)
