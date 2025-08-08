def generate_shape(n):
    result = ''
    for i in range(n):
        result += '+' * n
        if i < n - 1:
            result += '\n'
            
    return result
