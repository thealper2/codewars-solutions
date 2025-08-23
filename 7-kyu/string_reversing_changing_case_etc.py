def reverse_and_mirror(s1, s2):
    s1_rev = ''
    for c in s1:
        if c.isupper():
            s1_rev += c.lower()
        else:
            s1_rev += c.upper()
            
    s2_rev = ''
    for c in s2:
        if c.isupper():
            s2_rev += c.lower()
        else:
            s2_rev += c.upper()
            
    result = ''
    result += s2_rev[::-1]
    result += '@@@'
    result += s1_rev[::-1]
    result += s1_rev
    return result
