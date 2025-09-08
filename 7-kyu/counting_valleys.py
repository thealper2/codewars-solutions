def counting_valleys(s): 
    result = 0
    valley = 0
    is_down = False
    for c in s:
        if c == 'U':
            valley += 1
        elif c == 'D':
            valley -= 1
            
        if valley < 0:
            is_down = True
            
        if valley == 0 and is_down:
            result += 1
            is_down = False
            
    return result
