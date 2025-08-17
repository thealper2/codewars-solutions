def check_parity(parity, bin_str): 
    ones = bin_str.count('1')
    if parity == 'even' and ones % 2 == 1:
        return 1
    elif parity == 'odd' and ones % 2 == 0:
        return 1
    
    return 0
        
