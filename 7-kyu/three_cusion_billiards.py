def has_scored(s):
    cushions = []
    object_balls = []

    for l in s:
        if l.islower():
            cushions.append(l)
        elif l.isupper() and l not in object_balls:
            object_balls.append(l)

        if len(object_balls) == 2:
            return len(cushions) >= 3

    return False
