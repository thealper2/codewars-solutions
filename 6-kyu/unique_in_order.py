def unique_in_order(sequence):
    if not sequence:
        return []
    
    if isinstance(sequence, str):
        sequence = list(sequence)
        
    i = 0
    n = len(sequence)
    result = []
    
    while i < n:
        j = 1
        
        while i + j < n and sequence[i + j] == sequence[i]: 
            j += 1
            
        result.append(sequence[i])
        i += j
        
    return result    