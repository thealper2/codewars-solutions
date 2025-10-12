def odd(s):
    result = 0
    s = list(s)
    n = len(s)
    
    for i in range(n):
        if s[i] == 'o':
            d1 = -1
            d2 = -1
            
            for j in range(i + 1, n):
                if s[j] == 'd' and d1 == -1:
                    d1 = j
                elif s[j] == 'd' and d2 == -1:
                    d2 = j
                    break
            
            if d1 != -1 and d2 != -1:
                result += 1
                s[i] = s[d1] = s[d2] = '_'
    
    return result
