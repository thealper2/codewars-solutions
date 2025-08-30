def array_mash(a, b):
    result = []
    for a_, b_ in zip(a, b):
        result.append(a_)
        result.append(b_)
        
    return result
