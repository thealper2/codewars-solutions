def gaslighting(shirt_word:str, your_word:str, friends_letters:str) -> bool:
    if shirt_word == your_word:
        return False
    
    for a, s in zip(shirt_word, your_word):
        if a != s:
            if a in friends_letters or s in friends_letters:
                return True
    
    return False
