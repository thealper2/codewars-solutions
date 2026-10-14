from collections import Counter


def anagram_counter(words):
    freq = Counter(''.join(sorted(w)) for w in words)
    return sum(c * (c - 1) // 2 for c in freq.values())