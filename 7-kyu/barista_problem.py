def barista(coffees):
    if not coffees:
        return 0
    
    coffees.sort()
    total_wait = 0
    elapsed = 0
    for i, time in enumerate(coffees):
        elapsed += time
        total_wait += elapsed
        if i != len(coffees) - 1:
            elapsed += 2
            
    return total_wait
