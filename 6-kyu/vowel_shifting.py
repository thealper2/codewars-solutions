def vowel_shift(text,n):
    if text == None:
        return None
    
    if n == 0:
        return text
    
    vowels = 'aeiouAEIOU'
    vowel_chars = []
    vowel_indices = []
    for i, c in enumerate(text):
        if c in vowels:
            vowel_chars.append(c)
            vowel_indices.append(i)
            
    if not vowel_chars:
        return text
    
    shifted_vowels = []
    for i in range(len(vowel_chars)):
        new_index = (i - n) % len(vowel_chars)
        shifted_vowels.append(vowel_chars[new_index])
        
    result = list(text)
    for i, idx in enumerate(vowel_indices):
        result[idx] = shifted_vowels[i]
        
    return ''.join(result)
