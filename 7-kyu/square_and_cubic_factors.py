def factors(n):
    sq = []
    cb = []
    for i in range(2, int(n**0.5) + 1):
        if n % (i*i) == 0:
            sq.append(i)
            
    for i in range(2, int(n**(1/3)) + 1):
        if n % (i*i*i) == 0:
            cb.append(i)
            
    return [sq, cb]
