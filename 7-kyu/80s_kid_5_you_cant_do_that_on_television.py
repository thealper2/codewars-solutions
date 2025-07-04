def bucket_of(said):
    lower_str = said.lower()
    water_words = ['water', 'wet', 'wash']
    slime_phrases = ['i don\'t know', 'slime']
    
    has_water = any(word in lower_str for word in water_words)
    has_slime = any(phrase in lower_str for phrase in slime_phrases)
    
    if has_water and has_slime:
        return "sludge"
    elif has_water:
        return "water"
    elif has_slime:
        return "slime"
    else:
        return "air"
