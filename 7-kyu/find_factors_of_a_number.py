def factors(x):
    if type(x) != int:
        return -1
    
    if x < 1:
        return -1
    
    result = []
    for i in range(x, 0, -1):
        if x % i == 0:
            result.append(i)
            
    return result
