from collections import Counter

def highest_rank(arr):
    counts = Counter(arr)
    return max(counts, key=lambda x: (counts[x], x))
    