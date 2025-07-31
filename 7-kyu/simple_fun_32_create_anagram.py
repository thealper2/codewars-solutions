from collections import Counter


def create_anagram(s, t):
    freq_s = Counter(s)
    freq_t = Counter(t)

    replacements = 0
    all_chars = set(freq_s.keys()).union(set(freq_t.keys()))

    for char in all_chars:
        replacements += abs(freq_s[char] - freq_t[char])

    return replacements // 2
