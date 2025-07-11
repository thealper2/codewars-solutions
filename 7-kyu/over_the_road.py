def over_the_road(address, n):
    total_houses = 2 * n
    if address % 2 == 1:
        return total_houses - address + 1
    else:
        return total_houses - address + 1
