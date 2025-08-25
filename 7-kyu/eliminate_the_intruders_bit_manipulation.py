def eliminate_unset_bits(number):
    if not number:
        return 0
    
    a = number.count('1')
    if a == 0:
        return 0
    
    return int('1' * a, 2)
