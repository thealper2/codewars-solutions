def squares(x, n):
    i = 1
    result = []
    for _ in range(n):
        result.append(x ** i)
        i *= 2
        
    return result
