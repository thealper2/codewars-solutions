def ka_co_ka_de_ka_me(word):
    if not word:
        return ''
    
    vowels = 'aeiouAEIOU'
    result = 'ka'
    
    i = 0
    n = len(word)
    while i < n:
        result += word[i]
        if word[i] in vowels:
            j = i + 1
            while j < n and word[j] in vowels:
                result += word[j]
                j += 1
                
            if j > i + 1:
                i = j - 1
                
            if i < n - 1:
                result += 'ka'
                
        i += 1
        
    return result
