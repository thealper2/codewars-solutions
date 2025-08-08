def paint_letterboxes(start, finish):
    digits = [0 for _ in range(10)]
    for i in range(start, finish + 1):
        idx = 0
        while 10 ** idx <= i:
            d = i // (10**idx) % 10
            digits[d] += 1
            idx += 1
            
    return digits
