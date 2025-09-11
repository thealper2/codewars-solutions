from collections import Counter

def majority(lst):
    if not lst:
        return None
    
    counts = Counter(lst)
    most_common = counts.most_common(2)
    if len(most_common) == 1:
        return most_common[0][0]
    
    if most_common[0][1] > most_common[1][1]:
        return most_common[0][0]
    
    return None
