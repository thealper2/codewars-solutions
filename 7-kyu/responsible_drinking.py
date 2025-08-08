def hydrate(drink_string): 
    words = drink_string.split()
    total = 0
    for word in words:
        if word.isdigit():
            total += int(word)
            
    return f"{total} glass{'es' if total > 1 else ''} of water"
