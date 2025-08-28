def asterisc_it(n):
    if isinstance(n, list):
        s = ''.join(map(str, n))
    else:
        s = str(n)
        
    result = []
    for i in range(len(s)):
        result.append(s[i])
        if i < len(s)-1 and int(s[i]) % 2 == 0 and int(s[i+1]) % 2 == 0:
            result.append('*')
    
    return ''.join(result)
