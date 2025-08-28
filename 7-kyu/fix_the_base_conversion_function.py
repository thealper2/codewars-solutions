def convert_num(number, base):
    if type(number) not in [int, bool]:
        return 'Invalid number input'
    
    number = int(number)
        
    if base == 'hex':
        return hex(number)
    
    if base == 'bin':
        return bin(number)
    
    return 'Invalid base input'
