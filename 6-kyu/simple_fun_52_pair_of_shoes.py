def pair_of_shoes(shoes):
    sizes = {}
    for shoe in shoes:
        t, size = shoe
        if t == 0:
            sizes[size] = sizes.get(size, 0) + 1
        else:
            sizes[size] = sizes.get(size, 0) - 1

    return all(v == 0 for v in sizes.values())