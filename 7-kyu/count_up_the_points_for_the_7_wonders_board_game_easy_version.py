def seven_wonders_science(compasses, gears, tablets):
    points = compasses**2 + gears**2 + tablets**2
    while compasses > 0 and gears > 0 and tablets > 0:
        compasses -= 1
        gears -= 1
        tablets -= 1
        points += 7

    return points
