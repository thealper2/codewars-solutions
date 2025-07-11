def uglify_word(s):
    flag = 1
    result = []
    for char in s:
        if char.isalpha():
            if flag == 1:
                result.append(char.upper())
            else:
                result.append(char.lower())
            
            flag ^= 1
        
        else:
            result.append(char)
            flag = 1
    return ''.join(result)
