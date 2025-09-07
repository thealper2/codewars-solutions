def xmastree(n):
    result = []
    for i in range(n):
        fill = '_' * (n - (i + 1))
        height = '#' * ((2 * i) + 1)
        result.append(fill + height + fill)
        
    for _ in range(2):
        fill = '_' * (n - 1)
        result.append(fill + '#' + fill)
        
    return result
