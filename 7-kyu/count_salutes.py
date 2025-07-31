def count_salutes(hallway):
    salutes = 0
    right_movers = 0
    for char in hallway:
        if char == '>':
            right_movers += 1
        elif char == '<':
            salutes += 2 * right_movers
    
    return salutes

    
