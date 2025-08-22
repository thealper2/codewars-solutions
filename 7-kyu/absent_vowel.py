def absent_vowel(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        if vowel not in x.lower():
            return vowels.index(vowel)
