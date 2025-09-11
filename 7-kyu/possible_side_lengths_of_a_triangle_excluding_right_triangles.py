def side_len(a, b):
    res = []
    low, high = abs(a - b) + 1, a + b - 1
    
    for c in range(low, high+1):
        if a*a + b*b == c*c: 
            continue
        if a*a + c*c == b*b: 
            continue
        if b*b + c*c == a*a: 
            continue
        res.append(c)
    return res
