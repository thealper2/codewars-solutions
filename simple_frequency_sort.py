def solve(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
        
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    result = []
    for num, f in sorted_items:
        result.extend([num] * f)
        
    return result
