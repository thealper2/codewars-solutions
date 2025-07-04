def powers(n):
    result = []
    power = 0
    
    while n > 0:
        if n % 2 == 1:
            result.append(2 ** power)
        n = n // 2
        power += 1
        
    return result
