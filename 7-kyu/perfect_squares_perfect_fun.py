def square_it(digits):
    str_n = str(digits)
    n = len(str_n)
    sn = int(n ** 0.5)
    if sn * sn != n:
        return "Not a perfect square!"
    
    result = []
    for i in range(0, n, sn):
        result.append(str_n[i:i+sn])
        
    return '\n'.join(result)
