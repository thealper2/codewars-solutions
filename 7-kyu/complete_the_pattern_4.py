def pattern(n):
    result = []
    for i in range(n):
        result.append(''.join(map(str, range(i + 1, n + 1))))
    
    return '\n'.join(result)
