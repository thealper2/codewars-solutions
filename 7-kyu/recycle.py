def recycle_me(rubbish):
    plastic = 0
    glass = 0
    card = 0
    
    for item in rubbish:
        if item > 0:
            plastic += 1
        elif item < 0:
            glass += 1
        else:
            card += 1
    
    return (plastic, glass, card)
