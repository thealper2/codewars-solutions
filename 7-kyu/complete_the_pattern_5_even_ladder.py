def pattern(n):
    result = []
    for i in range(2, n + 1, 2):
        result.append(str(i) * i)
        
    return '\n'.join(result)