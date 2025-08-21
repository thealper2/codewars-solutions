import math


def number_lappings(my_speed, ghost_speed, time, round_length):
    if my_speed <= ghost_speed:
        return 0
    
    counter = ((my_speed - ghost_speed) * time) / round_length
    return math.floor(counter) - (1 if counter % 1 == 0 else 0)
