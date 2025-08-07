def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    
    if size <= 3:
        return phrase[:size] + "..."
    
    return phrase[:size - 3] + "..."
