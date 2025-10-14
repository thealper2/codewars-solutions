def play_pass(s, n):
    s = s.upper()
    l = len(s)
    result = ''
    for i in range(l):
        if s[i].isdigit():
            new_d = 9 - int(s[i])
            result += str(new_d)
            
        elif s[i].isalpha():
            new_c = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
            if i % 2 == 1:
                new_c = new_c.lower()
                
            result += new_c
        
        else:
            result += s[i]
            
    return result[::-1]
