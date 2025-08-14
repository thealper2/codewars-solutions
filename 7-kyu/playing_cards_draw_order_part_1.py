def draw(deck):
    drawn = []
    while deck:
        top_card = deck.pop(0)
        drawn.append(top_card)
        if deck:
            next_card = deck.pop(0)
            deck.append(next_card)
    
    return drawn
