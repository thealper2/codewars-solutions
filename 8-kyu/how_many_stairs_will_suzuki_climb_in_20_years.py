def stairs_in_20(stairs):
    return sum([sum([_ * 20 for _ in array]) for array in stairs])
