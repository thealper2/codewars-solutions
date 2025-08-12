def has_unique_chars(string):
    seen = set()
    for c in string:
        if c in seen:
            return False
        
        seen.add(c)
        
    return True