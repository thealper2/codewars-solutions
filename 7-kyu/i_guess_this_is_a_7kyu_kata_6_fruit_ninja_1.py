def cut_fruits(fruits):
    result = []
    for fruit in fruits:
        if fruit in FRUIT_NAMES:
            n = len(fruit) + 1
            result.append(fruit[:n // 2])
            result.append(fruit[n // 2:])
        else:
            result.append(fruit)
    return result
