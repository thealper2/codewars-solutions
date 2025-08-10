def digitize(n):
    if n < 10:
        return [n]
    
    result = []
    i = 0
    
    while 10 ** i <= n:
        d = n // 10 ** i % 10
        result.append(d)
        i += 1
        
    return result[::-1]