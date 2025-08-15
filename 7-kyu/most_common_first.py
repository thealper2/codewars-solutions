from collections import Counter


def most_common(s):
    if not s:
        return s
    
    freq = Counter(s)
    indexed_chars = [(char, freq[char], idx) for idx, char in enumerate(s)]
    sorted_chars = sorted(indexed_chars, key=lambda x: (-x[1], x[2]))
    result = [char for char, _, _ in sorted_chars]
    return ''.join(result)
