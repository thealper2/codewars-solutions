def jeringonza(s):
    vowels = 'aeiouAEIOU'
    result = ''
    for c in s:
        if c in vowels:
            result += c + ('p' if c.islower() else 'P') + c
        else:
            result += c
            
    return result
