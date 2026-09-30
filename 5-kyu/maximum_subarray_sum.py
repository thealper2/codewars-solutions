def max_sequence(arr):
    best = 0
    current = 0
    for x in arr:
        current = max(0, current + x)
        best = max(best, current)
        
    return best