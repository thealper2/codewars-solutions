def maskify(cc):
    n = len(cc)
    if n < 5:
        return cc
    
    return '#' * (n - 4) + cc[-4:]
