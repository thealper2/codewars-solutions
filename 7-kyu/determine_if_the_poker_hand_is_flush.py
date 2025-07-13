def is_flush(cards):
    suit = cards[0][-1]
    return all(card[-1] == suit for card in cards)