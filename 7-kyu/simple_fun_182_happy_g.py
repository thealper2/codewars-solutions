def happy_g(st):
    n = len(st)
    for i in range(n):
        if st[i] == "g":
            if i == 0:
                if st[i + 1] != "g":
                    return False
            elif i == n - 1:
                if st[i - 1] != "g":
                    return False

            elif st[i - 1] != "g" and st[i + 1] != "g":
                return False

    return True
