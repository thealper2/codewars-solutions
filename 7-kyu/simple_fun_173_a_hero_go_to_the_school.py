def which_bus_to_take(buses_colors, going_to_school):
    for i in range(len(buses_colors)):
        if going_to_school[i]:
            if buses_colors[i] == "red":
                return i

    for i in range(len(buses_colors)):
        if going_to_school[i]:
            if buses_colors[i] == "blue":
                return i

    return -1
