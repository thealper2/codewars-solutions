def calculate(n1, n2, o):
    def bin_to_int(b):
        if b.startswith('-'):
            return -int(b[1:], 2)
        return int(b, 2)
    
    num1 = bin_to_int(n1)
    num2 = bin_to_int(n2)
    
    if o == 'add':
        result = num1 + num2
    elif o == 'subtract':
        result = num1 - num2
    elif o == 'multiply':
        result = num1 * num2
    else:
        return "Invalid operator"
    
    if result < 0:
        return '-' + bin(abs(result))[2:]
    
    return bin(result)[2:]