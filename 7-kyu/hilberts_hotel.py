import math

def hilberts_hotel(rooms, people, buses):
    guests = list(rooms)
    people_inf = (people == math.inf)
    buses_inf  = (buses  == math.inf)

    if not people_inf and not buses_inf:
        n = people * buses
        return [r + n for r in guests]

    if people_inf and buses_inf:
        return [r * (r + 1) // 2 for r in guests]

    factor = buses if people_inf else people
    return [r * (factor + 1) for r in guests]
