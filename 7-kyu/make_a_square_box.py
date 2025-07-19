def box(n):
    result = []
    for i in range(n):
        if i == 0 or i == n - 1:
            result.append('-' * n)
        else:
            result.append('-' + ' ' * (n - 2) + '-')
            
    return result