def pattern(n):
    result = []
    middle_length = 2 * n - 1
    indent = (middle_length - 1) // 2
    
    for i in range(1, n):
        line = ' ' * indent + str(i % 10)
        result.append(line)
    
    middle = ''
    for i in range(1, n + 1):
        middle += str(i % 10)
    for i in range(n - 1, 0, -1):
        middle += str(i % 10)
    result.append(middle)
    
    for i in range(n - 1, 0, -1):
        line = ' ' * indent + str(i % 10)
        result.append(line)
    
    return '\n'.join(result) + '\n'
