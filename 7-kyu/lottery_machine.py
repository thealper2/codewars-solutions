def lottery(s):
    seen = []
    for c in s:
        if c.isdigit() and c not in seen:
            seen.append(c)
            
    if not seen:
        return "One more run!"
    
    return ''.join(seen)
