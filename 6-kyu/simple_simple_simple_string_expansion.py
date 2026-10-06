def string_expansion(s):
    result = []
    count = 1
    i = 0
    n = len(s)
    
    while i < n:
        ch = s[i]
        if ch.isdigit():
            count = int(ch)
            i += 1
        else:
            result.append(ch * count)
            i += 1
            
    return ''.join(result)