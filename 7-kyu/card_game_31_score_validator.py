def score31(c1, c2, c3):
    def get_card_value(card):
        rank = card[1:] if len(card) > 2 else card[1]
        if rank in ['J', 'Q', 'K']:
            return 10
        elif rank == 'A':
            return 11
        else:
            return int(rank)
    
    def get_card_suit(card):
        return card[0]
    
    def get_card_rank(card):
        return card[1:] if len(card) > 2 else card[1]
    
    rank1, rank2, rank3 = get_card_rank(c1), get_card_rank(c2), get_card_rank(c3)
    
    if rank1 == rank2 == rank3:
        if rank1 == 'A':
            return 32
        else:
            return 30.5
    
    suit1, suit2, suit3 = get_card_suit(c1), get_card_suit(c2), get_card_suit(c3)
    
    if suit1 == suit2 == suit3:
        return get_card_value(c1) + get_card_value(c2) + get_card_value(c3)
    
    suits = {'S': 0, 'H': 0, 'D': 0, 'C': 0}
    
    for card in [c1, c2, c3]:
        suit = get_card_suit(card)
        value = get_card_value(card)
        suits[suit] += value
    
    return max(suits.values())
