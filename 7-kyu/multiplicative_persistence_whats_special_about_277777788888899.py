def per(n):
    if n < 10:
        return []
    
    result = []
    current = n
    while current >= 10:
        product = 1
        temp = current
        
        while temp > 0:
            digit = temp % 10
            product *= digit
            temp = temp // 10
        
        result.append(product)
        current = product
    
    return result