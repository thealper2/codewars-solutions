def house_numbers_sum(inp):
    n = len(inp)
    i = 0
    total = 0
    
    while i < n and inp[i] != 0:
        total += inp[i]
        i += 1
        
    return total
