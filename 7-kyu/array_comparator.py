def match_arrays(v, r):
    count = 0
    for item in set(v):
        if item in set(r):
            count += 1
            
    return count
