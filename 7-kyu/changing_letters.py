def swap(st):
    result = ''
    for c in st:
        if c in 'aeiouAEIOU':
            result += c.upper()
        else:
            result += c
        
    return result
