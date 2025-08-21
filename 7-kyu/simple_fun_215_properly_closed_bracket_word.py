def closed_bracket_word(st):
    n = len(st)
    for i in range((n + 1) // 2):
        j = n - 1 - i
        if ord(st[i]) + ord(st[j]) != 219:
            return False
        
    return True
