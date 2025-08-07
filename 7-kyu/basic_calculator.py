def calculate(num1, op, num2): 
    if op not in '+-*/':
        return None
    if op == '/' and num2 == 0:
        return None
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
