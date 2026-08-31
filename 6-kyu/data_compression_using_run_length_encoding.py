def encode(st):
    if not st:
        return ""
    
    result = ""
    count = 1
    last_char = st[0]
    
    for c in st[1:]:
        if c == last_char:
            count += 1
        else:
            result += str(count) + last_char
            last_char = c
            count = 1
    
    result += str(count) + last_char
    return result

def decode(st):
    result = ""
    i = 0
    n = len(st)
    while i < n:
        count = ""
        while i < n and st[i].isdigit():
            count += st[i]
            i += 1
        if i < n:
            char = st[i]
            result += int(count) * char
            i += 1
    return result