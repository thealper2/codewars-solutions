def sort_cards(cards):
    order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    return sorted(cards, key=lambda x: order.index(x))
