def bulb_maze(maze):
    for i, room in enumerate(maze):
        if room == ' ':
            continue

        if room == 'o':
            if i % 2 == 0:
                return False
        elif room == 'x':
            if i % 2 == 1:
                return False

    return True
