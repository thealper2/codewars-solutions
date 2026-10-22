def one_two_three():
    while True:
        a = one_two()
        b = one_two()
        if a == 1 and b == 1:
            return 1
        elif a == 1 and b == 2:
            return 2
        elif a == 2 and b == 1:
            return 3
