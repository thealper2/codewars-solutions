def testit(s):
    t = 'word'
    i = 0
    r = 0
    s_lower = s.lower()
    for x in s_lower:
        if x == t[i]:
            i += 1
            if i == 4:
                r += 1
                i = 0
            
    return r
