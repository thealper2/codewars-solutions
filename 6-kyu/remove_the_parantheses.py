def remove_parentheses(st):
    result = ''
    is_opened = 0
    for c in st:
        if c == '(':
            is_opened += 1
        elif c == ')':
            is_opened -= 1
        elif is_opened == 0:            
            result += c
            
    return result