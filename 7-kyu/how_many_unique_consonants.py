def count_consonants(text):
    vowels = 'aeiou'
    seen = set()
    for char in text.lower():
        if char.isalpha() and char not in vowels:
            seen.add(char)
            
    return len(seen)
