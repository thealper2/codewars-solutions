def moving_average(values,n):
    if n == 0:
        return None
    
    if not values or n > len(values):
        return None
    
    return [sum(values[i:i+n]) / n for i in range(len(values) - n + 1)]
