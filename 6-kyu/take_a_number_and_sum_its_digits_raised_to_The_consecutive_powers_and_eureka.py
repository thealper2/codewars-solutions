def sum_dig_pow(a, b):
    result = []
    
    for n in range(a, b + 1):
        s = sum(int(d) ** (i + 1) for i, d in enumerate(str(n)))
            
        if s == n:
            result.append(n)
    
    
    return result