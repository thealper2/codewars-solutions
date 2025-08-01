def sponge_meme(s):
    if not s:
        return None
    
    last = True
    result = ''
    
    for c in s:
        if last:
            result += c.upper()
        else:
            result += c.lower()
            
        last = not last
            
    return result
