from preloaded import DECK

def deal(deal_number):
    deck = list(DECK)
    state = deal_number
    result = []
    n = 52
    for i in range(52):
        state = (state * 214013 + 2531011) % (2**31)
        rand = state // (2**16)
        index = rand % n
        card = deck[index]
        if index != n - 1:
            deck[index] = deck[n - 1]
            
        result.append(card)
        n -= 1
        
    return result
