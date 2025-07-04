def fix_parentheses(strng):
    open_needed = 0
    close_needed = 0
    balance = 0
    
    for char in strng:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            open_needed += -balance
            balance = 0
    
    close_needed = balance
    return '(' * open_needed + strng + ')' * close_needed
