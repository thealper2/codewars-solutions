def sticky_calc(operation, val1, val2):
    if val1 <= 0 or val2 <= 0:
        return 0
    
    val1 = int(round(val1))
    val2 = int(round(val2))
    
    concated = str(val1) + str(val2)
    if operation == '+':
        result = int(concated) + val2
    elif operation == '-':
        result =int(concated) - val2
    elif operation == '/':
        result = int(concated) / val2
    elif operation =='*':
        result = int(concated) * val2
        
    return round(result)
