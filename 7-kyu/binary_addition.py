def add_binary(a,b):
    result = ''
    s = a + b
    while s >= 1:
        result += str(s % 2)
        s //= 2
        
    return result[::-1]