def mormons(starting_number, reach, target):
    total = starting_number
    result = 0
    while total < target:
        total += total * reach
        result += 1

    return result