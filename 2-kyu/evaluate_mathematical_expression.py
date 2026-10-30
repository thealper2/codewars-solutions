def calc(expr):
    tokens = []
    i, n = 0, len(expr)
    while i < n:
        c = expr[i]
        if c.isspace():
            i += 1
        elif c.isdigit() or c == '.':
            j = i
            while j < n and (expr[j].isdigit() or expr[j] == '.'):
                j += 1
            tokens.append(float(expr[i:j]))
            i = j
        else:
            tokens.append(c)
            i += 1

    pos = 0
    def expr_():
        nonlocal pos
        v = term()
        while pos < len(tokens) and tokens[pos] in '+-':
            op = tokens[pos]; pos += 1
            r = term()
            v = v + r if op == '+' else v - r
        return v
    def term():
        nonlocal pos
        v = factor()
        while pos < len(tokens) and tokens[pos] in '*/':
            op = tokens[pos]; pos += 1
            r = factor()
            v = v * r if op == '*' else v / r
        return v
    def factor():
        nonlocal pos
        if tokens[pos] == '-':
            pos += 1
            return -factor()
        if tokens[pos] == '+':
            pos += 1
            return factor()
        if tokens[pos] == '(':
            pos += 1
            v = expr_()
            pos += 1  # ')'
            return v
        v = tokens[pos]; pos += 1
        return v
    return expr_()