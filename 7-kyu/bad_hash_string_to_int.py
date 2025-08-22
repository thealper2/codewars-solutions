def string_hash(s):
    a = 0
    space_count = s.count(' ')
    for char in s:
        a += ord(char)
    
    b = 0
    for i in range(len(s) - 1):
        b += ord(s[i+1]) - ord(s[i])
    
    c = (a | b) & (~a << 2)
    d = c ^ (32 * (space_count + 1))
    return d
