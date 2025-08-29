def maxlen(L1,L2):
    min_ = min(L1, L2)
    max_ = max(L1, L2)
    return min(max_ / 2, max(max_ / 3, min_))    
