def gap(num):
    num = str(bin(num)[2:])
    max_gap = 0
    current_gap = 0
    
    for d in num:
        if d == '1':
            max_gap = max(current_gap, max_gap)
            current_gap = 0
        elif d == '0':
            current_gap += 1
    
    return max_gap
