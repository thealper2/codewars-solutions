def counter_effect(hit_count):
    n = len(hit_count)
    result = []
    
    for i in range(n):
        result.append(list(range(int(hit_count[i]) + 1)))
    
    return result