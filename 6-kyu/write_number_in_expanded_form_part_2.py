def expanded_form(num):
    a, b = str(num).split('.')
    result = []
    a = int(a)
    p = 0
    while 10**p <= a:
        d = a // 10**p % 10
        if d != 0:
            result.append(str(d * 10**p))
            
        p += 1
        
    result = result[::-1]
        
    n = len(b)
    for i in range(n):
        if b[i] != '0':
            result.append(f'{b[i]}/{10**(i+1)}')
            
    return ' + '.join(result)
    
        
