def recurrence(values):
    min_val = min(values)
    min_idx = values.index(min_val)
    n = len(values)
    c = 0
    for i in range(min_idx + 1, n):
        if values[i] > values[i - 1]:
            c += 1
        else:
            c = 0
        
        if c == 3:
            return True
        
    return False
