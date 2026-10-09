def find_the_ball(start, swaps):
    pos = start
    for a, b in swaps:
        if pos == a:
            pos = b
        elif pos == b:
            pos = a

    return pos