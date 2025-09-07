def even_and_odd(n): 
    i = j = 0
    even = odd = 0
    k = 0
    
    while 10**k <= n:
        d = n // 10**k % 10
        if d % 2 == 0:
            even += d * (10 ** i)
            i += 1
        else:
            odd += d * (10 ** j)
            j += 1
            
        k += 1
            
    return (even, odd)
    
