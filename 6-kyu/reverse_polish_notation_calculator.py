def calc(expr):
    tokens = expr.split()
    stack = []
    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        else:
            stack.append(float(token))

    return stack[0] if stack else 0