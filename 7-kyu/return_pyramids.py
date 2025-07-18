def pyramid(n):
    result = []
    for i in range(n):
        leading_spaces = ' ' * (n - 1 - i)
        if i == n - 1:
            middle = '_' * (2 * i)
        else:
            middle = ' ' * (2 * i)
            
        line = leading_spaces + '/' + middle + '\\\n'
        result.append(line)
            
    return "".join(result)
