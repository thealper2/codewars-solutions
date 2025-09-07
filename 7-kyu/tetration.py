def tetration(x, y):
    if y == 0:
        return 1
    
    result = x
    for _ in range(y - 1):
        result = x ** result
        
    return result
