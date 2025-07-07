def solve(s, k): 
    for c in range(ord('a'), ord('z') + 1):
        char = chr(c)
        while k > 0 and char in s:
            index = s.index(char)
            s = s[:index] + s[index + 1:]
            k -= 1
            if k == 0:
                break
        
        if k == 0:
            break
            
    return s
