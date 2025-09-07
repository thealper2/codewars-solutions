def ones_counter(inp):
    result = []
    count = 0
    n = len(inp)
    for i in range(n):
        if inp[i] == 1:
            count += 1
        else:
            if count:
                result.append(count)
                
            count = 0
            
    if count:
        result.append(count)
        
    return result
