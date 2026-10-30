def hamming(n):
    h = [1] * n
    i2 = i3 = i5 = 0
    next2, next3, next5 = 2, 3, 5
    for k in range(1, n):
        nxt = min(next2, next3, next5)
        h[k] = nxt
        if nxt == next2:
            i2 += 1
            next2 = h[i2] * 2
        if nxt == next3:
            i3 += 1
            next3 = h[i3] * 3
        if nxt == next5:
            i5 += 1
            next5 = h[i5] * 5
    return h[n - 1]