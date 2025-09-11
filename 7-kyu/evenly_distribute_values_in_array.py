from collections import Counter


def distribute_evenly(lst):
    seen = []
    for w in lst:
        if w not in seen:
            seen.append(w)
            
    freq = Counter(lst)
    result = []
    while sum(freq.values()):
        for w in seen:
            if freq[w] > 0:
                result.append(w)
                freq[w] -= 1
                
    return result
