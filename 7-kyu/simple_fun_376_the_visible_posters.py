def count_visible(posters):
    wall = [0] * 1001
    for idx, (l, r) in enumerate(posters, 1):
        for i in range(l, r + 1):
            wall[i] = idx

    return len(set(wall) - {0})
