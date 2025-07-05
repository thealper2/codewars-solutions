def consecutive_ducks(n):
    if n == 1:
        return False
    
    max_k = int((2 * n) ** 0.5) + 2
    for k in range(2, max_k + 1):
        if (2 * n) % k == 0:
            temp = (2 * n) // k - k + 1
            if temp > 0 and temp % 2 == 0:
                m = temp // 2
                if m > 0:
                    return True
                
    return False