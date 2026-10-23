from collections import defaultdict

def substring(strng: str) -> str:
    left = 0
    counts = defaultdict(int)
    best_start, best_len = 0, 0
    for right, ch in enumerate(strng):
        counts[ch] += 1
        while len(counts) > 2:
            counts[strng[left]] -= 1
            if counts[strng[left]] == 0:
                del counts[strng[left]]

            left += 1

        if right - left + 1 > best_len:
            best_len = right - left + 1
            best_start = left

    return strng[best_start:best_start + best_len]