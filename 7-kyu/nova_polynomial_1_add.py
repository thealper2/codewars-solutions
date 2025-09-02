def poly_add(p1, p2):
    n = max(len(p1), len(p2))
    result = [0] * n
    for i in range(len(p1)):
        result[i] += p1[i]
        
    for i in range(len(p2)):
        result[i] += p2[i]
        
    return result
