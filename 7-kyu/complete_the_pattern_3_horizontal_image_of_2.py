def pattern(n):
    if n <= 0:
        return ''
    
    result = []
    for i in range(n, 0, -1):
        row = ''
        for j in range(n, i - 1, -1):
            row += str(j)
            
        result.append(row)

    return '\n'.join(result)
