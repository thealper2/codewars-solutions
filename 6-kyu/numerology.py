def numerology(date): 
    s = date.strftime('%m%d%Y')
    while len(s) > 1:
        s = str(sum(int(c) for c in s))
        
    return int(s)