def pattern(n):
    result = []
    for i in range(1, n + 1):
        line = str(i) * i
        result.append(line)
        
    return '\n'.join(result)
