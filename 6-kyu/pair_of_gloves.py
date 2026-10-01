from collections import Counter

def number_of_pairs(gloves):
    freq = Counter(gloves)
    return sum(v // 2 for v in freq.values())