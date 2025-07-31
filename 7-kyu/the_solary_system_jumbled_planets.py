def jumbled_solar_system(solar_system):
    if not solar_system:
        return []

    size_order = {
        "Asteroid": 0,
        "Pluto": 1,
        "Mercury": 2,
        "Mars": 3,
        "Venus": 4,
        "Earth": 5,
        "Neptune": 6,
        "Uranus": 7,
        "Saturn": 8,
        "Jupiter": 9,
    }

    result = []
    for i in range(1, len(solar_system)):
        current = solar_system[i]
        previous = solar_system[i - 1]

        if current == "Asteroid" and previous == "Asteroid":
            result.append("=")
        elif size_order[current] > size_order[previous]:
            result.append(">")
        elif size_order[current] < size_order[previous]:
            result.append("<")
        else:
            result.append("=")

    return result
