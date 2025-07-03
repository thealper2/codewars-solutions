def capitalize(s, ind):
    n = len(s)
    result = ""
    for i in range(n):
        if i in ind:
            result += s[i].upper()
        else:
            result += s[i]
            
    return result