def vowel_2_index(s):
    n = len(s)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = ""
    for i in range(n):
        if s[i].lower() in vowels:
            result += str(i + 1)
        else:
            result += s[i]
            
    return result