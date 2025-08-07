def div_con(x):
    total = 0
    for item in x:
        if isinstance(item, int):
            total += item
        elif isinstance(item, str):
            total -= int(item)
            
    return total
