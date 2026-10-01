from collections import Counter

def scramble(s1, s2):
    freq1 = Counter(s1)
    freq2 = Counter(s2)
    for k, v in freq2.items():
        if k not in freq1:
            return False

        if v > freq1[k]:
            return False

    return True