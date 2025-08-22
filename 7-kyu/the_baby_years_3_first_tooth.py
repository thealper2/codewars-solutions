def first_tooth(array):
    n = len(array)
    diffs = []
    for i in range(n):
        left_diff = 0
        right_diff = 0
        if i > 0:
            left_diff = array[i] - array[i-1]
        
        if i < n - 1:
            right_diff = array[i] - array[i+1]
        
        total_diff = left_diff + right_diff
        diffs.append(total_diff)
    
    max_diff = max(diffs)
    if diffs.count(max_diff) > 1:
        return -1
    
    return diffs.index(max_diff)
