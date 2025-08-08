def capitalize(s):
    result = ['', '']
    n = len(s)
    
    for i in range(n):
        if i % 2 == 0:
            result[0] += s[i].upper()
            result[1] += s[i].lower()
        else:
            result[0] += s[i].lower()
            result[1] += s[i].upper()
            
    return result
