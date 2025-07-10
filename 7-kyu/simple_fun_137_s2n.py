def s2n(m, n):
    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            result += i ** j
            
    return result
