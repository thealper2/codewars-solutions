def sumsquares(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sumsquares(item)
        else:
            total += item ** 2
            
    return total
