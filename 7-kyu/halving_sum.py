def halving_sum(n): 
    i = 0
    total = 0
    while 2 ** i <= n:
        total += n // (2 ** i)
        i += 1
        
    return total
