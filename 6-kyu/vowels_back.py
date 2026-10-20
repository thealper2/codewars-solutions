def vowel_back(st):
    vowels = set('aeiou')
    exceptions = {'c': 1, 'd': 3, 'e': 4, 'o': 1}
    result = []
    
    for ch in st:
        orig = ch
        if ch in exceptions:
            idx = (ord(ch) - ord('a') - exceptions[ch]) % 26
        elif ch in vowels:
            idx = (ord(ch) - ord('a') - 5) % 26
        else:
            idx = (ord(ch) - ord('a') + 9) % 26
            
        new_ch = chr(idx + ord('a'))
        if new_ch in 'code':
            result.append(orig)
        else:
            result.append(new_ch)
            
    return ''.join(result)