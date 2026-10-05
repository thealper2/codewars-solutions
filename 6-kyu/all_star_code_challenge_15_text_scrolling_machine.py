def rotate(str_):
    if not str_:
        return []
    
    result = [str_]
    for _ in range(len(str_) - 1):
        new_s = result[-1][-1] + result[-1][:-1]
        result.append(new_s)
        
    return result[::-1]