def interweave(s1, s2):
    result = []
    n = max(len(s1), len(s2))
    for i in range(n):
        if i < len(s1) and not s1[i].isdigit():
            result.append(s1[i])
        if i < len(s2) and not s2[i].isdigit():
            result.append(s2[i])
            
    return ''.join(result)
