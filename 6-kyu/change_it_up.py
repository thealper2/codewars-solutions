def changer(s):
    result = ''
    for c in s:
        if c.isalpha():
            new_c = chr(((ord(c.lower()) - ord('a') + 1) % 26) + ord('a'))
            if new_c in 'aeiouAEIOU':
                result += new_c.upper()
            else:
                result += new_c.lower()
        else:
            result += c
                
    
    return result
