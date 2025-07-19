def alpha_seq(strng):
    n = len(strng)
    result = []
    
    for i in range(n):
        c = strng[i].upper()
        l = ord(c) - ord('A')
        result.append(f"{c.upper()}{c.lower() * (l)}")

    result.sort()
    return ','.join(result)