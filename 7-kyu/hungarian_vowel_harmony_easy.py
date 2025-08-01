def dative(word):
    last = ''
    front_vowels = {'e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'}
    back_vowels = {'a', 'á', 'o', 'ó', 'u', 'ú'}
    for c in word:
        if c in front_vowels:
            last = 'nek'
        elif c in back_vowels:
            last = 'nak'
            
    return word + last
