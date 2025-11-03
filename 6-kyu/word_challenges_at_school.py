from preloaded import WORD_LIST

def wanted_words(n, m, forbid_list):
    vowels = set('aeiou')
    result = []
    
    for word in WORD_LIST:
        if any(letter in word for letter in forbid_list):
            continue
            
        vowel_count = 0
        consonant_count = 0
        
        for c in word:
            if c in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
        if vowel_count == n and consonant_count == m:
            result.append(word)
            
    return result
