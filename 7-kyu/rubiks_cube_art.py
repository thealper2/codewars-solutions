def cube(n):
    top = []
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        layer = '/\\' * (i + 1) + '_\\' * n
        top.append(spaces + layer)
        
    bottom = []
    for i in range(n):
        spaces = ' ' * i
        layer = '\\/' * (n - i) + '_/' * n
        bottom.append(spaces + layer)
        
    return '\n'.join(top + bottom)
