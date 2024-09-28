def close_compare(a, b, margin=0):
    if a - margin > b:
        return 1
    
    if b - margin > a:
        return -1
    
    if a - b <= margin or b - a <= margin:
        return 0