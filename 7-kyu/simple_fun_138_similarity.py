def similarity(a, b):
    set1 = set(a)
    set2 = set(b)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    jaccard_similarity = len(intersection) / len(union) if len(union) != 0 else 0
    return jaccard_similarity
