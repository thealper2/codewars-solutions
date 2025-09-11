import re

def vowel_start(sentence):
    s = re.sub(r'[^a-z0-9]', '', sentence.lower())
    result, word = [], ""
    vowels = "aeiou"
    
    for ch in s:
        if ch in vowels and word:
            result.append(word)
            word = ch
        else:
            word += ch
    if word:
        result.append(word)
    
    return " ".join(result)
