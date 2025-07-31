def polydivisible(x):
    x = str(x)
    for i in range(1, len(x) + 1):
        sub_num = int(x[:i])
        if sub_num % i != 0:
            return False

    return True
