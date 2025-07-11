def start_smoking(bars,boxes):
    initial = bars * 10 * 18 + boxes * 18
    total = initial
    stubs = initial
    
    while stubs >= 5:
        new_cigs = stubs // 5
        total += new_cigs
        stubs = stubs % 5 + new_cigs
    
    return total