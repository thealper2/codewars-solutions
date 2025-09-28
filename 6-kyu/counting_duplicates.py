from collections import defaultdict


def duplicate_count(text):
    text = text.lower()
    freq = defaultdict(int)
    cnt = 0
    for c in text:
        freq[c] += 1

    for k, v in freq.items():
        if v > 1:
            cnt += 1
            
    return cnt
