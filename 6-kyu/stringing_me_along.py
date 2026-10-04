def create_message(s):
    def message(next_word=None):
        if next_word is None:
            return s
        
        return create_message(s + " " + next_word)
    
    return message