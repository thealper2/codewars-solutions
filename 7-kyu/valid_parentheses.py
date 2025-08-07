def valid_parentheses(paren_str):
    if not paren_str:
        return True
    
    if paren_str[0] == ')':
        return False
    
    balance = 0
    for char in paren_str:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False
        
    return balance == 0
