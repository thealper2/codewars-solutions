def seqlist(first, c, l):
    result = [first]
    for i in range(l - 1):
        result.append(result[-1] + c)
        
    return result