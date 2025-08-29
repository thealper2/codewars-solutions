def evaluate(equation):
    tokens = equation.split(' @ ')
    a = int(tokens[0])
    if a == 0:
        return 0
    
    for token in tokens[1:]:
        b = int(token)
        if b == 0:
            return None
        
        a = (a + b) + (a - b) + (a * b) + (a // b)
    
    return a
