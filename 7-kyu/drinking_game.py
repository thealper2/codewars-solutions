def game(a, b):
    if a < 1 or b < 1:
        return "Non-drinkers can't play"
    
    beer = 1
    while True:
        if beer % 2 == 1:
            a -= beer
        else:
            b -= beer
            
        if a < 0:
            return "Joe"
        elif b < 0:
            return "Mike"
            
        beer += 1
