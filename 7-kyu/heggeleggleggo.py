def heggeleggleggo(word):
    result = ""
    vowels = ' aeiouAEIOU'
    for c in word:
        result += c
        if c not in vowels:
            result += "egg"
        
    return result