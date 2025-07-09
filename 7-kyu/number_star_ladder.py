def pattern(n):
    if n == 1:
        return '1'
    
    pattern = '1\n'
    for i in range(1, n):
        pattern += '1' + '*' * i + str(i + 1)
        if i < n - 1:
            pattern += '\n'
            
    return pattern
