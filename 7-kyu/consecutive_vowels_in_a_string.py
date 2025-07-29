def get_the_vowels(s):
    max_length = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in s:
        if vowels[max_length % 5] == c:
            max_length += 1
            
    return max_length