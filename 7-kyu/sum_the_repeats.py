from collections import defaultdict


def repeat_sum(l):
    freq = defaultdict(int)
    for arr in l:
        seen = set(arr)
        for num in seen:
            freq[num] += 1
            
    total = 0
    for k, v in freq.items():
        if v >= 2:
            total += k
            
    return total
