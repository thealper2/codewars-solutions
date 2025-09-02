def triangular_range(start, stop):
    result = {}
    n = 1
    while True:
        tri = n * (n + 1) // 2
        if tri > stop:
            break
            
        if tri >= start:
            result[n] = tri
            
        n += 1
    
    return result
