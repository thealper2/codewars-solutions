def score_a_hand(cards):
    suits = {'C', 'D', 'H', 'S'}
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    lead_suit = cards[0][-1]
    valid_cards = []
    for card in cards:
        if card[-1] == lead_suit:
            valid_cards.append(card)
            
    if not valid_cards:
        return cards[0]
    
    highest = valid_cards[0]
    for card in valid_cards[1:]:
        if values[card[:-1]] > values[highest[:-1]]:
            highest = card
            
    return highest
