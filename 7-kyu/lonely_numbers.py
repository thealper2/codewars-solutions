def numbers_need_friends_too(n):
    s = str(n)
    result = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
            
        group = s[i:j]
        if len(group) == 1:
            result.append(group * 3)
        else:
            result.append(group)
            
        i = j
        
    return int(''.join(result))
