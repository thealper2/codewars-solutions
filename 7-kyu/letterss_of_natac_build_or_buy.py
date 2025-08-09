def build_or_buy(hand):
    result = []
    if 'b' in hand and 'w' in hand:
        result.append('road')
        if 's' in hand and 'g' in hand:
            result.append('settlement')
            
    if 'o' in hand and 'g' in hand:
        if 's' in hand:
            result.append('development')
            
        if hand.count('o') >= 3 and hand.count('g') >= 2:
            result.append('city')
            
    return result
        