def cube_checker(volume, side):
    if volume == 0:
        return False

    if side < 0:
        return False

    return volume == side * side * side
