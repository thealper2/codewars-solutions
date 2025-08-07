def pattern(n):
    result = []
    for i in range(n):
        t = ''
        for j in range(n, i, -1):
            t += str(j)
            
        result.append(t)
    
    return '\n'.join(result)
