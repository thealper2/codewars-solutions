def accum(st):
    n = len(st)
    result = ""
    for i in range(n):
        result += (st[i] * (i + 1)).capitalize()
        if i + 1 < n:
            result += "-"
        
    return result
