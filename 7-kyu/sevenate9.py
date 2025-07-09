def seven_ate9(str_):
    n = len(str_)
    i = 0
    result = list(str_)
    
    while i < n - 2:
        if result[i] == '7' and result[i + 1] == '9' and result[i + 2] == '7':
            del result[i + 1]
            n -= 1
        else:
            i += 1
    
    return ''.join(result)