def second_symbol(s, symbol):
    n = len(s)
    for i in range(n):
        if s[i] == symbol:
            for j in range(i + 1, n):
                if s[j] == symbol:
                    return j
                
    return -1
