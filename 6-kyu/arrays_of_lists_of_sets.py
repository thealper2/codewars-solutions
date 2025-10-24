def solve(arr):
    normalized = [''.join(sorted(set(s))) for s in arr]
    groups = {}
    for i, norm_str in enumerate(normalized):
        if norm_str not in groups:
            groups[norm_str] = []
            
        groups[norm_str].append(i)
        
    result = []
    for indices in groups.values():
        if len(indices) >= 2:
            result.append(sum(indices))
            
    return sorted(result)
