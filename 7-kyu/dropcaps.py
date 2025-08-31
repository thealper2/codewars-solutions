def drop_cap(words):
    result = ""
    word = ""
    for c in words:
        if c.isalpha():
            word += c
        else:
            if word:
                if len(word) > 2:
                    result += word.capitalize()
                else:
                    result += word
                    
                word = ""
                
            result += c
            
    if word:
        if len(word) > 2:
            result += word.capitalize()
        else:
            result += word

        word = ""
            
    return result
