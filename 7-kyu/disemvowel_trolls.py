def disemvowel(string_):
    result = ''
    for c in string_:
        if c not in 'aeiouAEIOU':
            result += c
            
    return result
