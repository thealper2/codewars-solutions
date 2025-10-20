def mul_power(n, k):
    m = 1
    for i in range(2, int(n**0.5) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
            
        if cnt % k != 0:
            m *= i ** (k - (cnt % k))
            
    if n > 1:
        m *= n ** (k - 1)
        
    return m
