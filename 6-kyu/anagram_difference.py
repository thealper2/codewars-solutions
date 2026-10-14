from collections import Counter

def anagram_difference(w1, w2):
    f1 = Counter(w1)
    f2 = Counter(w2)
    result = 0
    for k1, v1 in f1.items():
        if k1 not in w2:
            result += v1
    for k2, v2 in f2.items():
        if k2 not in w1:
            result += v2
        else:
            result += abs(v2 - f1[k2])
            
    return result
    