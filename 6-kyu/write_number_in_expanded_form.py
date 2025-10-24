def expanded_form(num):
    result = []
    i = 0
    while 10**i <= num:
        digit = num // 10**i % 10
        if digit != 0:
            result.append(digit * (10 ** i))
    
        i += 1
    
    return ' + '.join(map(str, result[::-1]))
