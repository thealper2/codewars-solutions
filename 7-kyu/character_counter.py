def validate_word(word):
    prev = False
    word = word.lower()
    for c in word:
        c_count = word.count(c)
        if prev and c_count != prev:
            return False
        
        prev = c_count
        
    return True
