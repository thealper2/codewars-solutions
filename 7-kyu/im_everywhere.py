def i(word):
    if not word:
        return 'Invalid word'
    
    if not word[0].isalpha() or word[0].islower():
        return 'Invalid word'
    
    if word[0] == 'I':
        return 'Invalid word'
    
    vowels = 0
    consonants = 0
    for c in word:
        if c.isalpha():
            if c.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
                
    if vowels >= consonants:
        return 'Invalid word'
    
    return 'i' + word
