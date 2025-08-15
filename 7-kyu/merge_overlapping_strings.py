def merge_strings(a, b):
    max_overlap = min(len(a), len(b))
    best_i = 0
    for i in range(max_overlap, 0, -1):
        if a[-i:] == b[:i]:
            best_i = i
            break
            
    return a + b[best_i:]
