def compound_array(a, b):
    n = min(len(a), len(b))
    result = []
    
    for a_, b_ in zip(a[:n], b[:n]):
        result.append(a_)
        result.append(b_)
        
    result.extend(a[n:])
    result.extend(b[n:])
    return result