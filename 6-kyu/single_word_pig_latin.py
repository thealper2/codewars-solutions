def pig_latin(word):
    if not word.isalpha():
        return None
    
    word = word.lower()
    vowels = set('aeiou')
    if word[0] in vowels:
        return word + 'way'

    i = 0
    while i < len(word) and word[i] not in vowels:
        i += 1
    
    if i == len(word):
        return word + 'ay'
    
    return word[i:] + word[:i] + 'ay'