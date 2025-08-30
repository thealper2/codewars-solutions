def calculate(strng):
    words = strng.split()
    has = int(words[2])
    if words[-2] == 'loses':
        has -= int(words[-1])
    elif words[-2] == 'gains':
        has += int(words[-1])
        
    return has
