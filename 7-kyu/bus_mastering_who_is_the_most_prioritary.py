def arbitrate(inp, n):
    l = len(inp)
    for i in range(l):
        if i <= n and inp[i] == '1':
            return '0'* (i) + '1' + '0' * (l - i - 1)
        
    return inp