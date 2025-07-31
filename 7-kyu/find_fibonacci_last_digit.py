def get_last_digit(index):
    if index == 0:
        return 0

    elif index == 1 or index == 2:
        return 1

    a, b = 1, 1
    for _ in range(3, index + 1):
        a, b = b, (a + b) % 10

    return b
