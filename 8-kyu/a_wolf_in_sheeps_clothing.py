def warn_the_sheep(queue):
    sheep_number = 0
    queue = list(reversed(queue))
    for i in range(len(queue)-1):
        if queue[i] == "sheep":
            sheep_number += 1
            if queue[i+1] == "wolf":
                return f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!'
    
    return "Pls go away and stop eating my sheep"