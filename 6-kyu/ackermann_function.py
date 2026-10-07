def Ackermann(m, n):
    if not isinstance(m, int) or not isinstance(n, int):
        return None
    
    if m < 0 or n < 0:
        return None
    
    stack = []
    while True:
        if m == 0:
            n += 1
            if not stack:
                return n
            
            m = stack.pop()
        elif n == 0:
            m -= 1
            n = 1
        else:
            stack.append(m - 1)
            n -= 1