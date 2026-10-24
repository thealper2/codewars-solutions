def fish(shoal):
    counts = [0] * 10
    for ch in shoal:
        counts[int(ch)] += 1

    size = 1
    progress = 0

    while True:
        ate = False
        for s in range(1, min(size, 9) + 1):
            if counts[s] > 0:
                progress += counts[s] * s
                counts[s] = 0
                ate = True

        needed = 4 * size
        if progress >= needed:
            progress -= needed
            size += 1
            continue

        if not ate:
            break

    return size