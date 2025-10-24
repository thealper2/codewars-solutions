from itertools import permutations

def ssc_forperm(arr):
    n = len(arr)
    unique_perms = set(permutations(arr))
    total_perm = len(unique_perms)
    ssc_values = []
    for perm in unique_perms:
        ssc = sum(i * val for i, val in enumerate(perm, start=1))
        ssc_values.append(ssc)
        
    total_ssc = sum(ssc_values)
    max_ssc = max(ssc_values)
    min_ssc = min(ssc_values)
    
    return [
        {'total perm': total_perm},
        {'total ssc': total_ssc},
        {'max ssc': max_ssc},
        {'min ssc': min_ssc}
    ]
