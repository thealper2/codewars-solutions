import math


def buses(kids, adults, places):
    if places == 0:
        return 0
    
    if kids == 0:
        return ((adults - 1) // places) + 1
    
    total_people = adults + kids
    min_buses = math.ceil(total_people / places)
    if min_buses > adults / 2:
        return 0
    
    return min_buses
