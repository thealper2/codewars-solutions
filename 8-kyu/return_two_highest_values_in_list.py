def two_highest(arg1):
    if len(arg1) == 0:
        return []

    arg1 = list(set(arg1))
    for i in range(len(arg1) - 1, 0, -1):
        for j in range(i):
            if arg1[j] < arg1[j + 1]:
                arg1[j], arg1[j + 1] = arg1[j + 1], arg1[j]

    return arg1[:2] if len(arg1) > 1 else arg1
