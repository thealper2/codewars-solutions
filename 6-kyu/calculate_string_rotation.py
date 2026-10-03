def shifted_diff(first, second):
    for i in range(len(second)):
        if second[i:] + second[:i] == first:
            return i
    
    return -1
        