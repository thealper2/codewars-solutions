def kaprekar_split(n):
    if n == 1:
        return 0
    
    n2 = n ** 2
    s = str(n2)
    for i in range(1, len(s)):
        a = s[:i]
        b = s[i:]
        if a == '':
            a = 0
        else:
            a = int(a)
        
        if b == '':
            b = 0
        else:
            b = int(b)
        
        if a + b == n:
            return i
        
    return -1
