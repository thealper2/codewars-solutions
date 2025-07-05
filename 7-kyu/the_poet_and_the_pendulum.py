def pendulum(values):
    n = len(values)
    result = []
    values.sort()
    
    for i in range(n):
        if i % 2 == 0:
            result.insert(0, values[i])
        else:
            result.append(values[i])
            
    return result