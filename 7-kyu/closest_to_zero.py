def closest(lst):
    closest = None
    min_distance = float("inf")

    for num in lst:
        distance = abs(num)

        if distance == 0:
            return 0

        if distance < min_distance:
            min_distance = distance
            closest = num
        elif distance == min_distance:
            if num != closest:
                closest = None

    return closest
