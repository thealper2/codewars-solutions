def last_survivor(letters, coords): 
    letters = list(letters)
    for coord in coords:
        letters.pop(coord)
        
    return letters[0]
