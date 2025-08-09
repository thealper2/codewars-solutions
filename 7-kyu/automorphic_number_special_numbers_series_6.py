def automorphic(n):
    n_square = n ** 2
    i = 0
    t = 0
    
    while 10 ** i <= n_square:
        d = n_square // 10 ** i % 10
        t += d * (10 ** i)
        if t == n:
            return 'Automorphic'
        
        i += 1
        
    return 'Not!!'