def dominator(arr):
    if not arr:
        return -1
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    half = len(arr) / 2
    for num, count in counts.items():
        if count > half:
            return num
    return -1
