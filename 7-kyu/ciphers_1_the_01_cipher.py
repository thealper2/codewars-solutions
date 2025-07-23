def encode(s):
    n = len(s)
    result = ""
    d = {}
    for i in range(n):
        c = s[i]
        if d.get(c, None):
            result += d[c]
        else:
            if c.isalpha():
                if (ord(c.upper()) - ord('A')) % 2 == 0:
                    result += '0'
                    d[c] = '0'
                else:
                    result += '1'
                    d[c] = '1'
            else:
                result += c
                d[c] = c
        
    return result