def find_lineup(distances):
    n = len(distances)
    if sorted(distances) != list(range(n)):
        return []
    
    result = [0] * n
    for i, x in enumerate(distances):
        result[x] = i + 1
    
    return result
