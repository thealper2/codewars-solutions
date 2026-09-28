def duplicate_encode(word):
    d = {}
    for c in word.lower():
        if c not in d:
            d[c] = '('
        else:
            d[c] = ')'
            
    return ''.join([d[c.lower()] for c in word])