def minimum(a, x):
    r = a % x
    if x - r < r:
        return x - r
    else:
        return r
    
