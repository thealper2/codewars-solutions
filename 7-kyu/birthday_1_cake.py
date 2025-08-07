def cake(candles,debris):
    if candles == 0:
        return "That was close!"
    
    total_fallen = 0
    for i in range(len(debris)):
        char = debris[i]
        if i % 2 == 0:
            total_fallen += ord(char)
        else:
            total_fallen += ord(char.lower()) - ord('a') + 1
    
    if total_fallen > 0.7 * candles:
        return "Fire!"
    else:
        return "That was close!"
