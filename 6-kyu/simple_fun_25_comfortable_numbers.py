def comfortable_numbers(L, R):
    count = 0
    
    for a in range(L, R + 1):
        s_a = sum(int(d) for d in str(a))
        min_b = a - s_a
        max_b = a + s_a
        
        for b in range(a + 1, min(R, max_b) + 1):
            s_b = sum(int(d) for d in str(b))
            if a >= (b - s_b) and a <= (b + s_b):
                count += 1
    
    return count
