from collections import Counter


def only_duplicates(st):
    freq = Counter(st)
    return ''.join(c for c in st if freq[c] > 1)