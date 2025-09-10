def diplomas(h, w, n):
    if n == 0:
        return 0
    
    l = 0
    r = max(h, w) * n
    while l < r:
        mid = (l + r) // 2
        rows = mid // h
        cols = mid // w
        if rows * cols >= n:
            r = mid
        else:
            l = mid + 1
            
    return l
