def get_free_urinals(urinals):
    urinals = list(urinals)
    x = len(urinals)
    count = 0

    for i in range(x - 1):
        if urinals[i] == "1" and urinals[i + 1] == "1":
            return -1

    for i in range(x):
        if urinals[i] == "0":
            if ((i == 0) or (urinals[i - 1] == "0")) and (
                (i == x - 1) or (urinals[i + 1] == "0")
            ):
                urinals[i] = "1"
                count += 1

    return count
