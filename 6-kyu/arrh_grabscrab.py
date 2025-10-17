def grabscrab(said, possible_words):
    result = []
    sorted_said = sorted(said)
    
    for word in possible_words:
        if sorted(word) == sorted_said:
            result.append(word)
            
    return result
