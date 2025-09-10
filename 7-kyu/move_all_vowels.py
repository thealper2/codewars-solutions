def move_vowels(s): 
    vowels = []
    consonants = []
    for c in s:
        if c in 'aeiou':
            vowels.append(c)
        else:
            consonants.append(c)
            
    return ''.join(consonants + vowels)
