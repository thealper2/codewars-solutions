def sort_my_string(s):
    n = len(s)
    even = ''
    odd = ''
    
    for i in range(n):
        if s[i] == ' ':
            continue
        elif i % 2 == 0:
            even += s[i]
        elif i % 2 == 1:
            odd += s[i]
    
    return ' '.join([even, odd])
