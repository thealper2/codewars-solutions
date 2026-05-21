def maximum_volume(n):
    max_val = 0
    i = 1
    while n - (2 * i) > 0:
        v = (n - 2 * i) * (n - 2 * i) * i
        max_val = max(max_val, v)
        i += 1
        
    return max_val