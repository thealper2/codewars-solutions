import re

def evenator(s):
    words = s.split()
    result = []
    
    for word in words:
        cleaned_word = re.sub(r'[^a-zA-Z0-9]', '', word)
        if not cleaned_word:
            continue
        
        if len(cleaned_word) % 2 != 0:
            cleaned_word += cleaned_word[-1]
        
        result.append(cleaned_word)
    
    return ' '.join(result)
