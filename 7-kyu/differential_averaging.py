def add_to_average(current, points, add):
    if points == 0:
        return add

    return (current * points + add) / (points + 1)
