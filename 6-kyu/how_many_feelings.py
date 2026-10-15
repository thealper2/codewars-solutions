from collections import Counter

def count_feelings(st, arr):
    s_count = Counter(st)
    count = 0
    for feeling in arr:
        f_count = Counter(feeling)
        if all(s_count[ch] >= f_count[ch] for ch in f_count):
            count += 1

    return f"{count} feeling{'s' if count != 1 else ''}."