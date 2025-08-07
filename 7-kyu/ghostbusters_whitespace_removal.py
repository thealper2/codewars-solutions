def ghostbusters(building):
    result = ''.join([c for c in building if c != ' '])
    if result == building:
        return "You just wanted my autograph didn't you?"
    
    return result
