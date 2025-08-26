def fix_code(isbn):
    total = 0
    missing_index = -1
    for i, char in enumerate(isbn):
        if char == '?':
            missing_index = i
        else:
            if char == 'X':
                digit = 10
            else:
                digit = int(char)
                
            total += digit * (10 - i)
            
    if missing_index == -1:
        return ''
    
    for d in range(0, 11):
        temp_total = total + d * (10 - missing_index)
        if temp_total % 11 == 0:
            if d == 10:
                return 'X'
            else:
                return str(d)
            
    return ''
